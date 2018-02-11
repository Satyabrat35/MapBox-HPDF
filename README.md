# MapBox

 Hasura project on [Mapbox](https://www.mapbox.com/) Geolocation API


## Getting started

Follow these steps to get started with development using this project

		hasura-cli

In order to get started with development you have to install the hasura cli.To install copy this code to your terminal 

		$ curl -L https://hasura.io/install.sh | bash

Once installed login to hasura using

		$ hasura login
        
A login page would open up in your default browser , sign up or login to access the hasura dashboard. Clone the project by copying the following code to your terminal 

		$ git clone https://github.com/Satyabrat35/MapBox-HPDF.git

### Prerequisites

- [Hasura CLI](https://docs.hasura.io/0.15/manual/install-hasura-cli.html)
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) (required only for local development)
- [Mapbox API](https://www.mapbox.com/api-documentation/?language=Python#introduction)

### Directory structure

The flask microservice is located in `microservices/app` directory in your Hasura project with the following structure:

```bash
.
├── Dockerfile                   # instructions to build the image
├── k8s.yaml                     # defines how the app is deployed
├── conf
│   └── gunicorn_config.py       # configuration for the web server
└── src
	├── static
    	└── css                  # contains css files for adding styles
        └── js                   # contains basic javascript files for authentication purposes
    ├── templates 
    	└── html files           # contains static html files compiled with Jinja2 template
    ├── config.py                # some utilities to configure URLs etc               
    ├── __init__.py              # main Flask app is defined here
    ├── requirements.txt         # python dependency requirements
    └── server.py                # main Flask server code
```

## Local development

With Hasura's easy and fast git-push-to-deploy feature, you hardly need to run your code locally.
However, you can follow the steps below in case you have to run the code in your local machine.

### Without Docker

It is recommended to use a [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for Python when you are running locally.
Don't forget to add these directories to `.gitignore` to avoid committing packages to source code repo.

```bash
# setup pipenv or virtualenv and activate it (see link above)

# go to app directory
$ cd microservices/app

# install dependencies
$ pip install -r src/requirements.txt

# Optional: set an environment variable to run Hasura examples 
$ export CLUSTER_NAME=[your-hasura-cluster-name]

# run the development server (change bind address if it's already used)
$ gunicorn --reload --bind "0.0.0.0:8080" src:app
```

Go to [http://localhost:8080](http://localhost:8080) using your browser to see the development version on the app.
You can keep the gunicorn server running and when you edit source code and save the files, the server will be reload the new code automatically.
Once you have made required changes, you can [deploy them to Hasura cluster](#deploy).


## Microservices

Contains the microservices created by the user in the project. Each microservice has a route which is of the format

	<microservice-name>.<cluster-name>.hasura-app.io

Create a microservice

To create a microservice use the following commands:

# To list a number of templates for creating a microservice
	$ hasura microservice template-list

# To create a microservice
	$ hasura microservice create <ms-name> --template=<template-name>

# Add routes for the microservice
	$ hasura conf generate-route <ms-name> >> conf/routes.yaml
	$ hasura conf generate-remote <ms-name> >> conf/ci.yaml

To know more read the [hasura docs](https://docs.hasura.io/)

