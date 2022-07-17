from marshmallow import Schema, fields
from pymysql import Time

#parameter(schema)
class CommonResponse(Schema):
	message = fields.Str()
	data = fields.Dict()
	datatime = fields.Str()
class diary_log_field(CommonResponse):
	Class = fields.Str()
	Name = fields.Str()
	Time = fields.DateTime()
	Project = fields.Str(required=True)
	Workinghours = fields.Str(required=True)
	Imgurl = fields.Str(required=True)
	Content  = fields.Str(required=True)
class diary_log_delete(CommonResponse):
	Project = fields.Str()
class message_field(CommonResponse):
	Content = fields.Str()
	Title = fields.Str()
	Access = fields.Str(required=True)
	studentclass = fields.Str()
	studentname = fields.Str()
	ReplyContent = fields.Str()
	LeavingTime = fields.DateTime()
############
############
class LoginRequest(Schema):
    Password = fields.Str(doc="Password", required=True)
    Name = fields.Str(doc="Name",required=True)
    Class = fields.Str(doc="Class",required=True)
    Access = fields.Str()
    Email = fields.Str()
    Id = fields.Int()
class auto(CommonResponse):
    Name = fields.Str(doc="Name",required=True)
    Class = fields.Str(doc="Class",required=True)

class StatusReqest(Schema):
    Email = fields.Str(doc="Time", required=True)
    Password = fields.Str(doc="Content", required=True)

class Account(Schema):
	Id = fields.Int(doc="Id")
	Name = fields.Str(doc="Name")
	Email = fields.Str(doc="Email")
	Password = fields.Str(doc="Password")
	##Class=type+number
	type = fields.Str()
	number = fields.Str()
class upload_personaldata(Schema):
	file = fields.Raw(type = 'file',doc = "file")
class AccountDelete(Schema):
	Name = fields.Str(required=True)
	type = fields.Str()
	number = fields.Str()
#########
###管理端
class ManagerReadList(Schema):
    type = fields.Str(doc="class_type",required=True)
    number = fields.Str(doc="class_number",required=True)
    Name = fields.Str(doc="class_name")
    project = fields.Str(doc="project",required=True)
    date_from = fields.Str(doc="date_from",required=True)
    date_to = fields.Str(doc="date_to",required=True)
class typing_rate(Schema):
	Class = fields.Str(required=True)
	Time = fields.Str(doc="date_from",required=True)

