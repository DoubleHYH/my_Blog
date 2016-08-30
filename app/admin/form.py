# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
	name = StringField(u'用户名',validators = [Required()])
	password = PasswordField(u'密码',validators = [Required()])
	sbumit = SubmitField(u'登录')
