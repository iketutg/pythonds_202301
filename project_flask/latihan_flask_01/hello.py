from flask import Flask 
from flask import render_template
from flask import request


app = Flask(__name__)

# http://127.0.0.1:5000/  or http://localhost:5000/ 
@app.route('/')
def index():
    return 'index page'

# http://127.0.0.1:5000/  or http://localhost:5000/hello 
# http://localhost:5000/hello/python
@app.route('/hello')
@app.route('/hello/<names>')
def hello(names=None):
    return render_template('hello.html', name=names)

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        return "ini adalah post"
    else:
        return "ini selain post"