from flask import Blueprint, render_template, request, redirect, flash
from .models import db, Employee, Inventory, Returns, Restock, Storage, Disposal, Medicine, Supplier
from flask_login import login_required, current_user
import datetime

views = Blueprint('views', __name__)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/employee')
@login_required
def employee():
    employees = Employee.query.all()
    return render_template("employee.html", user=current_user, employees=employees)

@views.route('/add_employee', methods=['POST'])
def add_employee():
    employee_name = request.form['employee_name']
    employee_email = request.form['employee_email']
    employee_contact_no = request.form['employee_contact_no']

    new_employee = Employee(employee_name=employee_name, employee_email=employee_email, employee_contact_no=employee_contact_no)
    db.session.add(new_employee)
    db.session.commit()

    flash('Employee added successfully!', category='success')
    return redirect('/employee')

@views.route('/edit_employee/<int:employee_id>', methods=['POST'])
def edit_employee(employee_id):
    employee = Employee.query.get(employee_id)
    
    if employee:
        employee.employee_name = request.form['employee_name']
        employee.employee_email = request.form['employee_email']
        employee.employee_contact_no = request.form['employee_contact_no']
        db.session.commit()
            
        flash('Employee updated successfully!', category='success')
        return redirect('/employee')
    else:
        flash('Employee update unsuccessful!', category='error')
        return redirect('/employee')
    
@views.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        
        flash('Employee deleted successfully!', category='success')
    else:
        flash('Employee delete unsuccessful!', category='error')
    
    return redirect('/employee')

@views.route('/inventory')
@login_required
def inventory():
    inventory_list = Inventory.query.all()
    return render_template("inventory.html", user=current_user, inventory_list=inventory_list)

@views.route('/add_inventory', methods=['POST'])
def add_inventory():
    invoice_no = request.form['invoice_no']
    inventory_name = request.form['inventory_name']
    quantity = request.form['quantity']
    sku = request.form['sku']
    received_by = request.form['received_by']
    employee_id = request.form['employee_id']
    received_date = datetime.datetime.strptime(request.form['received_date'], '%Y-%m-%d').date()
    received_time = datetime.datetime.strptime(request.form['received_time'], '%H:%M:%S').time()
    received_datetime = datetime.datetime.combine(received_date, received_time)

    new_inventory = Inventory(invoice_no=invoice_no, inventory_name=inventory_name, quantity=quantity, sku=sku, received_by=received_by, employee_id=employee_id, received_datetime=received_datetime)
    db.session.add(new_inventory)
    db.session.commit()

    flash('Inventory added successfully!', category='success')
    return redirect('/inventory')

@views.route('/edit_inventory/<int:inventory_id>', methods=['POST'])
def edit_inventory(inventory_id):
    inventory = Inventory.query.get(inventory_id)
    received_date = datetime.datetime.strptime(request.form['received_date'], '%Y-%m-%d').date()
    received_time = datetime.datetime.strptime(request.form['received_time'], '%H:%M:%S').time()
    
    if inventory:
        inventory.invoice_no = request.form['invoice_no']
        inventory.inventory_name = request.form['inventory_name']
        inventory.quantity = request.form['quantity']
        inventory.sku = request.form['sku']
        inventory.received_by = request.form['received_by']
        inventory.employee_id = request.form.get('employee_id')
        inventory.received_datetime = datetime.datetime.combine(received_date, received_time)
        db.session.commit()
            
        flash('Inventory updated successfully!', category='success')
        return redirect('/inventory')
    else:
        flash('Inventory update unsuccessful!', category='error')
        return redirect('/inventory')
    
@views.route('/delete_inventory/<int:inventory_id>', methods=['POST'])
def delete_inventory(inventory_id):
    inventory = Inventory.query.get(inventory_id)
    if inventory:
        db.session.delete(inventory)
        db.session.commit()
        
        flash('Inventory deleted successfully!', category='success')
    else:
        flash('Inventory delete unsuccessful!', category='error')
    
    return redirect('/inventory')

@views.route('/returns')
@login_required
def returns():
    returns_list = Returns.query.all()
    return render_template("returns.html", user=current_user, returns_list=returns_list)

