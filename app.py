from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  # 0.0.0.0 makes it run on localhost
  # debug = True so that it automatically updates anytime we change the code
