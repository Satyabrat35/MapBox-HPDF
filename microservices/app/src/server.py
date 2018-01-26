from src import app
from flask import render_template, request, json ,flash
import requests
import json


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/sup")
def sup():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # This is the url to which the query is made
    url = "https://auth.coalitionist99.hasura-app.io/v1/signup"

    # This is the json payload for the query
    params = {
        "provider": "username",
        "data": {
            "username": username,
            "password": password
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer f82e920a8d6d584fe1ad8231f1e64ad417a41679a63fc327"
    }

    # Make the query and store response in resp
    #resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
    if request.form['password'] == request.form['conf_password']:
        resp=requests.request("POST",url=url,data=json.dumps(params),headers=headers)
        print(resp.content)
        sq = json.loads(resp.content)
        if "message" in sq.keys():
            flash(sq["message"])
        else:
            flash("User created! Please login to continue")
            return render_template('login.html')
    else:
        flash('Password do not match')        


    # resp.content contains the json response.
    #flash('Password do not match')
    return render_template('signup.html')

@app.route("/signin", methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    # This is the url to which the query is made
    #url = "https://auth.coalitionist99.hasura-app.io/v1/signup"
    # This is the url to which the query is made
    url = "https://auth.coalitionist99.hasura-app.io/v1/login"

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": username,
            "password": password
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    #auth_token=None
    #name = None
    print(resp.content)
    data = json.loads(resp.content)
    if "message" in data.keys():
        flash(data["message"])
    else:
        auth_token = data["auth_token"]
        name = data["username"]
        flash("Hello {}".format(data["username"]))
        return render_template('wel.html',auth_token=auth_token ,name=name)
    return render_template('login.html')
    
@app.route('/locate')
def loc():
    return render_template('locate.html')

@app.route('/navigate')
def navigate():
    return render_template('navigate.html')    