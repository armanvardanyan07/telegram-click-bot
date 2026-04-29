# Web to Telegram Button Trigger

This is a simple fullstack project that connects a web page with a Python backend and a Telegram bot. When a user clicks a button on the website, a request is sent to the backend, which then triggers a message in Telegram.

It is built for learning how frontend, backend, and external APIs work together in a real system.

---

## How it works

User opens a web page → clicks a button → JavaScript sends a request to Flask server → Python processes the request → Telegram bot sends a message to a chat.

---

## Tech stack

- Python
- Flask
- pyTelegramBotAPI (telebot)
- HTML
- JavaScript (Fetch API)

---

## Setup

Install dependencies:


pip install flask pyTelegramBotAPI


Create a Telegram bot using BotFather and get your bot token.

Get your chat ID by sending a message to your bot and retrieving it via Telegram API tools.

---

## Configuration

In `app.py` set:

- your bot token
- your chat ID

---

## Run backend


python app.py


Server runs on:


http://127.0.0.1:5000


---

## Frontend

Open `index.html` in a browser and click the button.  
Each click sends a request to the backend and triggers a Telegram message.

---

## Project structure


.
├── app.py
├── index.html
└── README.md


---

## Features

- Web button triggers backend request
- Python server handles requests
- Telegram bot sends message instantly
- Simple architecture for learning fullstack basics

---

## Limitations

- No authentication
- No CORS handling in basic version
- No database
- Works locally by default

---

## What you learn

- How frontend communicates with backend
- How REST-style requests work
- How Telegram Bot API works
- Basic fullstack architecture
- Event-driven systems

---

## Possible improvements

- Add CORS support
- Deploy backend to VPS or cloud
- Use FastAPI instead of Flask
- Add database logging
- Add multiple buttons with different actions
- Replace polling with webhooks
- Build modern frontend (React/Vue)

---

## Purpose

This project is made for learning and experimentation. It shows how a simple user action on a web page c
