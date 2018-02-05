from src import app
from flask import render_template, request, json ,flash , make_response
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

@app.route("/change_p")
def cpass():
	return render_template('change_password.html')    

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
    #print(resp.content)
    data = json.loads(resp.content)
    if "message" in data.keys():
        flash(data["message"])
    else:
        name = data["username"]
        rsp = make_response(render_template('wel.html',name=name))
        rsp.set_cookie('Auth_Token',data["auth_token"])
        rsp.set_cookie('Name',data["username"])
        #flash("Hello {}".format(data["username"]))
        return rsp
    return render_template('login.html')
    
@app.route('/locate')
def loc():
    return render_template('locate.html')

@app.route('/navigate')
def navigate():
    return render_template('navigate.html')


#@app.route('/navigate_2')
#def navigate_2():
#	return render_template('navigate_2.html')    
# For extra additions

@app.route('/logout')
def logout():
    auth_token = request.cookies.get('Auth_Token')
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + str(auth_token)
    }    
    url = "https://auth.coalitionist99.hasura-app.io/v1/user/logout"

    resp = requests.request("POST",url,headers=headers)
    data = json.loads(resp.content)
    #session.clear()
    if "message" in data.keys():
        flash(data["message"])
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/back')
def back():
	name = request.cookies.get('Name')
	return render_template('wel.html',name=name)

@app.route('/change_pass',methods=['POST'])
def change_pass():
	old_password = request.form['old_password']
	new_password = request.form['new_password']
	auth_token = request.cookies.get('Auth_Token')
	headers = {
		"Content-Type": "application/json",
        "Authorization": "Bearer " + str(auth_token)
	}
	requestPayload = {
		"old_password": old_password,
		"new_password": new_password
	}
	url = "https://auth.coalitionist99.hasura-app.io/v1/providers/username/change-password"

	if request.form['new_password'] == request.form['conf_new_password']:
		resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
		data = json.loads(resp.content)
		if "message" in data.keys():
			flash(data['message'])
			return render_template('login.html')
	else:
		flash('Password do not match')
		return render_template('change_password.html')		