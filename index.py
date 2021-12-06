from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import connection

root = Tk()
root.title("Python - Display SQLite3 Data In TreeView")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 700
height = 300
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================
def populateView():
    tree.delete(*tree.get_children())
    connection.Database()
    connection.cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = connection.cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3]))
    connection.cursor.close()
    connection.conn.close()
    

#==================================FRAME==============================================
Top = Frame(root, width=700, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Button_Group=Frame(root, width=700, height=50)
Button_Group.pack(side=TOP)
Buttons = Frame(Button_Group, width=200, height=50)
Buttons.pack(side=LEFT)
Buttons1 = Frame(Button_Group, width=500, height=50)
Buttons1.pack(side=RIGHT)
Body = Frame(root, width=700, height=300, bd=8, relief="raise")
Body.pack(side=BOTTOM)


#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=300, font=('arial', 24), text = "Python - Display SQLite3 Data In TreeView")
txt_title.pack()

#==================================BUTTONS WIDGET=====================================
btn_display = Button(Buttons, width=15, text="Display All", command=populateView)
btn_display.pack(side=LEFT)


#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = ttk.Treeview(Body, columns=("Firstname", "Lastname", "Address"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=200)
tree.pack()

#==================================INITIALIZATION=====================================

if __name__ == '__main__':
    root.mainloop()
   
