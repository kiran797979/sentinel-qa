# 🛡️ Sentinel QA: The Autonomous Reliability Engineer

[![GitHub Stars](https://img.shields.io/github/stars/kiran797979/sentinel-qa?style=for-the-badge)](https://github.com/kiran797979/sentinel-qa/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/kiran797979/sentinel-qa?style=for-the-badge)](https://github.com/kiran797979/sentinel-qa/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![Scan Frequency](https://img.shields.io/badge/Scan%20Frequency-5%20Mins-red?style=for-the-badge)]()

> **Sentinel QA** is a production-grade, 24/7 autonomous reliability engineer. Built for the modern web, it doesn't just find bugs—it diagnoses root causes, tracks regressions, and proactively protects your entire fleet of web applications using advanced browser intelligence and AI-driven analysis.

---

## 📢 Live Ecosystem

| Component | Live URL |
| :--- | :--- |
| 📊 **Reliability Dashboard** | [https://site-sentinel-qa.preview.emergentagent.com/](https://site-sentinel-qa.preview.emergentagent.com/) |
| 🛠️ **ShopSphere (Testing Lab)** | [https://qatesting-store.preview.emergentagent.com/](https://qatesting-store.preview.emergentagent.com/) |
| 📱 **Telegram Alert Bot** | [EmergentWingmanBot](https://t.me/EmergentWingmanBot) |

---

## 📋 Table of Contents
1. [Project Vision](#-project-vision)
2. [Core Capabilities](#-core-capabilities)
3. [The Fleet Architecture](#-the-fleet-architecture)
4. [ShopSphere: The Chaos Lab](#-shopsphere-the-chaos-lab)
5. [Intelligence & Diagnosis](#-intelligence--diagnosis)
6. [Technical Implementation](#-technical-implementation)
7. [Autonomous Workflow](#-autonomous-workflow)
8. [Reliability Metrics](#-reliability-metrics)
9. [Deployment & Scaling](#-deployment--scaling)

---

## 🎯 Project Vision
In traditional software development, QA is often a reactive or scheduled process. **Sentinel QA** flips the script by introducing **Autonomous Reliability Engineering (ARE)**. By operating as a continuous, intelligent background agent, Sentinel QA ensures that critical user journeys are never broken for more than **5 minutes**. It acts as a digital immune system for your web infrastructure.

## 🚀 Core Capabilities

### 🕵️ 1. Multi-Site Autonomous Monitoring
Sentinel QA manages a 'Fleet' of websites. It currently monitors four distinct environments every 5 minutes:
- **ShopSphere**: Intentional Chaos Lab
- **Swag Labs**: E-commerce Sandbox
- **UI Playground**: Dynamic UI Testing
- **BrowserWire**: Live Production Monitoring

### 💫 2. Visual Intelligence & Flaw Analysis
Using Playwright-based browser automation, the agent doesn't just look for error codes; it analyzes the DOM and visual state. 
- **Screenshot Evidence**: Automated captures of every failed state.
- **Flaw Annotation**: Highlighting exactly *why* a visual state is considered a bug.

### 🧠 3. Long-term Regression Memory
Sentinel QA maintains a persistent state. It distinguishes between new bugs, existing issues, and resolved regressions.

### 📡 4. Proactive Multi-Channel Alerting
When a `Critical` issue is found, the agent pushes directly to **Telegram** with full context, screenshots, and diagnosis.

## 🏗️ The Fleet Architecture

1.  **Orchestrator (`main.py`)**: The heartbeat. Manages the high-frequency **5-minute cycle**.
2.  **Diagnostic Engine (`sentinel_qa_engine.py`)**: The brain. Handles browser automation and root-cause analysis.
3.  **Scheduler (`sentinel_scheduler.py`)**: The automation logic for cron-based recurring triggers.
4.  **State Manager (`src/state_manager.py`)**: The memory. Manages persistence and health scoring.

## 🔥 ShopSphere: The Chaos Lab
To prove Sentinel QA's capabilities, we built **ShopSphere**—a full-featured e-commerce site with a hidden **Chaos Control Panel** at `/admin/chaos` to demonstrate real-time failure detection.

## 🛠️ Technical Implementation

### High-Frequency Scheduling
The system uses a high-frequency `cron` cadence (`*/5 * * * *`) managed by the Emergent Cloud Scheduler. This ensures true 24/7 autonomy with a 5-minute detection window.

## 📊 Reliability Metrics
Sentinel QA calculates a **Global Reliability Score** every 5 minutes. This score is updated and visualized on the **Reliability Dashboard** to provide real-time 'Nerve Center' data.

---

*Built by **Wingman** for kiran797979 during the June 2026 Autonomous Agents Hackathon.*