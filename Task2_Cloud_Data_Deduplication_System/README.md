# Cloud Data Deduplication System

## Project Overview

The Cloud Data Deduplication System is a Flask-based web application that allows users to upload CSV files, detect duplicate records automatically, and store only unique records in a SQLite database.

The project demonstrates the use of Python, Flask, Pandas, SQLAlchemy, HTML, CSS, and SQLite.

---

## Features

- Upload CSV files
- Automatic duplicate detection
- Store unique records only
- Dashboard with statistics
- Search records
- Delete records
- Responsive user interface
- SQLite database integration

---

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- Pandas
- HTML5
- CSS3

---

## Folder Structure

```
CloudDataDeduplicationSystem/

│── app.py
│── config.py
│── requirements.txt
│── README.md

├── database/
│     app.db

├── uploads/

├── static/
│     css/
│         style.css

├── templates/
│     base.html
│     dashboard.html
│     index.html
│     login.html
│     register.html
│     upload.html
│     upload_result.html
│     records.html
```

---

## Installation

Install the required packages

```
pip install -r requirements.txt
```

Run the project

```
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Future Scope

- User Authentication
- AWS S3 Storage
- File Encryption
- Cloud Deployment
- User Roles
- Admin Dashboard

---

## Developed By

Saumya Sharma
