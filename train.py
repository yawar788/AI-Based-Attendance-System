from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import os
import cv2
import numpy as np
import logging
from tkinter import messagebox

class Train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x500+100+50')
        self.root.title('Train Dataset')
        self.root.configure(bg='#1e1e1e')  # Dark Theme Background

        # Styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', font=('Helvetica', 20, 'bold'), background='#1e1e1e', foreground='white')

        # Title Label
        title_label = ttk.Label(self.root, text='TRAIN DATASET', anchor='center', style='TLabel')
        title_label.pack(side=TOP, fill=X, pady=10)

        # Main Frame
        main_frame = Frame(self.root, bg='#2c2c2c', bd=2, relief=RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=600, height=300)

        # Button Config
        button_width, button_height, radius = 200, 80, 20

        # Button Colors
        button_colors = {"Train Data": ("#e74c3c", "#c0392b")}

        # Function to create modern rounded button
        def create_rounded_button(text, command):
            normal_color, hover_color = button_colors[text]
            image = Image.new('RGBA', (button_width, button_height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.rounded_rectangle((0, 0, button_width, button_height), radius, fill=normal_color)
            button_image = ImageTk.PhotoImage(image)

            btn = Label(main_frame, text=text, font=('Helvetica', 16, 'bold'), fg='white', image=button_image,
                        compound='center', bg=normal_color, cursor="hand2")
            btn.image = button_image
            btn.place(relx=0.5, rely=0.5, anchor=CENTER)

            # Hover Effect
            def on_enter(e): btn.config(bg=hover_color)
            def on_leave(e): btn.config(bg=normal_color)

            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            btn.bind("<Button-1>", lambda e: command())

        # Button
        create_rounded_button("Train Data", self.train_classifier)

    # Train classifier
    def train_classifier(self):
        data_dir = "C:\\Users\\Lenovo\\Desktop\\face_recognization\\Images_data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # gray scale image
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training Dataset", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                logging.error(f"Error processing image {image}: {e}")

        ids = np.array(ids)

        # Train the classifier and save
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training dataset completed!!")
        except Exception as e:
            logging.error(f"Error training classifier: {e}")
            messagebox.showerror("Error", "Training dataset failed!!")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()
