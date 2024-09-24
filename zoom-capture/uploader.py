import os
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from lib import operate_dir
import datetime as dt

while True:
    print('今日のフォルダをアップロードしますか？(y/n)')
    f = input()
    
    if f == 'y':
        break
    elif f == 'n':
        exit()
    else:
        continue

# デバッグレベルのログを出力
logging.basicConfig(level=logging.DEBUG)

load_dotenv(verbose=True)

slack_token = os.getenv("SLACK_TOKEN")
slack_channel = os.getenv("CHANNEL_ID")
client = WebClient(token=slack_token)

# 今日の日付のフォルダを操作
daily_path = operate_dir.daily_dir()

# 日付のフォーマットを指定
dt_now = dt.datetime.now()
yyyymmdd = dt_now.strftime('%y%m%d')

# 圧縮ファイルの保存先パスを生成
zip_daily_path = os.path.join(os.getcwd(), 'Zip_Screenshot', f'{yyyymmdd}.zip')

# フォルダをZIPファイルに圧縮
operate_dir.zip_folder(daily_path, zip_daily_path)

# Slackにファイルをアップロードする関数
def upload_file_to_slack(channel_id, file_path):
    try:
        # ファイルが存在するか確認
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            return

        # 新しい推奨のfiles_upload_v2を使用してファイルのアップロード
        with open(file_path, "rb") as file_content:
            response = client.files_upload_v2(
                channel=channel_id,  # 推奨されている`channel`を使用
                file=file_content,   # ファイルオブジェクトとして渡す
                title=os.path.basename(file_path)
            )
        print(f"File uploaded: {response['file']['id']}")
    except SlackApiError as e:
        print(f"Error uploading file: {e.response['error']}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Slackにファイルをアップロード
upload_file_to_slack(slack_channel, zip_daily_path)