import os, logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from lib import operate_dir
import datetime as dt

#デバックレベルのログを出力
logging.basicConfig(level=logging.DEBUG)


load_dotenv(verbose=True)

slack_token = os.getenv("SLACK_TOKEN")
slack_channel = os.getenv("CHANNEL_ID")
client = WebClient(token=slack_token)

# # daily_path = operate_dir.daily_dir()
# # dt_now = dt.datetime.now()
# # yyyymmdd = dt_now.strftime('%y%m%d')
# # zip_daily_path = os.getcwd() + '\\' + 'Zip_Screenshot' + '\\' + yyyymmdd + '.zip'

# operate_dir.zip_folder(daily_path, zip_daily_path)

# トークンが正しいか確認します
auth_test = client.auth_test()
bot_user_id = auth_test["user_id"]
print(f"App's bot user: {bot_user_id}")


