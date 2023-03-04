#from application.dataaccess.database_manager import DatabaseManager
from application.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


db = SqlAlchemyDatabase()
#DatabaseManager = DatabaseManager(db)