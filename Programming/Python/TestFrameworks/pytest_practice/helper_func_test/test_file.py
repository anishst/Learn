import pytest

#  This tests Class based helper function
@pytest.mark.usefixtures("setup")
def test_SFTPHelper_class(SFTHelpers):
    location = 'DG'
    env = 'QAEF'
    file_list = ["file1", "file2"]
    SFTHelpers.download_files(file_list, env, location)

#  This tests function based helper function
@pytest.mark.usefixtures("setup")
def test_download_file_function(download_file):
    print("Test download")
    download_file()