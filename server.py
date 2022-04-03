from flask import Flask, render_template
from getCreds import mailCredentials
from main import main
app = Flask(__name__)

app.add_url_rule('/photos/<path:filename>', endpoint='photos', view_func=app.send_static_file)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  status=main()
  if status==True:
    return 'Contraseña cambiada con exito'

if __name__ == '__main__':
  app.run(debug=True)