# Cloud File Storage System

## Project Overview

The **Cloud File Storage System** is a web application developed using **Python** and **Flask** that allows users to securely manage their files. The application provides features such as user registration, login, file upload, file download, file viewing, file deletion, and file type validation. User information is stored using **SQLite**, and the project is designed to be extended with cloud storage services such as **AWS S3**, **Azure Blob Storage**, or **Google Cloud Storage**.

---

## Features

- User Registration
- User Login & Logout
- Upload Files
- View Uploaded Files
- Download Files
- Delete Files
- File Type Validation
- SQLite Database Integration
- Basic Access Permissions
- Responsive Navigation Interface

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- HTML
- CSS
- SQLite

---

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
CloudFileStorageSystem/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── app.db
│
├── uploads/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── index.html
│   ├── upload.html
│   ├── files.html
│   ├── login.html
│   └── register.html
│
└── __pycache__/
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder

```bash
cd CloudFileStorageSystem
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Current Functionality

The application currently supports:

- User Registration
- User Login & Logout
- File Upload
- File Download
- File Viewing
- File Deletion
- File Type Validation
- SQLite Database for User Management
- Session-Based Authentication
- Basic Access Permissions

---

## Future Improvements

- Integrate AWS S3 for cloud file storage
- Integrate Azure Blob Storage
- Integrate Google Cloud Storage
- Generate Shareable Download Links
- Encrypt User Passwords
- Improve User Interface and User Experience
- Store file information in the database
- Add user profile management

---

## Author

**Saumya Sharma**

