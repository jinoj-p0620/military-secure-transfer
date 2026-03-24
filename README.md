# 🛡️ Secure Military File Transfer System (Django)

## 📌 Overview

This project is a **secure file transfer system** designed for military-grade communication using advanced cryptographic techniques.

It ensures **confidentiality, integrity, and stealth** by combining:

* 🧬 DNA Encoding
* 🔳 Visual Cryptography
* 🖼️ Image Steganography

---

## 🔐 Key Features

* 📤 Secure file/image transmission
* 🧬 DNA-based data encoding (binary → A, C, G, T)
* 🔳 Visual cryptography (image splitting into shares)
* 🖼️ LSB steganography for hidden communication
* 📍 Geo-tagging (latitude & longitude tracking)
* 🔄 Secure decryption & reconstruction pipeline
* 👨‍✈️ Soldier-based communication system

---

## ⚙️ Working Pipeline

1️⃣ Upload carrier image + secret message/image
2️⃣ Convert secret → Binary → DNA sequence
3️⃣ Split image into 2 visual shares
4️⃣ Hide DNA data inside share using steganography
5️⃣ Store encrypted data + metadata
6️⃣ Reconstruct + decrypt on receiver side

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Image Processing:** OpenCV, Pillow
* **Data Processing:** NumPy
* **Security Techniques:**

  * DNA Encoding
  * Visual Cryptography
  * Steganography

---

## 📁 Project Structure

```
project/
│── app/
│── templates/
│── media/
│── manage.py
│── requirements.txt
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/military-secure-transfer.git
cd military-secure-transfer
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```
python manage.py runserver
```

---

## 🔗 API Endpoints

### 📤 Upload & Encrypt

* `/process_upload_view_post/`

### 🔍 View Messages

* `/view_shared_files/`

### 🔓 Decrypt Data

* `/decrypt_message_api/`
---

## 📱 Mobile Application (User Module)

The **User module** of this system is developed using **Flutter** and is provided as an APK file.

### 📥 Download APK

👉 https://drive.google.com/file/d/1PUBojOxap4mvdDPDcOl1zEoiO7IxngT2/view?usp=sharing

### 📲 Features of Mobile App

* Secure login for soldiers/users
* Upload image + secret message/image
* Real-time secure transmission
* View received encrypted files
* Decrypt hidden messages
* Location tracking (Latitude & Longitude) For geofencing

### ⚠️ Installation Steps

1. Download APK from Google Drive
2. Enable **"Install from Unknown Sources"** on your device
3. Install the APK
4. Connect to Django backend (same network/server)

---

## 🔄 Decryption Process

* Extract DNA from image
* Convert DNA → Binary → Original message
* Reconstruct original image using XOR
* Identify payload (TEXT / IMAGE)

---

## ⚠️ Notes

* Ensure `media/` directory exists
* Use PNG format for lossless processing
* LSB encoding is used on Red channel
* Supports both text and image payloads

---

## 📌 Future Enhancements

* AES encryption integration
* Blockchain-based logging
* Real-time communication
* Mobile app support

---

## 👨‍💻 Author

JINOJ P
