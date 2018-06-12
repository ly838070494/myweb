from app.goods import goods


@goods.route('/')
def goods_list():
    return 'goods_list'



@goods.route('/add')
def add_goods():
    return 'add_goods'