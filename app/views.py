# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, Blueprint, request
from flask import flash
from form import SendForm
from models import Post, Message

blog = Blueprint('blog',__name__)

@blog.route('/')
@blog.route('/<int:page>')
def index(page=1):
	paginator = Post.objects.paginate(page=page, per_page=5)
	return render_template("index.html", paginator=paginator)

@blog.route('/post/<string:postId>')
def postView(postId):
	post = Post.objects(id = postId).first()
	return render_template('single.html', post = post)

@blog.route('/about')
def about():
	return render_template('about.html')

@blog.route('/contact', methods = ['GET','POST'])
def contact():
	form = SendForm()
	if form.validate_on_submit():
		message = Post(name = form.name.data,
				email = form.email.data,
				content = form.message.data)
		message.save()
		flash(u'留言已保存')
		return redirect(url_for('blog.contact'))
	return render_template('contact.html', form = form)

@blog.route('/search')
def search():
	findStr = request.args.get('find')
	if findStr:
		post1 = Post.objects(title__contains = findStr).all()
		post2 = Post.objects(content__contains = findStr).all()
		post = post1 or post2
		return render_template('list.html', post = post)
	return render_template('list.html')

