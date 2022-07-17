import imp
from typing import Coroutine
from flask import Flask
from flask_restful import  Api
from dbmodel import *
from apispec import APISpec #產出sweg文件
import configs as CONFIGS
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
CORS = "CORS(app,resources=r'/.*')"##允許跨域請求
app.config.from_object(CONFIGS)
api.add_resource(Diary_Log,'/DiaryLog/<string:Class>/<string:Name>')
api.add_resource(Message,'/Message/<string:Class>/<string:Name>')
api.add_resource(Login,'/login')
api.add_resource(Status,'/status/<string:Class>/<string:Name>')
api.add_resource(Account_management,'/account')
api.add_resource(Manager_read_diary,'/ReadDiaryLog')
api.add_resource(Get_datalist,'/Getdatalist')

if __name__ == '__main__':
    app.run()