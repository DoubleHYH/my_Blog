# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from admin import create_admin
from models import db, Post, User
from views import blog
from flaskext.markdown import Markdown
from flask_login import LoginManager


def creatApp():
	app = Flask(__name__)
	Bootstrap(app)
	app.config.from_object('config')
	registerDatabase(app)
	registerBlueprints(app)
	create_admin(app)
	registerMarkdown(app)
	registerTagsFilter(app)
	registerLogin(app)
	return app

def registerDatabase(app):
	db.init_app(app)

def registerBlueprints(app):
	app.register_blueprint(blog)

def registerMarkdown(app):
	Markdown(app)

def registerTagsFilter(app):

	@app.template_filter('mSeries')
	def getSeries(tag):
		return []

	@app.template_filter('mArchive')
	def getArchive(tag):
		return []

	@app.template_filter('mTagCloud')
	def getTags(tag):
		tags = reduce(lambda x,y:x+y,[tmp.tags for tmp in Post.objects.only('tags').all()])
		return sorted({tmp:tags.count(tmp) for tmp in set(tags)}.iteritems(), key=lambda x : x[1],reverse = True)

def registerLogin(app):
	loginManager = LoginManager()
	loginManager.init_app(app)
	loginManager.login_view = "admin.login"
	loginManager.login_message = u'请先登录'
	@loginManager.user_loader
	def loadUser(user_id):
		return User.objects(id=user_id).first()

if __name__ == '__main__':
	app.run(debug = True)
