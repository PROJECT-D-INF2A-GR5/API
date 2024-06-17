from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)
    deleted_on = Column(DateTime)

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)
    deleted_on = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    role = Column(String)
    content = Column(String)

class ProductList(Base):
    __tablename__ = 'product_lists'

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)
    deleted_on = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='product_lists')
    products = relationship('Product', backref='product_list')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)
    deleted_on = Column(DateTime)
    product_list_id = Column(Integer, ForeignKey('product_lists.id'))
    product_type = Column(String)
    product_id = Column(String)

class KitchenTop(Base):
    __tablename__ = 'kitchen_tops'

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)
    deleted_on = Column(DateTime)
    material = Column(String)
    back_splash = Column(Integer)
    window_sill = Column(Integer)
    drill_holes = Column(Integer)
    wall_socket_possibility = Column(Boolean)
    edge_finishing_possibility = Column(Boolean)
    price_per_square = Column(Numeric)
    edge_finishing_price_per_meter = Column(Numeric)
    back_splash_price_per_meter = Column(Numeric)
    window_sill_price_per_meter = Column(Numeric)
    under_mount_sink_cutout = Column(Numeric)
    inset_cutout = Column(Numeric)
    rough_cutout = Column(Numeric)
    faucet_hole = Column(Numeric)
    soap_dispenser = Column(Numeric)
    drill_holes_per_piece = Column(Numeric)
    wall_socket_price_per_piece = Column(Numeric)
    back_panel_price_per_meter = Column(Numeric)
    back_panel_edge_finishing_price_per_meter = Column(Numeric)