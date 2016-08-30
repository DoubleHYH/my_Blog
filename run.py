from app import creatApp

app = creatApp()

if __name__ == '__main__':
	app.run(host = '127.0.0.1',port = 5000, debug = True)
