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


def get_only_latest_file(start_value, end_value):
    download_location = os.environ['USERPROFILE'] + '/Downloads'
    files_found = [filename for filename in os.listdir(download_location) if
                   filename.startswith(start_value) and filename.endswith(end_value)]
    print(files_found)
    for name in sorted(files_found, key=lambda name: os.path.getmtime(os.path.join(download_location, name))):
        print(name)
    paths = [os.path.join(download_location, basename) for basename in files_found]
    latest_file = max(paths, key=os.path.getmtime)
    print(latest_file)

def using_glob(start_value, end_value):
    import glob
    import os
    download_location = os.environ['USERPROFILE'] + '/Downloads'
    list_of_files = glob.glob(download_location + '/' + start_value + '*.' + end_value)  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print("Using glob: ")
    print(latest_file)

verify_jaser_report_file_download('BatchList', 'pdf')
get_only_latest_file('BatchList', 'pdf')
using_glob('BatchList', 'pdf')

