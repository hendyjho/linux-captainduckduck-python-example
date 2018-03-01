from flask import Flask
fapp = Flask(__name__)

@fapp.route('/')
def hello_world():
    return 'Flask Dockerized 1'

@fapp.route('/test')
def hello_worlda():
    return 'Flask Dockerized > test'


if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0', port=80)
    fapp.run(host='0.0.0.0')