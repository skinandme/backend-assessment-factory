from sqlalchemy.orm import relationship

from app.extensions import db


class CustomerOrder(db.Model):
    """Customer order model."""

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))

    customer = relationship("Customer", foreign_keys=customer_id)
    address = relationship("Address", foreign_keys=address_id)


class Customer(db.Model):
    """Customer model."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    customer_orders = relationship("CustomerOrder", viewonly=True)


class Address(db.Model):
    """Address model."""

    id = db.Column(db.Integer, primary_key=True)
    line_1 = db.Column(db.String(255))
    line_2 = db.Column(db.String(255))
    postcode = db.Column(db.String(255))
    city = db.Column(db.String(255))
    country_code = db.Column(db.String(255))