@views.route('/add_returns', methods=['POST'])
def add_returns():
    return_suppliername = request.form['return_suppliername']
    return_itemname = request.form['return_itemname']
    return_quantity = request.form['return_quantity']
    return_remarks = request.form['return_remarks']
    returned_by = request.form['returned_by']
    employee_id = request.form['employee_id']
    inventory_id = request.form['inventory_id']
    supplier_id = request.form['supplier_id']
    date_created = datetime.datetime.strptime(request.form['date_created'], '%Y-%m-%d').date()
    date_updated = datetime.datetime.strptime(request.form['date_updated'], '%Y-%m-%d').date()

    new_returns = Returns(return_suppliername=return_suppliername, return_itemname=return_itemname, return_quantity=return_quantity, return_remarks=return_remarks, 
                              returned_by=returned_by, employee_id=employee_id, inventory_id=inventory_id, supplier_id=supplier_id, date_created=date_created, date_updated=date_updated)
    db.session.add(new_returns)
    db.session.commit()

    flash('Return added successfully!', category='success')
    return redirect('/returns')

@views.route('/edit_returns/<int:return_id>', methods=['POST'])
def edit_returns(return_id):
    returns = Returns.query.get(return_id)
    
    if inventory:
        returns.return_suppliername = request.form['return_suppliername']
        returns.return_itemname = request.form['return_itemname']
        returns.return_quantity = request.form['return_quantity']
        returns.return_remarks = request.form['return_remarks']
        returns.returned_by = request.form['returned_by']
        returns.employee_id = request.form['employee_id']
        returns.inventory_id = request.form['inventory_id']
        returns.supplier_id = request.form['supplier_id']
        returns.date_created = datetime.datetime.strptime(request.form['date_created'], '%Y-%m-%d').date()
        returns.date_updated = datetime.datetime.strptime(request.form['date_updated'], '%Y-%m-%d').date()
        db.session.commit()
            
        flash('Return updated successfully!', category='success')
        return redirect('/returns')
    else:
        flash('Return update unsuccessful!', category='error')
        return redirect('/returns')
    
@views.route('/delete_returns/<int:return_id>', methods=['POST'])
def delete_returns(return_id):
    returns = Returns.query.get(return_id)
    if returns:
        db.session.delete(returns)
        db.session.commit()
        
        flash('Return deleted successfully!', category='success')
    else:
        flash('Return delete unsuccessful!', category='error')
    
    return redirect('/returns')

@views.route('/restock')
@login_required
def restock():
    restock_list = Restock.query.all()
    return render_template("restock.html", user=current_user, restock_list=restock_list)

@views.route('/add_restock', methods=['POST'])
def add_restock():
    restock_suppliername = request.form['restock_suppliername']
    restock_itemname = request.form['restock_itemname']
    restock_quantity = request.form['restock_quantity']
    restocked_by = request.form['restocked_by']
    employee_id = request.form['employee_id']
    inventory_id = request.form['inventory_id']
    supplier_id = request.form['supplier_id']
    restock_date = datetime.datetime.strptime(request.form['restock_date'], '%Y-%m-%d').date()

    new_restock = Restock(restock_suppliername=restock_suppliername, restock_itemname=restock_itemname, restock_quantity=restock_quantity, 
                              restocked_by=restocked_by, employee_id=employee_id, inventory_id=inventory_id, supplier_id=supplier_id, restock_date=restock_date)
    db.session.add(new_restock)
    db.session.commit()

    flash('Restock added successfully!', category='success')
    return redirect('/restock')

@views.route('/edit_restock/<int:restock_id>', methods=['POST'])
def edit_restock(restock_id):
    restock = Restock.query.get(restock_id)
    
    if restock:
        restock.restock_suppliername = request.form['restock_suppliername']
        restock.restock_itemname = request.form['restock_itemname']
        restock.restock_quantity = request.form['restock_quantity']
        restock.restocked_by = request.form['restocked_by']
        restock.employee_id = request.form['employee_id']
        restock.inventory_id = request.form['inventory_id']
        restock.supplier_id = request.form['supplier_id']
        restock.restock_date = datetime.datetime.strptime(request.form['restock_date'], '%Y-%m-%d').date()
        db.session.commit()
            
        flash('Restock updated successfully!', category='success')
        return redirect('/restock')
    else:
        flash('Restock update unsuccessful!', category='error')
        return redirect('/restock')
    
@views.route('/delete_restock/<int:restock_id>', methods=['POST'])
def delete_restock(restock_id):
    restock = Restock.query.get(restock_id)
    if restock:
        db.session.delete(restock)
        db.session.commit()
        
        flash('Restock deleted successfully!', category='success')
    else:
        flash('Restock delete unsuccessful!', category='error')
    
    return redirect('/restock')

