# 🛡️ Sentinel QA: The Autonomous Reliability Engineer

[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]() 
[![Scan Frequency](https://img.shields.io/badge/Scan%20Frequency-10%20Mins-blue)]() 
[![Tech](https://img.shields.io/badge/Stack-Python%20%7C%20Playwright%20%7C%20Telegram-orange)]()

> **Sentinel QA** is a 24/7 autonomous quality engineer designed to protect web applications through continuous monitoring, proactive failure diagnosis, and regression tracking.

---

## 🚀 Features

- 🕵️ **Autonomous Monitoring**: Scans your entire fleet of websites every 10 minutes without human intervention.
- 💫 **Visual Intelligence**: Captures screenshots of failures and performs 'Visual Flaw Analysis' to pinpoint UI regressions.
- 📡 **Proactive Alerts**: Immediate Telegram notifications for Critical and High-severity issues with root-cause diagnosis.
- 🧠 **Long-term Memory**: Tracks bug history across sessions to identify recurring issues and calculate reliability trends.
- 📊 **Reliability Analytics**: Real-time health scoring (0-100) based on weighted severity of active bugs.
- 🔗 **On-Demand Triggers**: Respond 'Scan Now' on Telegram to trigger an instantaneous 'Lively Scan' of all assets.

## 🛠️ Tech Stack

- **Core**: Python 3.x
- **Automation**: Playwright (via Agent Browser Wingman)
- **Intelligence**: AI-powered Root Cause Diagnosis
- **Delivery**: Telegram Bot API
- **Dashboard**: React + Tailwind CSS (SaaS UI)

## 🧰 Monitoring Fleet

Sentinel QA is currently protecting:
1.  **ShopSphere (Testing Lab)**: [https://qatesting-store.preview.emergentagent.com/](https://qatesting-store.preview.emergentagent.com/)
2.  **Swag Labs (Sandbox)**: [https://www.saucedemo.com/](https://www.saucedemo.com/)
3.  **UI Testing Playground**: [http://www.uitestingplayground.com/](http://www.uitestingplayground.com/)

## 🦡 Chaos Engineering Demo

Demonstrate Sentinel's responsiveness using the **Chaos Control Panel**:
- **URL**: `/admin/chaos` on ShopSphere
- **Action**: Toggle a defect (e.g., 'Break Checkout') and watch Sentinel QA detect it, alert Telegram, and drop the Health Score in the next cycle.

## 📄 Project Structure

```bash
├── main.py                 # Core orchestrator and heartbeat
├── sentinel_qa_engine.py    # Visual intelligence and diagnosis engine
├── sentinel_scheduler.py    # Autonomous fleet scheduler
├── sentinel_qa_state.json   # Persistent memory and bug state
└── src/
    └── state_manager.py     # State persistence and scoring logic
```

---

*Built with ❤️ by Wingman for the Autonomous Agents Hackathon.*