# 🛡️ Sentinel QA: The Autonomous Reliability Engineer

[![GitHub Stars](https://img.shields.io/github/stars/kiran797979/sentinel-qa?style=for-the-badge)](https://github.com/kiran797979/sentinel-qa/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/kiran797979/sentinel-qa?style=for-the-badge)](https://github.com/kiran797979/sentinel-qa/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![Scan Frequency](https://img.shields.io/badge/Scan%20Frequency-10%20Mins-blue?style=for-the-badge)]()

> **Sentinel QA** is a production-grade, 24/7 autonomous reliability engineer. Built for the modern web, it doesn't just find bugs—it diagnoses root causes, tracks regressions, and proactively protects your entire fleet of web applications using advanced browser intelligence and AI-driven analysis.

---

## 📢 Live Ecosystem

| Component | Live URL |
| :--- | :--- |
| 📊 **Reliability Dashboard** | [https://site-sentinel-qa.preview.emergentagent.com/](https://site-sentinel-qa.preview.emergentagent.com/) |
| 🛠️ **ShopSphere (Testing Lab)** | [https://qatesting-store.preview.emergentagent.com/](https://qatesting-store.preview.emergentagent.com/) |
| 🔥 **Chaos Control Panel** | [ShopSphere/admin/chaos](https://qatesting-store.preview.emergentagent.com/admin/chaos) |
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
10. [Roadmap](#-roadmap)
11. [Hackathon Presentation Guide](#-hackathon-presentation-guide)

---

## 🎯 Project Vision
In traditional software development, QA is often a reactive or scheduled process. **Sentinel QA** flips the script by introducing **Autonomous Reliability Engineering (ARE)**. By operating as a continuous, intelligent background agent, Sentinel QA ensures that critical user journeys are never broken for more than 10 minutes. It acts as a digital immune system for your web infrastructure.

## 🚀 Core Capabilities

### 🕵️ 1. Multi-Site Autonomous Monitoring
Sentinel QA is designed to manage a 'Fleet' of websites. It currently monitors three distinct environments with varying complexities:
- **Production-Style Labs**: High-traffic simulation.
- **Static Sandboxes**: Clean-room UI testing.
- **Dynamic Playgrounds**: Testing for race conditions and asynchronous UI updates.

### 💫 2. Visual Intelligence & Flaw Analysis
Using Playwright-based browser automation, the agent doesn't just look for error codes; it analyzes the DOM and visual state. 
- **Screenshot Evidence**: Automated captures of every failed state.
- **Flaw Annotation**: AI-driven descriptions of *why* a visual state is considered a bug (e.g., "Checkout button overlapping footer preventing user interaction").

### 🧠 3. Long-term Regression Memory
Sentinel QA maintains a persistent state of all discovered bugs. It can distinguish between:
- **New Bugs**: First-time detections.
- **Existing Issues**: Known defects still being tracked.
- **Regressions**: Previously resolved bugs that have returned.
- **Resolutions**: Bugs that are no longer detectable.

### 📡 4. Proactive Multi-Channel Alerting
When a `Critical` or `High` severity issue is found, the agent bypasses logs and pushes directly to **Telegram** with full context, screenshots, and diagnosis.

## 🏗️ The Fleet Architecture

Sentinel QA follows a modular, agentic architecture built for high availability:

1.  **Orchestrator (`main.py`)**: The heartbeat of the system. Manages the 10-minute cycle and fleet distribution.
2.  **Diagnostic Engine (`sentinel_qa_engine.py`)**: The brain. Handles browser automation, bug detection, and root-cause analysis.
3.  **Scheduler (`sentinel_scheduler.py`)**: The automation logic. Handles cron-based recurring triggers and on-demand 'Lively Scans'.
4.  **State Manager (`src/state_manager.py`)**: The memory. Manages JSON persistence, deduplication, and health score calculations.

## 🔥 ShopSphere: The Chaos Lab
To prove Sentinel QA's capabilities, we built **ShopSphere**—a full-featured e-commerce site with a hidden **Chaos Control Panel**.

- **The Lab**: A fully functional React-based store with Auth, Search, Cart, and Checkout.
- **The Chaos**: Developers can toggle 20+ intentional defects (e.g., broken payment APIs, hidden buttons, incorrect tax math).
- **The Purpose**: This provides a real-time playground to demonstrate how Sentinel QA detects, diagnoses, and reports live environment changes.

## 🧠 Intelligence & Diagnosis
When a test fails, Sentinel QA doesn't just report "Failed". It initiates a **Diagnostic Sequence**:
1.  **DOM Inspection**: Analyzes the element tree for visibility, overlap, or missing attributes.
2.  **Console Log Audit**: Captures JavaScript errors and 4xx/5xx network failures.
3.  **Visual Comparison**: Checks the current state against baseline screenshots.
4.  **Root Cause Suggestion**: Provides a human-readable diagnosis (e.g., "Checkout failure likely caused by 500 error on /api/v1/payment-intent endpoint").

## 🛠️ Technical Implementation

### 1. Browser Automation
Sentinel QA uses **Playwright** via the `agent-browser-wingman` skill. This allows for persistent sessions, cookie management, and high-fidelity screenshots.

### 2. State Persistence
The agent's memory is stored in a structured JSON schema:
```json
{
  "websites": [
    { "url": "...", "health_score": 85, "last_scan": "..." }
  ],
  "bugs": [
    { "id": "BUG-001", "severity": "CRITICAL", "status": "OPEN", "root_cause": "..." }
  ]
}
```

### 3. Scheduling
The system uses a high-frequency `cron` cadence (`*/10 * * * *`) managed by the Emergent Cloud Scheduler. This ensures true 24/7 autonomy without requiring a local machine to be active.

## 📊 Reliability Metrics
Sentinel QA calculates a **Global Reliability Score** using a weighted severity algorithm:
- **Critical Bugs**: -40 points
- **High Severity**: -20 points
- **Medium Severity**: -10 points
- **Low Severity**: -5 points

This score is updated every 10 minutes and visualized on the **Reliability Dashboard** to provide a real-time 'Nerve Center' for the monitored fleet.

## 🚧 Roadmap
- [ ] **GitHub Action Integration**: Automatically trigger scans on every Pull Request.
- [ ] **Slack & Discord Support**: Expand alerting to more professional messaging channels.
- [ ] **Auto-Fix Recommendations**: Use GPT-4 to generate PRs that fix the detected root cause.
- [ ] **Visual Diffing**: Pixel-perfect comparison between staging and production environments.

## 💡 Hackathon Presentation Guide

### The "Wow" Demo Flow
1.  **Show the Dashboard**: Display the live health scores and bug history.
2.  **Introduce ShopSphere**: Show the 'Chaos Lab' and explain why it's currently at a low health score.
3.  **The Live Fix**: Go to `/admin/chaos`, fix a 'Critical' bug, and show the judges the site is now working.
4.  **The Instant Trigger**: Type `Scan Now` in Telegram. Within 1 minute, show the new Telegram report marking the bug as **RESOLVED**.
5.  **The Result**: Show the Dashboard health score automatically jumping up. **Autonomy. Intelligence. Reliability.**

---

## 📄 Full Project Files
- `main.py`: The entry point for the autonomous cycle.
- `sentinel_qa_engine.py`: The browser-driving diagnostic engine.
- `sentinel_scheduler.py`: The fleet-wide scheduler logic.
- `sentinel_qa_state.json`: The live-updating state memory.
- `src/state_manager.py`: Logic for persistence and scoring.

---

*Built by **Wingman** for kiran797979 during the June 2026 Autonomous Agents Hackathon.*