@views.route('/storage')
@login_required
def storage():
    storage_list = Storage.query.all()
    return render_template("storage.html", user=current_user, storage_list=storage_list)

@views.route('/add_storage', methods=['POST'])
def add_storage():
    medicine_id = request.form['medicine_id']
    batch_id = request.form['batch_id']
    batch_name = request.form['batch_name']
    batch_type = request.form['batch_type']
    batch_sku = request.form['batch_sku']

    new_storage = Storage(medicine_id=medicine_id, batch_id=batch_id, batch_name=batch_name, 
                              batch_type=batch_type, batch_sku=batch_sku)
    db.session.add(new_storage)
    db.session.commit()

    flash('Storage added successfully!', category='success')
    return redirect('/storage')

@views.route('/edit_storage/<int:storage_id>', methods=['POST'])
def edit_storage(storage_id):
    storage = Storage.query.get(storage_id)
    
    if storage:
        storage.medicine_id = request.form['medicine_id']
        storage.batch_id = request.form['batch_id']
        storage.batch_name = request.form['batch_name']
        storage.batch_type = request.form['batch_type']
        storage.batch_sku = request.form['batch_sku']
        db.session.commit()
            
        flash('Storage updated successfully!', category='success')
        return redirect('/storage')
    else:
        flash('Storage update unsuccessful!', category='error')
        return redirect('/storage')
    
@views.route('/delete_storage/<int:storage_id>', methods=['POST'])
def delete_storage(storage_id):
    storage = Storage.query.get(storage_id)
    if storage:
        db.session.delete(storage)
        db.session.commit()
        
        flash('Storage deleted successfully!', category='success')
    else:
        flash('Storage delete unsuccessful!', category='error')
    
    return redirect('/storage')

@views.route('/disposal')
@login_required
def disposal():
    disposal_list = Disposal.query.all()
    return render_template("disposal.html", user=current_user, disposal_list=disposal_list)

@views.route('/add_disposal', methods=['POST'])
def add_disposal():
    storage_id = request.form['storage_id']
    disposal_itemname = request.form['disposal_itemname']
    disposed_by = request.form['disposed_by']
    employee_id = request.form['employee_id']
    disposal_remarks = request.form['disposal_remarks']
    disposal_date = datetime.datetime.strptime(request.form['disposal_date'], '%Y-%m-%d').date()
    disposal_time = datetime.datetime.strptime(request.form['disposal_time'], '%H:%M:%S').time()
    disposal_datetime = datetime.datetime.combine(disposal_date, disposal_time)

    new_disposal = Disposal(storage_id=storage_id, disposal_itemname=disposal_itemname, disposed_by=disposed_by, disposal_remarks=disposal_remarks, 
                              employee_id=employee_id, disposal_datetime=disposal_datetime)
    db.session.add(new_disposal)
    db.session.commit()

    flash('Disposal added successfully!', category='success')
    return redirect('/disposal')

@views.route('/edit_disposal/<int:disposal_id>', methods=['POST'])
def edit_disposal(disposal_id):
    disposal = Disposal.query.get(disposal_id)
    disposal_date = datetime.datetime.strptime(request.form['disposal_date'], '%Y-%m-%d').date()
    disposal_time = datetime.datetime.strptime(request.form['disposal_time'], '%H:%M:%S').time()
    
    if disposal:
        disposal.storage_id = request.form['storage_id']
        disposal.disposal_itemname = request.form['disposal_itemname']
        disposal.disposed_by = request.form['disposed_by']
        disposal.employee_id = request.form['employee_id']
        disposal.disposal_remarks = request.form['disposal_remarks']
        disposal.disposal_datetime = datetime.datetime.combine(disposal_date, disposal_time)
        db.session.commit()
            
        flash('Disposal updated successfully!', category='success')
        return redirect('/disposal')
    else:
        flash('Disposal update unsuccessful!', category='error')
        return redirect('/disposal')
    
@views.route('/delete_disposal/<int:disposal_id>', methods=['POST'])
def delete_disposal(disposal_id):
    disposal = Disposal.query.get(disposal_id)
    if disposal:
        db.session.delete(disposal)
        db.session.commit()
        
        flash('Disposal deleted successfully!', category='success')
    else:
        flash('Disposal delete unsuccessful!', category='error')
    
    return redirect('/disposal')

