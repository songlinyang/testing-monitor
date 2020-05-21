# -*- coding:utf-8 -*-
import os,sys
import requests
import json
import traceback
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from utils import config
import configparser as cparser
cf = cparser.ConfigParser()
cf.read(BASE_PATH+"/config.ini")

class Uploader():

    def __init__(self):
        self.base_url = cf.read("Uploader","base_url")

    def upload_action(self,report_path,file_name):
        try:
            url = self.base_url + "/upload"
            file_path = str(os.path.join(report_path,file_name)).replace("\\","/")
            file_path = file_path.replace("//","/")
            payload = {"file":open(file_path,'rb')}
            print(payload)
            response = requests.post(url, files=payload)

            print(response.text)
        except Exception as e:
            traceback.print_exc()
        finally:
            return True


    def get_domain(self):
        url = self.base_url + "/uploads"
        return url

# if __name__ == "__main__":
#     upLoader=Uploader()
#     upLoader.upload_action(config.PICTURE_PATH,"2019-07-11-10_picture_result.png","2019-07-11")
#     print(upLoader.get_file_action("2019-07-11-10_picture_result.png"))
