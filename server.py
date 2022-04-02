from flask import Flask, render_template
from getCreds import mailCredentials

mail, password = mailCredentials()

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print (mail, password) # Acá se va a ejecutar el script 

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)