# -*- coding:utf-8 -*-

from flask_admin import Admin
from view import MyIndexView, UserView, PostView, MessageView
from app.models import User, Post, Message

def create_admin(app = None):
	admin = Admin(	app,
					name = u'后台管理',
					index_view = MyIndexView(),
					template_mode='bootstrap3')
	admin.add_view(UserView(User))
	admin.add_view(PostView(Post))
	admin.add_view(MessageView(Message))
