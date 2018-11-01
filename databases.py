from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,quantity,description):
    product_object = Product(
        name=name,
        price=price,
        quantity=quantity,
        description=description)
    session.add(product_object)
    session.commit()


def update_product(name,price,quantity):
  #TODO: complete the functions (you will need to change the function's inputs)
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	if(price>300):
		print("error price is too high")
	else:
		product_object.price = price
	product_object.quantity = quantity
	session.commit()




def delete_product(their_name):
	session.query(Product).filter_by(
       name=their_name).delete()
	session.commit()

def get_product(id):
  pass
