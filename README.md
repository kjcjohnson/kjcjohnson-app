

# Heroku and Python Deployment Demo

You’ll learn how to register a domain name, configure your DNS, and deploy a basic website using Heroku!


### Things you should have already:
- [GitHub](http://github.com) account.
- [Heroku](http://heroku.com) account.
- Account with domain registrar of choice. [This one is simple.](http://iwantmyname.com)
- Fingers to type with.

### Things we're gonna do.
1. Write a dead simple app in [Python](http://python.org) using [Flask](http://flask.pocoo.org/)
2. Run our app locally.
3. Deploy said app to *the cloud* via Heroku.
4. Register a domain.
5. Setup DNS to point to our app.

## Simple Flask App

- Clone this repo: `git clone git@github.com:michiganhackers/heroku-py-demo.git`
- Install Virtualenv: `pip install virtualenv` (may need `sudo`).  
(If you're wondering, this is for creating an isolated python environment.)
- Run `virtualenv venv --distribute` to start up a virtual environment. 
- Run: `source venv/bin/activate` to start up the virtualenv.
- Install Flask: `pip install -r requirements.txt`.

Now we are ready to run it!

- Type `python hello.py` to run the app.
- Navigate to `http://localhost:3000/`
- Notice if you make changes to the file the server will restart.

Notes:
- The `Procfile` is used by Heroku to start your app.
- Heroku uses `Foreman` to run your app, you can too! Try `foreman start`.
- If you add new pip modules use `pip freeze > requirements.txt` before deploying.
(This way Heroku knows what your dependencies are.)

## Deploy


- `heroku login`
- `heroku create [yourappname]` Make up a great app name.
- `git push heroku master` (If you dont have an ssh key on Heroku see below.)  

Heroku will install dependences and launch your app here. Magic!

- `heroku ps:scale web=1` This gives your app 1 `web worker`.
- `heroku open` This will go to yourappname.herokuapp.com
- Grab a beer.

SSH Key Upload:
- open new terminal window and type `cat .ssh/id_rsa.pub`
- if no file exists type `ssh-keygen` then hit enter (dont name a file)
- type a password if you want extra security. (Jack is wincing right now).
- type `cat .ssh/id_rsa.pub` again and copy only the printed lines.
- go to your [account page](http://dashboard.heroku.com/account) and paste in the ssh key.

## Domain Setup


