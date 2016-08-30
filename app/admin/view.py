# -*- coding:utf-8 -*-
from flask import url_for, request, redirect, flash
from flask_admin import AdminIndexView, expose, form
from flask_admin.contrib.mongoengine import ModelView
from flask_login import login_required, login_user, logout_user, current_user
from form import LoginForm
from wtforms import fields, widgets
from app.models import User
from werkzeug.security import check_password_hash


class CKTextAreaWidget(widgets.TextArea):
	def __call__(self, field, **kwargs):
		existing_classes = kwargs.pop('data-provide', '') or kwargs.pop('data-provide_', '')
		kwargs['data-provide'] = u'%s%s' % (existing_classes, "markdown")
		existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
		return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
	widget = CKTextAreaWidget()


class MyIndexView(AdminIndexView):
	@expose('/')
	@login_required
	def index(self):
		return self.render('admin/index.html')

	@expose('/login', methods = ['GET','POST'])
	def login(self):
		form = LoginForm()
		if form.validate_on_submit():
			user = User.objects(name = form.name.data).first()
			next = None
			if user and check_password_hash(user.password, form.password.data):
				login_user(user)
				flash(u'登录成功')
				next = request.args.get('next')
			else:
				flash(u'密码错误')
			return redirect(next or url_for('.login'))
		return self.render('admin/login.html', form=form)

	@expose('/logout')
	def logout(self):
		logout_user()
		return redirect(url_for('.index'))


class UserView(ModelView):

	def is_accessible(self):
		return current_user.is_authenticated

	can_create = False
	can_delete = False


class PostView(ModelView):
	form_overrides = dict(	content= CKTextAreaField,
							)
	create_template = 'admin/create.html'
	edit_template = 'admin/edit.html'
	column_choices = {'status':[(0, u'草稿'),(1, u'公开')]}
	column_list = ('title', 'content', 'author', 'series', 'tags', 'status', 'create_time', 'modify_time')
	form_args = dict(	title = dict(label = u'标题'),
						content = dict(label = u'内容'),
						author = dict(label = u'作者'),
						series = dict(label = u'所属系列'),
						tags = dict(label = u'标签'),
						status = dict(label = u'状态'),
						create_time = dict(label = u'创建时间'),
						modify_time = dict(label = u'修改时间'))
	form_rules = [form.rules.FieldSet(('title','content','author','series','tags','status','create_time','modify_time'))]

	def is_accessible(self):
		return current_user.is_authenticated


class MessageView(ModelView):

	def is_accessible(self):
		return current_user.is_authenticated



