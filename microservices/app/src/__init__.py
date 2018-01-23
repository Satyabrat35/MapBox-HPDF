from flask import Flask

app = Flask(__name__)

app.secret_key = '+\xaeOm\xa7D["\xff\x1b-\x83\xd7\x87\xd4\x8a\x8730\xa0\x00\x1fe\xe9'
#app.config['SESSION_TYPE'] = 'filesystem'
WTF_CSRF_ENABLED = True
# This line adds the hasura example routes form the hasura.py file.
# Delete these two lines, and delete the file to remove them from your project
#from .hasura import hasura_examples
#app.register_blueprint(hasura_examples)

from .server import *
