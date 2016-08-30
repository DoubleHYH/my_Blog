# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Email

class SendForm(Form):
	name = StringField('Name', validators = [Required()])
	email = StringField('Email', validators = [Email(), Required()])
	message = TextAreaField('Message', validators = [Required()])
	sbumit = SubmitField(u'发送')
