import os
import datetime as dt

def daily_dir():
    dt_now = dt.datetime.now()
    yyyymmdd = dt_now.strftime('%y%m%d')
    create_directory = os.getcwd() + '\\' + 'Screenshot' + '\\' + yyyymmdd
    
    if(not (os.path.exists(create_directory))):
        os.mkdir(create_directory)
    
    return create_directory