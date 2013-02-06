

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
6. Sit back and relax.

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

## Deploy

## Domain Setup
