from flask import Flask, render_template
from getCreds import mailCredentials
from main import main
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  main()
  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)