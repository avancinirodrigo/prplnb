import filecmp
from application.usecases.response import Success, NotFound
from application.usecases.signup import SignUp, SignUpData
from application.usecases.storage_manager import StorageManager
from tests.tests_helper import TestsHelper


def test_add_file_fs_happy(db, dsfs):
    signupData = SignUpData('avancinirodrigo', 'avancini')
    signupUc = SignUp(signupData)
    signupUc.execute(db)
    dataDir = TestsHelper.GetDataDirPath()
    filepath = f'{dataDir}/restful-web-services.pdf'
    file_b = open(filepath, 'rb')
    uc = StorageManager(db, dsfs)
    out = uc.add_file(signupData.to_dict(), file_b, '/docs/review/review.pdf')
    assert isinstance(out.response_type, Success)
    
    out_get = uc.get_file(signupData.to_dict(), '/docs/review/review.pdf', 0)
    file_b01 = out_get.data['file_bytes']
    assert isinstance(out_get.response_type, Success)
    assert file_b01.read() == open(filepath, 'rb').read()

def test_add_file_revision_happy(db, dsfs):
    signupData = SignUpData('avancinirodrigo', 'avancini')
    signupUc = SignUp(signupData)
    signupUc.execute(db)
    dataDir = TestsHelper.GetDataDirPath()
    filepath0 = f'{dataDir}/restful-web-services.pdf'
    file_b0 = open(filepath0, 'rb')
    uc = StorageManager(db, dsfs)
    uc.add_file(signupData.to_dict(), file_b0, '/docs/review/review.pdf')
    
    filepath1 = f'{dataDir}/Full-Stack-Engineer-Test.pdf'
    file_b1 = open(filepath1, 'rb')
    out = uc.add_file(signupData.to_dict(), file_b1, '/docs/review/review.pdf')
    assert isinstance(out.response_type, Success)

    out_get0 = uc.get_file(signupData.to_dict(), '/docs/review/review.pdf', 0)
    file_b00 = out_get0.data['file_bytes']

    out_get1 = uc.get_file(signupData.to_dict(), '/docs/review/review.pdf', 1)
    file_b11 = out_get1.data['file_bytes']
    assert isinstance(out_get1.response_type, Success)
    assert file_b11.read() == open(filepath1, 'rb').read()
    assert file_b11.read() != file_b00.read()

def test_get_last_revision(db, dsfs):
    signupData = SignUpData('avancinirodrigo', 'avancini')
    signupUc = SignUp(signupData)
    signupUc.execute(db)
    dataDir = TestsHelper.GetDataDirPath()
    
    filepath0 = f'{dataDir}/restful-web-services.pdf'
    file_b0 = open(filepath0, 'rb')
    uc = StorageManager(db, dsfs)
    uc.add_file(signupData.to_dict(), file_b0, '/docs/review/review.pdf')    

    filepath1 = f'{dataDir}/Full-Stack-Engineer-Test.pdf'
    file_b1 = open(filepath1, 'rb')
    uc.add_file(signupData.to_dict(), file_b1, '/docs/review/review.pdf')
    
    out_get = uc.get_file(signupData.to_dict(), '/docs/review/review.pdf')
    file11 = out_get.data['file']
    file_b11 = out_get.data['file_bytes']

    assert isinstance(out_get.response_type, Success)
    assert file11.revision == 1
    assert open(filepath1, 'rb').read() == file_b11.read()

def test_get_file_not_found(db, dsfs):
    signupData = SignUpData('avancinirodrigo', 'avancini')
    signupUc = SignUp(signupData)
    signupUc.execute(db)
    uc = StorageManager(db, dsfs)    
    out = uc.get_file(signupData.to_dict(), '/docs/review/review.pdf')
    assert isinstance(out.response_type, NotFound)