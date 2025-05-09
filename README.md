[![Lech Poznan Light](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo2lightmode.png#gh-light-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)
[![Lech Poznan Dark](https://github.com/Eskimek/AI-message-by-discord-user/blob/main/assets/logo1.png#gh-dark-mode-only)](https://github.com/Eskimek/AI-message-by-discord-user)

[![Node.js](https://img.shields.io/badge/Node.js-18+-green?style=for-the-badge&logo=node.js)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org/)
[![Playwright](https://img.shields.io/badge/Scraper-Playwright-purple?style=for-the-badge&logo=microsoft)](https://playwright.dev/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)](LICENSE)

## 🎫 Lech Poznań Ticket Viewer
A modern web dashboard that fetches and displays live stadium ticket availability for Lech Poznań games using reverse-engineered Roboticket API.
---
## Features
- Trybuna-wise ticket summary
- Warning on low availability
- Info when trybuna is sold out
- Percentage fill with progress bars
- Global ticket stats (free, sold, capacity)
- Clean, modern UI with responsive grid
- Automatically refreshes and saves data to JSON
- Scrapes from [bilety.lechpoznan.pl](https://bilety.lechpoznan.pl) using Playwright
- Backend ready for MongoDB + websockets sync
- Built for containerization & deployment

---

## 📦 Installation
### 1. Clone the repo or just download zip

```bash
git clone https://github.com/Eskimek/Lech-Poznan--Licznik-Biletow
cd <repo-folder>
```
### 2. Install Node.js dependencies
```bash
npm install
```
### 3. Install Python dependencies
```bash
pip install playwright
playwright install
```
---
## Run Locally
```bash
node server.js
```
Then open your browser at:
```
http://localhost:3000
```
Click **"Odśwież dane"** to scrape latest data and update the JSON.
---
## 📁 Folder Structure
```
.
├── guietc.html               # frontend
├── sektor_summary.json       # live data file
├── server.js                 # express server
├── scrape_lech_tickets.py    # scraper
├── package.json
├── .gitignore
```
---
## 📞 Contact
discord: **eskimek**
