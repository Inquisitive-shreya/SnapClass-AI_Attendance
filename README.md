# 🎓 SnapClass – Smart Classroom Attendance System

SnapClass is an AI-powered smart classroom system that automates student attendance using face recognition and voice recognition. It helps reduce manual attendance work, avoids proxy attendance, and provides a simple portal for both teachers and students.

---

## 🚀 Features

- 📸 Face recognition and voice recognition based attendance
- 👩‍🏫 Teacher dashboard
- 👨‍🎓 Student portal
- 🔐 Student registration and login
- 📚 Subject creation and management
- 🔗 Course joining using unique join code
- 📝 Automatic attendance marking
- ☁️ Supabase database integration
- 🌐 Streamlit-based web app

---

## 🧠 Tech Stack

- Python
- Streamlit
- Supabase
- Face Recognition
- voice Recognition
- Pandas
---

## 📂 Folder Structure

```bash
SnapClass/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── components/
│   │   ├── header.py
│   │   ├── footer.py
│   │   └── dialog_add_photo.py
│   │   └── dialog_attendance_results.py
│   │   └── dialog_auto_enroll.py
│   │   └── dialog_create_subject.py
│   │   └── dialog_enroll.py
│   │   └── dialog_share_subject.py
│   │   └── dialog_voice_attendance.py
│   │   └── subject_card.py
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── teacher_screen.py
│   │   └── student_screen.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── config.py
│   ├── pipelines/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── Ui/
│   │   └── base_layout.py
│   │
│   └── utils/
│       ├── face_recognition.py
│       └── preprocessing.py
```
---

### Installation
# Clone the repository
git clone https://github.com/Inquisitive-shreya/SnapClass.git

# Navigate to project folder
cd SnapClass

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
---

## 🔑 Environment Variables

Create a `.streamlit/secrets.toml` file:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

> ⚠️ Add this file to `.gitignore`

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌍 Demo

👉 Live Demo: https://snapclasss-main.streamlit.app/

---

## 🧩 How SnapClass Works

1. Teacher logs in or registers
2. Teacher creates a subject
3. A unique join code is generated
4. Student joins using the code
5. Student registers face & voice
6. System detects student during attendance
7. Attendance is marked automatically
8. Data is stored in Supabase

---

## 📌 Future Improvements

- 🔍 Improve recognition accuracy
- 🛡️ Anti-spoofing detection
- 📊 Analytics dashboard
- 📥 Export attendance (CSV/PDF)
- 📱 Mobile app integration
- 🔔 Notifications system
