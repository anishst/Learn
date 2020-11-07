import pytest

# global var
pytest.connObject = None

@pytest.yield_fixture(scope="session")
def setup():
    print("\nSetting up FTP Connection object")
    m = "DB OBJECT"
    pytest.connObject = m
    yield
    print("\nClosing FTP Connection")

class SFTPHelper:

    @staticmethod
    def download_files(file_list, env, location):
        print(f"Connecting to {pytest.connObject}")
        save_location = f"DataFiles/{env}/"
        for file in file_list:
            folder_path = f"/data/{env}/{location}/ARCHIVE"
            print(f"Downloding file {file} from {folder_path} in {env} ")
            print(f"Saving file in {save_location}")



@pytest.fixture
def SFTHelpers():
    return SFTPHelper

def download_files():
    print(f"Connecting to {pytest.connObject}")
    print("Downloading files!!!")


@pytest.fixture
def download_file():
    return download_files