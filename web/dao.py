from models import Category,Product


def get_categories():
    return Category.query.all()


def get_products(kw):
    pro = Product.query
    if kw:
        pro = pro.filter(Product.name.contains(kw))

    return pro.all()
