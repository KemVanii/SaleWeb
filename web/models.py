from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Relationship
from web import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = Relationship("Product", backref="Category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(1000))
    category = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        cat1 = Category(name='Mobile')
        cat2 = Category(name='Tablet')

        pro = Product(name='Ipad', price=1000 * 3,
                      image='https://images.fpt.shop/unsafe/fit-in/585x390/filters:quality(5):fill(white)/fptshop.com.vn/Uploads/Originals/2022/12/6/638059309890101717_iphone-11-trang-1.jpg',
                      category=2)
        pro1 = Product(name='Ipad2', price=1000 * 4,
                       image='https://images.fpt.shop/unsafe/fit-in/585x390/filters:quality(5):fill(white)/fptshop.com.vn/Uploads/Originals/2022/12/6/638059309890101717_iphone-11-trang-1.jpg',
                       category=2)
        pro2 = Product(name='Bphone', price=1000 * 3,
                       image='https://images.fpt.shop/unsafe/fit-in/585x390/filters:quality(5):fill(white)/fptshop.com.vn/Uploads/Originals/2022/12/6/638059309890101717_iphone-11-trang-1.jpg',
                       category=1)
        pro3 = Product(name='Xiaomi', price=1000 * 10,
                       image='https://images.fpt.shop/unsafe/fit-in/585x390/filters:quality(5):fill(white)/fptshop.com.vn/Uploads/Originals/2022/12/6/638059309890101717_iphone-11-trang-1.jpg',
                       category=1)

        db.session.add_all([cat1, cat2, pro, pro1, pro2, pro3])
        db.session.commit()
