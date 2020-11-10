from flask import Flask

app = Flask(__name__)

@app.route('/<int:userif')
def hello(userid):
    return 'hello word id = {}'.fprmat(userid)

@app.route('/test1')
def test():
    return "test!"
 
    if __name__ == '__main__':
        app.debug - True
        app.run("127.0.0.1",port=8000)