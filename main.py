from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import os
from student import Student
from train import Train_data
from face_recognize import Face_recognize

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x720+0+0')
        self.root.title('Face Recognition System')
        self.root.configure(bg='#1e1e1e')  # Dark Theme Background

        # Styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', font=('Helvetica', 24, 'bold'), background='#1e1e1e', foreground='white')

        # Title Label
        title_label = ttk.Label(self.root, text='FACE RECOGNITION SYSTEM', anchor='center', style='TLabel')
        title_label.pack(side=TOP, fill=X, pady=10)

        # Main Frame
        main_frame = Frame(self.root, bg='#2c2c2c', bd=2, relief=RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=900, height=500)

        # Button Config
        button_width, button_height, radius = 200, 100, 25
        button_spacing_x, button_spacing_y = 40, 40

        # Optimized Button Colors
        button_colors = {
            "Student Details": ("#34495e", "#2c3e50"),
            "Face Detector": ("#e74c3c", "#c0392b"),
            "Attendance": ("#27ae60", "#229954"),
            "Train Data": ("#f39c12", "#e67e22"),
            "Photos": ("#2980b9", "#1f618d"),
            "Developer": ("#8e44ad", "#732d91")
        }

        # Function to create modern rounded buttons
        def create_rounded_button(text, command, row, col):
            normal_color, hover_color = button_colors[text]
            image = Image.new('RGBA', (button_width, button_height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.rounded_rectangle((0, 0, button_width, button_height), radius, fill=normal_color)
            button_image = ImageTk.PhotoImage(image)

            btn = Label(main_frame, text=text, font=('Helvetica', 16, 'bold'), fg='white', image=button_image,
                        compound='center', bg=normal_color, cursor="hand2")
            btn.image = button_image
            btn.grid(row=row, column=col, padx=button_spacing_x, pady=button_spacing_y, sticky="nsew")

            # Hover Effect
            def on_enter(e): btn.config(bg=hover_color)
            def on_leave(e): btn.config(bg=normal_color)

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            btn.bind("<Button-1>", lambda e: command())

        # Buttons
        create_rounded_button("Student Details", self.student_detail, 0, 0)
        create_rounded_button("Face Detector", self.face_data, 0, 1)
        create_rounded_button("Attendance", lambda: print("Attendance Clicked"), 0, 2)
        create_rounded_button("Train Data", self.train_data, 1, 0)
        create_rounded_button("Photos", self.open_img, 1, 1)
        create_rounded_button("Developer", lambda: print("Developer Clicked"), 1, 2)

        # Adjust Grid Layout
        for i in range(2):
            main_frame.rowconfigure(i, weight=1)
        for j in range(3):
            main_frame.columnconfigure(j, weight=1)

        # Footer Frame (Ensures Proper Placement)
        footer_frame = Frame(self.root, bg='#1e1e1e')
        footer_frame.pack(side=BOTTOM, fill=X, pady=5)

        # Footer Label (Fixed Visibility + Red Heart ❤️)
        footer_label = Label(footer_frame, text="Made with ", font=('Helvetica', 12, 'bold'),
                             fg='white', bg='#1e1e1e', anchor='w')
        footer_label.pack(side=LEFT, padx=10)

        heart_label = Label(footer_frame, text="❤️", font=('Helvetica', 12, 'bold'), fg='red', bg='#1e1e1e')
        heart_label.pack(side=LEFT)

        location_label = Label(footer_frame, text=" in Sukkur", font=('Helvetica', 12, 'bold'),
                               fg='white', bg='#1e1e1e')
        location_label.pack(side=LEFT)

    # Open Image Folder
    def open_img(self):
        os.startfile("C:\\Users\\Lenovo\\Desktop\\face_recognization\\Images_data")

    # Student Details
    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # Train Data
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_data(self.new_window)

    # Face Recognition
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognize(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
