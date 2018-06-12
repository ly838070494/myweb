from flask import Blueprint


goods = Blueprint('goods', __name__)

from app.goods import view