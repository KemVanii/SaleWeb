from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from web import db, app


class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship("Product", backref="category", lazy=True)



class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        p1 = Product(name="Iphone 13", price=13000000, image="", category_id=1)
        db.session.add_all([p1])
        db.session.commit()
        # db.create_all()
