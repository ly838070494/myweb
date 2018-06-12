from flask import Flask, redirect, url_for
from app.user import user
from app.goods import goods

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(goods, url_prefix='/goods')

@app.route('/')
def index():
    return redirect(url_for('user.get_list'))



if __name__ == '__main__':
    app.run(debug=True)
