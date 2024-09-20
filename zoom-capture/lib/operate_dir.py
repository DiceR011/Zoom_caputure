import os,zipfile
import datetime as dt

def daily_dir():
    dt_now = dt.datetime.now()
    yyyymmdd = dt_now.strftime('%y%m%d')
    create_directory = os.getcwd() + '\\' + 'Screenshot' + '\\' + yyyymmdd
    
    if(not (os.path.exists(create_directory))):
        os.mkdir(create_directory)
    
    return create_directory

def zip_folder(folder_path, output_zip_path):
    """フォルダをZIP圧縮する関数"""
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                # 圧縮ファイルにフォルダ構造を保持して追加
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f"Folder '{folder_path}' has been zipped as '{output_zip_path}'")