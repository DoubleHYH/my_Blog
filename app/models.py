# -*- coding:utf-8 -*-
from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from datetime import datetime

db = MongoEngine()

class User(UserMixin,db.Document):
	name = db.StringField(required=True, max_length=64)
	password = db.StringField(max_length=256)
	email = db.StringField(max_length=64)
	description = db.StringField(max_length=1024)

	def __unicode__(self):
		return self.name


class Post(db.Document):
	title = db.StringField(required = True, max_length = 64)
	content = db.StringField(required = True)
	author = db.ReferenceField(User)
	series = db.StringField(max_length = 32)
	tags = db.ListField(db.StringField(max_length = 32))
	status = db.BooleanField(required = True, default = False)
	create_time = db.DateTimeField(default = datetime.now)
	modify_time = db.DateTimeField(default = datetime.now)
	meta = {'ordering': ['-create_time']}


class Message(db.Document):
	name = db.StringField(required = True)
	email = db.StringField(required = True)
	content = db.StringField(required = True)
	create_time = db.DateTimeField(default = datetime.now)
