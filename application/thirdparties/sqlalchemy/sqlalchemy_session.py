from sqlalchemy import create_engine, exc
from application.dataaccess.session import Session


class SqlAlchemySession(Session):
	def __init__(self, session):
		self._session = session

	def commit(self):
		try:
			self._session.commit()
		except exc.IntegrityError as e:
			self._session.rollback()
			self._session.close()
			if 'NotNullViolation' in str(e):
				raise NotNullViolationException('Object violates not-null constraint.')
			else:
				raise e

	def add(self, object):
		self._session.add(object)

	def delete(self, object):
		self._session.delete(object)

	def expunge(self, object):
		self._session.expunge(object)

	def close(self):
		self._session.close()

	def query(self, object):
		return self._session.query(object)     


class NotNullViolationException(Exception):
	pass