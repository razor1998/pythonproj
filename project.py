import sqlite3 as db
from tkinter import *

def display_all():
    conn = db.connect('company.db')
    c = conn.cursor()
    c.execute('SELECT * FROM TBL_STOCK')
    list0 = c.fetchall()
    output='Product_ID'+' '+'product_name'+' '+'qty_on_hand'+' '+'product_unit_price'+' '+'reorder_level'+'\n'
    for x in list0:
        output = output+x[0]+'     '+x[1]+'       '+str(x[2])+'      '+str(x[3])+'               '+str(x[4])+'\n'
    return output

    conn.commit()
    conn.close()


def insert():
    conn = db.connect('company.db')
    c = conn.cursor()
    c.execute('insert into TBL_STOCK(Product_ID, Product_Name, Quauntity_On_Hand, Product_Unit_Price, ReOrder_Level) VALUES(?,?,?,?,?)',(Product_ID_TF.get(),Product_Name_TF.get(),QTY_On_Hand_TF.get(),Product_Unit_Price_TF.get(),ReOrder_Level_TF.get()))
    Product_ID_TF.delete(0, END)
    Product_Name_TF.delete(0, END)
    QTY_On_Hand_TF.delete(0, END)
    Product_Unit_Price_TF.delete(0, END)
    ReOrder_Level_TF.delete(0, END)
    output='Inserted Successfully'
    query_label = Label(root, text=output)
    query_label.grid(row=6, column=0, columnspan=2)
    conn.commit()
    conn.close()


def delete():
    conn = db.connect('company.db')
    c = conn.cursor()
    c.execute('DELETE FROM TBL_STOCK WHERE Product_ID=?',(Product_ID_TF.get(),))
    Product_ID_TF.delete(0, END)
    Product_Name_TF.delete(0, END)
    QTY_On_Hand_TF.delete(0, END)
    Product_Unit_Price_TF.delete(0, END)
    ReOrder_Level_TF.delete(0, END)
    output='Deleted'
    query_label = Label(root, text=output)
    query_label.grid(row=6, column=0, columnspan=2)
    conn.commit()
    conn.close()

def update():
    conn = db.connect('company.db')
    c = conn.cursor()
    c.execute('update TBL_STOCK set Product_ID=?, Product_Name=?, Quauntity_On_Hand=?, Product_Unit_Price=?, ReOrder_Level=? WHERE Product_ID = ?',(Product_ID_TF.get(),Product_Name_TF.get(),QTY_On_Hand_TF.get(),Product_Unit_Price_TF.get(),ReOrder_Level_TF.get(),Product_ID_TF.get()))
    Product_ID_TF.delete(0, END)
    Product_Name_TF.delete(0, END)
    QTY_On_Hand_TF.delete(0, END)
    Product_Unit_Price_TF.delete(0, END)
    ReOrder_Level_TF.delete(0, END)
    output='Update Successfull'
    query_label = Label(root, text=output)
    query_label.grid(row=6, column=0, columnspan=2)
    conn.commit()
    conn.close()

def calculate_profit():
    conn = db.connect('company.db')
    c = conn.cursor()
    c.execute('SELECT SUM(Product_Unit_Price) FROM TBL_STOCK')
    list0 = c.fetchall()
    
    output='Proft is: '
    for x in list0:
        output = output+str(x[0])
    return output

    conn.commit()
    conn.close()
    return



root = Tk()

Product_ID_LBL = Label(root, text='Product ID')
Product_Name_LBL = Label(root, text='Product Name')
QTY_On_Hand_LBL = Label(root, text='Quantity on Hand')
Product_Unit_Price_LBL = Label(root, text='Product Unit Price')
ReOrder_Level_LBL = Label(root, text='ReOrder Level')

Product_ID_LBL.grid(row=0, column=0)
Product_Name_LBL.grid(row=1, column=0)
QTY_On_Hand_LBL.grid(row=2, column=0)
Product_Unit_Price_LBL.grid(row=3, column=0)
ReOrder_Level_LBL.grid(row=4, column=0)


Product_ID_TF = Entry(root)
Product_Name_TF = Entry(root)
QTY_On_Hand_TF = Entry(root)
Product_Unit_Price_TF = Entry(root)
ReOrder_Level_TF = Entry(root)

Product_ID_TF.grid(row=0, column=1)
Product_Name_TF.grid(row=1, column=1)
QTY_On_Hand_TF.grid(row=2, column=1)
Product_Unit_Price_TF.grid(row=3, column=1)
ReOrder_Level_TF.grid(row=4, column=1)


view_all_btn = Button(root, text='View all', command=lambda: text.insert(END, display_all()))
insert_btn = Button(root, text='Insert Record', command=insert)
delete_btn = Button(root, text='Delete Record', command=delete)
cal_profit_btn = Button(root, text='Calculate Profit', command=lambda: text.insert(END, calculate_profit()))
upd_btn = Button(root, text='Update Record', command=update)

view_all_btn.grid(row=5, column=1)
insert_btn.grid(row=5, column=0)
upd_btn.grid(row=5, column=2)
delete_btn.grid(row=5, column=3)
cal_profit_btn.grid(row=5, column=4)
text = Text(root, height=10, width=70)
text.grid(row=6, columnspan=5)
root.mainloop()
