# 🎓 AI-Based Attendance

An **AI-Based Attendance System** that automatically marks student attendance using **face recognition technology**.  
This system eliminates manual attendance, prevents proxy attendance, and improves accuracy and efficiency.

---

## 👤 Student Information
- **Name:** Yawar Abbas    
- **Domain:** Artificial Intelligence / Computer Vision  
- **Repository:** Public  

---

## 📌 Abstract
Manual attendance systems are inefficient and prone to errors and proxy attendance.  
This project proposes an **AI-based attendance system** that uses **computer vision and machine learning** to detect and recognize faces in real time and mark attendance automatically.

The system captures facial images, trains a recognition model, and records attendance in a structured CSV file.

---

## 🎯 Objectives
- Automate attendance using face recognition
- Reduce human error and proxy attendance
- Store attendance digitally
- Provide a scalable and efficient solution for academic institutes

---

## 🚀 Features
- Real-time face detection
- Face recognition using trained classifier
- Automatic attendance marking
- CSV-based attendance storage
- Modular and clean Python code
- Easy to extend with database or GUI

---

## 🧠 Technologies Used
- **Python 3**
- **OpenCV**
- **NumPy**
- **Machine Learning**
- **Haar Cascade Classifier**
- **CSV File Handling**

---

## 🗂️ Project Structure
```text
AI-Based-Attendance-System/
│
├── main.py                         # Main execution file
├── face_recognize.py               # Face recognition logic
├── train.py                        # Model training
├── student.py                      # Student data handling
├── classifier.xml                  # Trained ML model
├── haarcascade_frontalface_default.xml
├── attendance.csv                  # Attendance record
├── README.md
├── requirement.txt
└── _archiv/
````

---

## ⚙️ System Workflow

1. Capture student face images
2. Train face recognition model
3. Detect faces using Haar Cascade
4. Recognize faces using trained classifier
5. Mark attendance automatically in CSV file

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/yawar788/AI-Based-Attendance-System.git
```

### Step 2: Navigate to Directory

```bash
cd AI-Based-Attendance-System
```

### Step 3: Install Dependencies

```bash
pip install -r requirement.txt
```

### Step 4: Run System

```bash
python main.py
```

---

## 📊 Output

* Live webcam face recognition
* Attendance stored in:

```text
attendance.csv
```

---

## 🔐 Security & Privacy

* No cloud storage
* Local data processing
* Public repository access

---

## 🔮 Future Enhancements

* GUI using Tkinter or PyQt
* MySQL database integration
* Deep learning models (CNN / FaceNet)
* Web-based dashboard
* Multi-camera support

---

## 📜 License

This project is developed for **academic and educational purposes only**.

---

````