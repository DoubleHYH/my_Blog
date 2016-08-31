from flask_script import Manager, Server
from app import creatApp
from app.models import User, Post
from werkzeug.security import generate_password_hash

app = creatApp()
manager = Manager(app)

manager.add_command("runserver",
					Server(host='127.0.0.1',
							port=5000,
							use_debugger=True))
@manager.option('-u', '--name', dest='mName', default='admin')
@manager.option('-p', '--password', dest='mPassword', default='123456')
def addUser(mName,mPassword):
	admin = User(name=mName, password=generate_password_hash(mPassword))
	admin.save()

@manager.command
def addPost():
	user = User.objects(name="admin").first()
	post = Post(title = "%shello"%x,
				content = "hello world",
				author = user,
				tags = ['python','flask'],
				status = 1)
	post.save()

@manager.command
def test():
	pass

if __name__ == "__main__":
	manager.run()


