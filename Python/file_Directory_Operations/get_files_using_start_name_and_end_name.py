import os

def verify_jaser_report_file_download(start_value, end_value):
    # download_location = os.path.expandvars('%userprofile%/Downloads/')
    try:
        download_location = os.environ['USERPROFILE']+ '/Downloads'
        # download_location = r'C:\Users\532975\Downloads'
        files_found = [filename for filename in os.listdir(download_location) if filename.startswith(start_value) and filename.endswith(end_value)]
        if files_found:
            print(f"Found file: {files_found}")
        else:
            print("no files found")
    except Exception as e:
        print(f"Error handle file check: {e}")



verify_jaser_report_file_download('AgencyCIRA', 'pdf')
