### app.py
### basic flask application to run a heroku pipeline

# bring in flask
from flask import Flask

# define the application
app = Flask(__name__)

# set the default route
@app.route('/')
def index():
    return 'hello heroku pipeline test-github-mdh'

# set the script to run
if __name__ == '__main__':
    app.run(debug=True)