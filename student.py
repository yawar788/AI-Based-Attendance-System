from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition System')
        self.root.configure(bg='#1e1e1e')  # Dark Theme Background

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_radio1 = StringVar()

        # Title Label
        title_label = Label(self.root, text='STUDENT MANAGEMENT SYSTEM', font=('Helvetica', 25, 'bold'),
                            bg='#23272A', fg='white')
        title_label.place(x=0, y=0, width=1280, height=45)

        # Main Frame
        main_frame = Frame(self.root, bg='#2c2f33', bd=2, relief=RIDGE)
        main_frame.place(x=0, y=45, width=1280, height=670)

        # Helper function: Create a modern rounded button for subframes
        def create_modern_button(parent, text, command, row, col):
            btn_width = 150
            btn_height = 40
            radius = 10
            normal_color = "#34495e"
            hover_color = "#2c3e50"
            image = Image.new('RGBA', (btn_width, btn_height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.rounded_rectangle((0, 0, btn_width, btn_height), radius, fill=normal_color)
            button_image = ImageTk.PhotoImage(image)
            btn = Label(parent, text=text, font=('Helvetica', 12, 'bold'), fg='white', image=button_image,
                        compound='center', bg=normal_color, cursor="hand2")
            btn.image = button_image  # Keep a reference
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
            btn.bind("<Leave>", lambda e: btn.config(bg=normal_color))
            btn.bind("<Button-1>", lambda e: command())

        # ----------------------- Left Side: Student Details Form -----------------------
        left_frame = LabelFrame(main_frame, bd=2, bg='#2c2f33', relief=RIDGE,
                                text=" Student's Detail ", font=('Helvetica', 15, 'bold'), fg='white')
        left_frame.place(x=50, y=10, width=550, height=500)

        # Current Course Information Frame
        current_course_frame = LabelFrame(main_frame, bd=2, bg='#2c2f33', relief=RIDGE,
                                          text=" Current Course Information ", font=('Helvetica', 15, 'bold'), fg='white')
        current_course_frame.place(x=55, y=50, width=540, height=200)

        # Student Name
        student_name_label = Label(current_course_frame, text="Name:", font=('Helvetica', 13, 'bold'),
                                   bg='#2c2f33', fg='white')
        student_name_label.grid(row=2, column=0, padx=10, sticky=W)
        student_name_entry = ttk.Entry(current_course_frame, textvariable=self.var_std_name, width=13,
                                       font=('Helvetica', 13, 'bold'))
        student_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # CMS-ID
        studentID_label = Label(current_course_frame, text="CMS-ID:", font=('Helvetica', 13, 'bold'),
                                bg='#2c2f33', fg='white')
        studentID_label.grid(row=2, column=2, padx=10, sticky=W)
        studentID_entry = ttk.Entry(current_course_frame, textvariable=self.var_std_id, width=13,
                                    font=('Helvetica', 13, 'bold'))
        studentID_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Enrollment No
        roll_label = Label(current_course_frame, text="Enrollment No:", font=('Helvetica', 13, 'bold'),
                           bg='#2c2f33', fg='white')
        roll_label.grid(row=3, column=0, padx=10, sticky=W)
        roll_entry = ttk.Entry(current_course_frame, textvariable=self.var_roll, width=13,
                               font=('Helvetica', 13, 'bold'))
        roll_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(current_course_frame, text="Email:", font=('Helvetica', 13, 'bold'),
                            bg='#2c2f33', fg='white')
        email_label.grid(row=3, column=2, padx=10, sticky=W)
        email_entry = ttk.Entry(current_course_frame, textvariable=self.var_email, width=13,
                                font=('Helvetica', 13, 'bold'))
        email_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(current_course_frame, text="Department", font=('Helvetica', 13, 'bold'),
                                 bg='#2c2f33', fg='white')
        department_label.grid(row=0, column=0, padx=10)
        department_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=('Helvetica', 13, 'bold'),
                                        width=13, state='readonly')
        department_combo['values'] = ('Select Dept', 'Business', 'IT', 'Physical', 'Education', 'Electrical')
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=2, pady=10)

        # Course
        course_label = Label(current_course_frame, text="Course", font=('Helvetica', 13, 'bold'),
                             bg='#2c2f33', fg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=('Helvetica', 13, 'bold'),
                                    state='readonly', width=13)
        course_combo['values'] = ("Select Course", "BBA", "BSCS", "BE", "B.ed", "BS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Batch
        year_label = Label(current_course_frame, text="Batch", font=('Helvetica', 13, 'bold'),
                           bg='#2c2f33', fg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=('Helvetica', 13, 'bold'),
                                  state='readonly', width=13)
        year_combo['values'] = ("Select Year", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=('Helvetica', 13, 'bold'),
                               bg='#2c2f33', fg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=('Helvetica', 13, 'bold'),
                                      state='readonly', width=13)
        semester_combo['values'] = ("Select Semestr", '1', '2', '3', '4', '5', '6', '7', '8')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information Frame
        class_student_frame = LabelFrame(main_frame, bd=2, bg='#2c2f33', relief=RIDGE,
                                         text=" Class Student Information ", font=('Helvetica', 15, 'bold'),
                                         fg='white')
        class_student_frame.place(x=55, y=250, width=540, height=220)

        # Radio Buttons for Photo Sample
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text='Take Photo Sample', value='Yes')
        radiobtn1.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text='No Photo Sample', value='No')
        radiobtn2.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Button Frame for CRUD Operations
        btn_frame = LabelFrame(class_student_frame, bd=2, bg='#2c2f33', relief=RIDGE)
        btn_frame.place(x=-2, y=60, width=540, height=70)
        # Using modern interactive rounded buttons for subframe operations:
        self.create_modern_button(btn_frame, "Save", self.add_data, 0, 0)
        self.create_modern_button(btn_frame, "Update Student", self.update_data, 0, 1)
        self.create_modern_button(btn_frame, "Delete Student", self.delete_data, 0, 2)

        # Button Frame for Photo Operations
        btn_frame1 = LabelFrame(class_student_frame, bd=2, bg='#2c2f33', relief=RIDGE)
        btn_frame1.place(x=-2, y=130, width=540, height=70)
        self.create_modern_button(btn_frame1, "Reset", self.reset_data, 0, 0)
        self.create_modern_button(btn_frame1, "Take photo", self.generate_dataset, 0, 1)
        self.create_modern_button(btn_frame1, "Update photo", lambda: print("Update photo Clicked"), 0, 2)

        # Right Frame - Search System
        right_frame = LabelFrame(main_frame, bd=2, bg='#2c2f33', relief=RIDGE,
                                 text="Search System", font=('Helvetica', 15, 'bold'), fg='white')
        right_frame.place(x=670, y=10, width=555, height=450)
        search_frame = LabelFrame(right_frame, bd=2, bg='#2c2f33', relief=RIDGE, font=('Helvetica', 15, 'bold')) 
        search_frame.place(x=3, y=17, width=543, height=80)
        search_label = Label(search_frame, text="Search by:", font=('Helvetica', 13, 'bold'), bg='green', fg='white')
        search_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)
        search_combo = ttk.Combobox(search_frame, font=('Helvetica', 13, 'bold'), state='readonly', width=10)
        search_combo['values'] = ("Select", 'Roll_no', 'Name', 'Email')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        search_entry = ttk.Entry(search_frame, width=12, font=('Helvetica', 13, 'bold'))
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)
        search_button = Button(search_frame, text='Search', width=10, font=('Helvetica', 12, 'bold'), bg='blue', fg='white')
        search_button.grid(row=0, column=3, padx=2)
        showAll_button = Button(search_frame, text='Show all', width=10, font=('Helvetica', 12, 'bold'), bg='blue', fg='white')
        showAll_button.grid(row=0, column=4, padx=2)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg='#2c2f33', relief=RIDGE)
        table_frame.place(x=3, y=110, width=543, height=310)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=('dept', 'course', 'year', 'sem', 'id', 'name', 'email', 'photo', 'roll'),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading('dept', text='Department')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('year', text='Batch')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('id', text='CMS-ID')
        self.student_table.heading('name', text='Name')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('photo', text='PhotoSampleStatus')
        self.student_table.heading('roll', text='Enrollment No')
        self.student_table['show'] = 'headings'
        self.student_table.column('dept', width=100)
        self.student_table.column('course', width=100)
        self.student_table.column('year', width=100)
        self.student_table.column('sem', width=100)
        self.student_table.column('id', width=100)
        self.student_table.column('name', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('photo', width=150)
        self.student_table.column('roll', width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Helper function for modern, interactive rounded buttons in subframes
    def create_modern_button(self, parent, text, command, row, col):
        btn_width = 150
        btn_height = 40
        radius = 10
        normal_color = "#34495e"
        hover_color = "#2c3e50"
        image = Image.new('RGBA', (btn_width, btn_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((0, 0, btn_width, btn_height), radius, fill=normal_color)
        button_image = ImageTk.PhotoImage(image)
        btn = Label(parent, text=text, font=('Helvetica', 12, 'bold'), fg='white', image=button_image,
                    compound='center', bg=normal_color, cursor="hand2")
        btn.image = button_image  # keep reference
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=normal_color))
        btn.bind("<Button-1>", lambda e: command())

    # Database Methods
    def get_db_connection(self):
        return mysql.connector.connect(host='localhost', username='root', password='yawar3250@', database='face_recognition1')

    def add_data(self):
        if self.var_dep.get()=='Select Dept' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = self.get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_email.get(),
                    self.var_radio1.get(),
                    self.var_roll.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = self.get_db_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_email.set(data[6])
            self.var_radio1.set(data[7])
            self.var_roll.set(data[8])

    def update_data(self):
        if self.var_dep.get()=='Select Dept' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update:
                    conn = self.get_db_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, name=%s, email=%s, photosample=%s, roll_no=%s WHERE student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_email.get(),
                            self.var_radio1.get(),
                            self.var_roll.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=='':
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete:
                    conn = self.get_db_connection()
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Dept")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_email.set("")
        self.var_roll.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get()=='Select Dept' or self.var_std_name.get()=='' or self.var_std_id.get()=='':
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = self.get_db_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                my_result = my_cursor.fetchall()
                id = 0
                for i in my_result:
                    id += 1
                my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, name=%s, roll_no=%s, email=%s, photosample=%s WHERE student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()  
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontal from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.1, 4)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1  
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "Images_data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
