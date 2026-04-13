Окей, зробимо **красивий README з бейджами (виглядає як реальний GitHub-проєкт 🔥)**

Просто заміни свій README на цей 👇

---

```markdown
# 🚀 GoIT Python Web HW3

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-completed-success)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Overview

This project is a simple web application built using Python's built-in HTTP server and Jinja2 templating engine.

The application allows users to:
- send messages via a web form
- store messages in a JSON file
- view all saved messages

---

## ✨ Features

- 📄 Routing:
  - `/` — Home page
  - `/message` — Message form
  - `/read` — View saved messages

- 📝 Form handling (POST requests)
- 💾 JSON-based data storage
- 🧠 Dynamic rendering with Jinja2
- 🎨 Static files support (CSS, images)
- ❌ Custom 404 error page
- ⚡ Runs on port **3000**

---

## 🛠️ Tech Stack

- Python 3
- Jinja2
- HTTPServer (standard library)

---

## 📂 Project Structure

```

goit-pythonweb-hw-03/
│
├── main.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── message.html
│   ├── read.html
│   └── error.html
│
├── static/
│   ├── style.css
│   └── logo.png
│
└── storage/
└── data.json

````

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yulianakosenko/goit-pythonweb-hw-03.git
cd goit-pythonweb-hw-03
````

---

## ▶️ Run the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python main.py
```

Open in browser:

```
http://localhost:3000
```

---

## 📎 Notes

* Messages are stored with timestamps using `datetime.now()`
* `data.json` is created automatically if it does not exist
* Static files are served from `/static`
* Templates are rendered via Jinja2

---

## 📸 Preview

> Home page with navigation and static assets
> Message form and stored messages rendering

---

## 👩‍💻 Author

**Yuliya Kostenko**

