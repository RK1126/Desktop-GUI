import mysql.connector

from tkinter import *
from tkinter import ttk


cnx = mysql.connector.connect(host='localhost', user='root', password='fuckthebitch', database='project')
#  ..separate cursor for every function
# decoration baad me


def popup_box(msg):
    window = Tk()
    window.title('Message')
    label = Label(window, text=msg)
    label.pack()
    button = ttk.Button(window, text='Okay', command=window.destroy)
    button.pack()
    window.mainloop()


def ret_string(x):
    return str(x)


def db_student(db_id):
    cursor_stu = cnx.cursor(buffered=True)
    query_1 = ("select * from login where name = %s")
    cursor_stu.execute(query_1,(db_id,))#......id input should be as string
    i =[]
    for name in cursor_stu:
        i = name
    cursor_stu.close()
    return i       # return a list


def stu_output(name,password):
    new_window = Toplevel(background='green')

    new_window.title('Your details')
    #  create database for detials
    query = ("select roll_number from login where name = %s and password = %s")
    cursor_out = cnx.cursor(buffered =True)
    cursor_out.execute(query,(name,password)) # return roll number
    i =[]
    for roll_number in cursor_out:
        i = roll_number
    # load marks on top level screen
    # use frames and labels to disply output on popup windows
    stu_details = Frame(new_window, height=250)
    stu_details.pack(fill=X, side=TOP)
    stu_name = Label(stu_details, text=name.upper(), fg='red')
    stu_name.config(font=Label_font2)
    stu_name.place(x=600, y=100, anchor=CENTER)
    query_2 = ("select * from marks where roll_number  = %s")
    cursor_out.execute(query_2, (i[0],))  # ..... possible error
    j = []
    for d in cursor_out:  # person marks in a list  ..
        j = d
    stu_result = Frame(new_window, height=500)
    stu_result.pack(fill=X, side=BOTTOM)

    title_for = Label(stu_result,text='\n\n\nSubject\t\t\t\t\tMarks', fg='red')
    title_for.config(font=Label_font3)
    title_for.place(x=600, y=50, anchor=CENTER)

    h = 150
    j = list(map(ret_string, j))

    for sub, mark in zip(['Maths\t', 'Physics\t', 'English\t', 'Chemistry', 'Snskrit\t'], j):
        display_marks = Label(stu_result, text=sub+'\t\t\t\t'+mark, fg='blue')
        display_marks.config(font=Label_font3)
        display_marks.place(x=600, y=h, anchor=CENTER)
        h = h + 50

    cursor_out.close()
    new_window.mainloop()


def func():
    print('rk create function for me')


def fun_student(id, password):  # pass lower case of id and in called function
    #  change id in lower case
    id_lower = id.lower()
    query_output = db_student(id)
    if query_output:
        query_out_name = query_output[1].lower()
        if id_lower == query_out_name:
            if password == query_output[2]:
                stu_output(id, password)
            else:
                popup_box('Enter a valid Password')

    else:
        popup_box('Enter valid information')

#  ...................................no function should be below this..................................................


window = Tk()
window.config(bg='yellow')
window.title("Enquiry Box")
Label_font1 = ('times', 40, 'bold')  # ... for school name
Label_font2 = ('times', 20, 'bold')  # .....for medium size use
Label_font3 = ('times', 15, 'bold')  # .....for portal's name
School_name = Label(window, text="A.V.M. SCHOOL", fg='green')
Login_portal = Label(window, text='Login Portal', fg='maroon4')

School_name.pack(fill=X)
School_name.config(font=Label_font1, height=2)
Login_portal.config(font=Label_font2, height=4)
Login_portal.pack(fill=X)

#  *********************student box************************************************************************************

student_box = Frame(window, height=250, width=400, bg='green')
student_box.pack(side=LEFT)

portal_1_name = Label(student_box, text="Student Portal", fg='dark orchid', bg='black')
portal_1_name.config(font=Label_font3)
portal_1_name.place(x=100, y=20, anchor=W)

student_name = Label(student_box, text='Name', bg='LightGoldenrod1')
student_name.config(font=Label_font3)
student_name.place(x=65, y=100, anchor=S)

student_pass = Label(student_box, text='Password', bg='orchid4')
student_pass.config(font=Label_font3)
student_pass.place(x=50, y=130, anchor=S)

student_name_entry = Entry(student_box)
student_name_entry.place(x=100, y=85, anchor=W)

student_pass_entry = Entry(student_box)
student_pass_entry.place(x=100, y=115, anchor=W)

student_box_button = Button(student_box, text='Login', fg='blue', bg='yellow', command=lambda: fun_student(
                                                                    student_name_entry.get(), student_pass_entry.get()))
student_box_button.place(x=75, y=200)

#  ***********************other box************************************************************************************
other_box = Frame(window, height=250, width=400, bg='red')
other_box.pack(side=RIGHT)

portal_2_name = Label(other_box, text="Others", fg='gold4', bg='black')
portal_2_name.config(font=Label_font3)
portal_2_name.place(x=120, y=20, anchor=W)

other_id = Label(other_box, text='ID', bg='LightGoldenrod1')
other_id.config(font=Label_font3)
other_id.place(x=78, y=100, anchor=S)

other_pass = Label(other_box, text='Password', bg='orchid4')
other_pass.config(font=Label_font3)
other_pass.place(x=50, y=130, anchor=S)


other_id_entry = Entry(other_box)
other_id_entry.place(x=100, y=85, anchor=W)

other_pass_entry = Entry(other_box)
other_pass_entry.place(x=100, y=115, anchor=W)

other_box_button = Button(other_box, text='Login', fg='blue', bg='yellow', command=func)
other_box_button.place(x=75, y=200)

#  frame for future purpose.************************************************************************************

future_box = Frame(window, height=250, width=600, bg='blue')
future_box.pack(side=RIGHT)

window.mainloop()


cnx.close()
