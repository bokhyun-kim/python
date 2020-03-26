from flask import Flask #flask 호출

app = Flask(__name__)

@app.route('/') #기본 route 설정 '/'는 로컬호스트를 의미
def default():
    return 'default page'

@app.route('/helloworld')
def hello():
    return 'hello world'

if __name__=='__main__':
    app.run(host='0.0.0.0')