@views.route('/medicine')
@login_required
def medicine():
    medicine_list = Medicine.query.all()
    return render_template("medicine.html", user=current_user, medicine_list=medicine_list)

@views.route('/add_medicine', methods=['POST'])
def add_medicine():
    generic_name = request.form['generic_name']
    brand_name = request.form['brand_name']
    medicine_price = request.form['medicine_price']
    medicine_description = request.form['medicine_description']
    medicine_manufacturer = request.form['medicine_manufacturer']
    medicine_sku = request.form['medicine_sku']
    medicine_type = request.form['medicine_type']
    manufacture_date = datetime.datetime.strptime(request.form['manufacture_date'], '%Y-%m-%d').date()
    expiration_date = datetime.datetime.strptime(request.form['expiration_date'], '%Y-%m-%d').date()

    new_medicine = Medicine(generic_name=generic_name, brand_name=brand_name, medicine_price=medicine_price, medicine_description=medicine_description, medicine_manufacturer=medicine_manufacturer, 
                          medicine_sku=medicine_sku, medicine_type=medicine_type, manufacture_date=manufacture_date, expiration_date=expiration_date)
    db.session.add(new_medicine)
    db.session.commit()

    flash('Medicine added successfully!', category='success')
    return redirect('/medicine')

@views.route('/edit_medicine/<int:medicine_id>', methods=['POST'])
def edit_medicine(medicine_id):
    medicine = Medicine.query.get(medicine_id)
    
    if medicine:
        medicine.generic_name = request.form['generic_name']
        medicine.brand_name = request.form['brand_name']
        medicine.medicine_price = request.form['medicine_price']
        medicine.medicine_description = request.form['medicine_description']
        medicine.medicine_manufacturer = request.form['medicine_manufacturer']
        medicine.medicine_sku = request.form['medicine_sku']
        medicine.medicine_type = request.form['medicine_type']
        medicine.manufacture_date = datetime.datetime.strptime(request.form['manufacture_date'], '%Y-%m-%d').date()
        medicine.expiration_date = datetime.datetime.strptime(request.form['expiration_date'], '%Y-%m-%d').date()
        db.session.commit()
            
        flash('Medicine updated successfully!', category='success')
        return redirect('/medicine')
    else:
        flash('Medicine update unsuccessful!', category='error')
        return redirect('/medicine')
    
@views.route('/delete_medicine/<int:medicine_id>', methods=['POST'])
def delete_medicine(medicine_id):
    medicine = Medicine.query.get(medicine_id)
    if medicine:
        db.session.delete(medicine)
        db.session.commit()
        
        flash('Medicine deleted successfully!', category='success')
    else:
        flash('Medicine delete unsuccessful!', category='error')
    
    return redirect('/medicine')

@views.route('/suppliers')
@login_required
def suppliers():
    supplier_list = Supplier.query.all()
    return render_template("suppliers.html", user=current_user, supplier_list=supplier_list)

@views.route('/add_supplier', methods=['POST'])
def add_supplier():
    supplier_name = request.form['supplier_name']
    supplier_email = request.form['supplier_email']
    supplier_contact = request.form['supplier_contact']

    new_supplier = Supplier(supplier_name=supplier_name, supplier_email=supplier_email, supplier_contact=supplier_contact)
    db.session.add(new_supplier)
    db.session.commit()

    flash('Supplier added successfully!', category='success')
    return redirect('/suppliers')

@views.route('/edit_supplier/<int:supplier_id>', methods=['POST'])
def edit_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    
    if supplier:
        supplier.supplier_name = request.form['supplier_name']
        supplier.supplier_email = request.form['supplier_email']
        supplier.supplier_contact = request.form['supplier_contact']
        db.session.commit()
            
        flash('Supplier updated successfully!', category='success')
        return redirect('/suppliers')
    else:
        flash('Supplier update unsuccessful!', category='error')
        return redirect('/suppliers')
    
@views.route('/delete_supplier/<int:supplier_id>', methods=['POST'])
def delete_supplier(supplier_id):
    supplier = Supplier.query.get(supplier_id)
    if supplier:
        db.session.delete(supplier)
        db.session.commit()
        
        flash('Supplier deleted successfully!', category='success')
    else:
        flash('Supplier delete unsuccessful!', category='error')
    
    return redirect('/suppliers')