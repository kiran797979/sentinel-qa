# Sentinel QA: Autonomous Reliability Engineer

This repository contains the core logic and state for Sentinel QA, an autonomous 24/7 reliability engineer.

## Project Overview
Sentinel QA is designed to protect web applications through continuous autonomous testing, failure diagnosis, and regression tracking.

### Key Features
- **Autonomous Scheduling**: Runs on a high-frequency recurring cadence.
- **Browser Intelligence**: Uses Playwright-based automation to navigate complex user journeys.
- **Failure Diagnosis**: Analyzes root causes and suggests potential fixes.
- **Long-term Memory**: Remembers historical bugs and tracks stability trends over time.
- **Proactive Alerts**: Pushes critical and high-severity findings immediately to Telegram.

## Current Status: Monitoring ShopSphere
Sentinel QA is currently monitoring [ShopSphere](https://qatesting-store.preview.emergentagent.com/), an e-commerce testing lab with intentionally engineered defects.

### Latest Stats
- **Active Bugs**: 7
- **Health Score**: 0/100 (due to active Chaos defects)
- **Monitoring Cadence**: Every 10 minutes