from . import db
from flask_login import UserMixin

class Authentication(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(70), nullable=False)
    employee_contact_no = db.Column(db.String(13), nullable=False, unique=True)
    employee_email = db.Column(db.String(50), nullable=False, unique=True)
    disposal = db.relationship('Disposal')
    inventory = db.relationship('Inventory')
    returns = db.relationship('Returns')
    restock = db.relationship('Restock')
    
class Medicine(db.Model):
    medicine_id = db.Column(db.Integer, primary_key=True)
    generic_name = db.Column(db.String(50), nullable=False)
    brand_name = db.Column(db.String(50), nullable=False)
    medicine_price = db.Column(db.Float, nullable=False)
    medicine_description = db.Column(db.String(1000), nullable=False)
    medicine_manufacturer = db.Column(db.String(50), nullable=False)
    medicine_sku = db.Column(db.String(30), nullable=False)
    manufacture_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    medicine_type = db.Column(db.String(30), nullable=False)
    storage = db.relationship('Storage')
    
class Storage(db.Model):
    storage_id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer, db.ForeignKey('medicine.medicine_id'), nullable=False)
    batch_id = db.Column(db.String(30), unique=True, nullable=False)
    batch_name = db.Column(db.String(30), nullable=False)
    batch_type = db.Column(db.String(30), nullable=False)
    batch_sku = db.Column(db.String(30), unique=True, nullable=False)
    disposal = db.relationship('Disposal')
    
class Disposal(db.Model):
    disposal_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    storage_id = db.Column(db.Integer, db.ForeignKey('storage.storage_id'), nullable=False)
    disposal_itemname = db.Column(db.String(50), nullable=False)
    disposed_by = db.Column(db.String(70), nullable=False)
    disposal_remarks = db.Column(db.String(100), nullable=False)
    disposal_datetime = db.Column(db.DateTime, nullable=False)
    
class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    invoice_no = db.Column(db.String(30), nullable=False, unique=True)
    inventory_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sku = db.Column(db.String(30), nullable=False, unique=True)
    received_by = db.Column(db.String(70), nullable=False)
    received_datetime = db.Column(db.DateTime, nullable=False)
    returns = db.relationship('Returns')
    restock = db.relationship('Restock')
    
class Supplier(db.Model):
    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(50), nullable=False)
    supplier_contact = db.Column(db.String(13), nullable=False, unique=True)
    supplier_email = db.Column(db.String(50), nullable=False, unique=True)
    returns = db.relationship('Returns')
    restock = db.relationship('Restock')

class Returns(db.Model):
    return_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.inventory_id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'), nullable=False)
    return_suppliername = db.Column(db.String(50), nullable=False)
    return_itemname = db.Column(db.String(50), nullable=False)
    returned_by = db.Column(db.String(70), nullable=False)
    return_quantity = db.Column(db.Integer, nullable=False)
    return_remarks = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    date_updated = db.Column(db.Date, nullable=False)
    
class Restock(db.Model):
    restock_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.employee_id'), nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.inventory_id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'), nullable=False)
    restock_suppliername = db.Column(db.String(50), nullable=False)
    restock_itemname = db.Column(db.String(50), nullable=False)
    restocked_by = db.Column(db.String(70), nullable=False)
    restock_quantity = db.Column(db.Integer, nullable=False)
    restock_date = db.Column(db.Date, nullable=False)