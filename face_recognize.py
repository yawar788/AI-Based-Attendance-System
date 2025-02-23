from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import logging
import csv
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Face_recognize():
    def __init__(self,root):
        self.root=root
        self.root.geometry('650x600+0+0')
        self.root.title('Face Recognition System')

        title_lbl=Label(self.root,text='FACE RECOGNITION',font=('times new roman',20,'bold'),bg='silver',fg='black')
        title_lbl.place(x=-90,y=0,width=790,height=80)

        # Button
        b1_1=Button(self.root,text='Face Recognizer',cursor='hand2',command=self.face_recog,font=('times new roman',15,'bold'),bg='black',fg='white')
        b1_1.place(x=230,y=300,width=200,height=45)

    # attendance


# attendance
    def attendance(self, i, n, r, d):
        file_path = "attendance.csv"
        file_exists = os.path.isfile(file_path)

        with open(file_path, "a+", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                # Write the header if the file does not exist
                writer.writerow(["ID", "Name", "Roll No", "Department", "Time", "Date", "Status"])

            f.seek(0)
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip().split(",")
                name_list.append(entry[0])

            # Check if the entry already exists
            if str(i) not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                writer.writerow([i, n, r, d, dtString, d1, "Present"])

    # face recognizer
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            logging.info(f"Detected {len(features)} faces")

            coords = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                conf_level = int(100 * (1 - pred / 300))
                logging.info(f"Prediction: ID={id}, Confidence={conf_level}")

                conn = mysql.connector.connect(host='localhost', user='root', password='yawar3250@', database='face_recognition1')
                my_cursor = conn.cursor()

                try:
                    my_cursor.execute("select name from student where student_id=%s", (id,))
                    n = my_cursor.fetchone()
                    logging.info(f"Name fetched from database: {n}")
                    if n:
                        n = "+".join(n)
                    else:
                        n = "Unknown"

                    my_cursor.execute("select roll_no from student where student_id=%s", (id,))
                    r = my_cursor.fetchone()
                    logging.info(f"Roll No fetched from database: {r}")
                    if r:
                        r = "+".join(r)
                    else:
                        r = "Unknown"

                    my_cursor.execute("select dep from student where student_id=%s", (id,))
                    d = my_cursor.fetchone()
                    logging.info(f"Department fetched from database: {d}")
                    if d:
                        d = "+".join(d)
                    else:
                        d = "Unknown"
                except mysql.connector.Error as err:
                    logging.error(f"Error fetching data from database: {err}")
                    n = r = d = "Unknown"

                if conf_level > 50:  # Lowered confidence threshold
                    cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No:{r}", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    self.attendance(id, n, r, d)  # Call attendance function
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

                coords = [x, y, w, h]
            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 225, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                logging.error("Failed to capture image from camera")
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognize(root)
    root.mainloop()