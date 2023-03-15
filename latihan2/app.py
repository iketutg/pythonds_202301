
from flask import Flask  
app = Flask(__name__) 
##from markupsafe import escape # 3 

## 2
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()