# 🚀 Telegram Virtual Number Shop Bot

A production-ready Telegram bot for managing and selling virtual numbers with a clean admin workflow, MongoDB backend, and scalable architecture.

---

## 👨‍💻 Developer

**Coded by Arsh**

* GitHub: https://github.com/dev-trezlo
* Telegram: https://t.me/thenameisarsh_0_0
* Instagram: https://instagram.com/thenameisarsh

> © All Rights Reserved — Arsh

---

## ✨ Features

### 🧑‍💼 User Panel

* `/start` interactive menu with inline buttons:

  * 💰 Balance
  * 👤 Account Details
  * 💳 Recharge
  * 📞 Support
  * 🛒 Buy Account

* 🌍 Country-based number selection

* 📦 Stock availability check

* 💸 Balance validation before purchase

* ⚡ Smooth buying flow (quantity → confirm → deliver)

---

### 🛠️ Admin Panel

* `/addstock` command to add numbers per country
* Automatic stock management
* MongoDB-powered storage:

  * Users
  * Stock
  * Transactions

---

### ⚙️ Backend

* Async-based architecture (fast & scalable)
* MongoDB integration
* Clean modular structure
* Ready for deployment

---

## 🚨 Important Notice (Legal & Ethical Use)

This project **strictly avoids** any implementation that:

* ❌ Automatically retrieves Telegram login codes (OTP)
* ❌ Intercepts SMS or authentication data
* ❌ Generates Telegram sessions via unauthorized methods

> This bot is designed for **safe, legal, and ethical use only**.

---

## ✅ Safe & Legal Usage Options

### 1. Manual OTP Flow (Recommended)

* User purchases number
* Requests OTP manually
* Enters code on their own device

---

### 2. SMS Provider Integration (Allowed Only If Legal)

You may integrate APIs like:

* Twilio (or similar)

**Conditions:**

* You own the numbers
* You have user consent
* You follow legal guidelines

---

### 3. Session-Based Systems

* Must be implemented with **explicit user consent**
* Must follow platform policies & legal compliance

---

## 🚀 Deployment (Heroku Ready)

### 🔧 Required Environment Variables

```env
BOT_TOKEN=your_bot_token
MONGODB_URI=your_mongo_uri
ADMIN_IDS=123456789,987654321
CURRENCY_SYMBOL=₹
DEFAULT_PRICE=20
```

---

### ☁️ Deploy to Heroku

1. Fork / clone this repo
2. Set environment variables
3. Deploy via:

```
https://dashboard.heroku.com/new?template=https://github.com/username/paidotpbot
```

---

## 📦 Tech Stack

* Python (Async)
* Aiogram (Telegram Bot Framework)
* MongoDB (Database)
* Heroku (Deployment)

---

## 🔮 Future Enhancements

* 💳 Recharge system (manual / automated)
* 🌐 Admin web dashboard (Flask / FastAPI)
* 📊 Analytics & logging
* ⚡ Rate limiting & anti-abuse system
* 🔌 API for resellers

---

## 📜 License

This project is proprietary.

> Unauthorized copying, modification, or redistribution is strictly prohibited.

---

## ❤️ Support

For support or custom development:

* Telegram: https://t.me/thenameisarsh_0_0
* Instagram: https://instagram.com/thenameisarsh

---

> Built with focus, scaled with vision 🚀
