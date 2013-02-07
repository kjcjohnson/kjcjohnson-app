import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello Michigan Hackers'

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 3000))
	print("We have liftoff!")
	app.run(host='0.0.0.0', port=port, debug=True)

