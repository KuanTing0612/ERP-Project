from flask import Flask
from flask_restful import  Api
from dbmodel import *
import configs as CONFIGS
from flask_cors import CORS
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
app = Flask(__name__)
api = Api(app)
app.config.from_object(CONFIGS)
CORS = "CORS(app,resources=r'/.*')"##允許跨域請求
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)
api.add_resource(Diary_Log,'/DiaryLog/<string:Class>/<string:Name>')
docs.register(Diary_Log)
api.add_resource(Message,'/Message/<string:Class>/<string:Name>')
docs.register(Message)
api.add_resource(Login,'/login')
docs.register(Login)
api.add_resource(Status,'/status/<string:Class>/<string:Name>')
docs.register(Status)
api.add_resource(Account_management,'/account')
docs.register(Account_management)
api.add_resource(Manager_read_diary,'/ReadDiaryLog')
docs.register(Manager_read_diary)
api.add_resource(Get_datalist,'/Getdatalist')
docs.register(Get_datalist)
api.add_resource(typing_rate,'/typing_rate')
docs.register(typing_rate)
if __name__ == '__main__':
    app.run(port=8050,host="0.0.0.0")