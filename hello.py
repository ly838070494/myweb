from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello flask!'

@app.route('/hello')
def hi():
	return 'You are welcome.'

@app.route('/user/<username>')
def get_user(username = ''):
    if username != '':
        str = '用户名是：%s' % username
    else:
        str = '用户名为空！'
    return str

@app.route('/about')
def about():
    return 'about the website.'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('hi'))
    print(url_for('about', next='/'))
    print(url_for('get_user', username='jack ma'))


if __name__ == '__main__':
    # app.run(host='0.0.0.0') host参数允许局域网其他机器访问
    app.run(debug=True)  # 调试模式
