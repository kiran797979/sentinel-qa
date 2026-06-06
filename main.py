import sys
import time
from src.state_manager import SentinelState
from sentinel_qa_engine import SentinelQAEngine
from sentinel_scheduler import SentinelScheduler

FLEET_URLS = [
    "https://qatesting-store.preview.emergentagent.com/",
    "https://www.saucedemo.com/",
    "http://www.uitestingplayground.com/"
]

def main():
    print("🛡️ Sentinel QA: Autonomous Reliability Engineer Starting...")
    state = SentinelState()
    engine = SentinelQAEngine()
    scheduler = SentinelScheduler(cron_expression='*/10 * * * *')

    while True:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting fleet-wide reliability audit...")
        for url in FLEET_URLS:
            results = engine.run_scan(url)
            # AI Diagnosis and state updates happen inside engine/state
        
        next_run = scheduler.get_next_run()
        print(f"Audit complete. Next autonomous run at: {next_run}")
        
        # In production, this would be managed by a task scheduler like Celery or GitHub Actions.
        # For the demo, we maintain the 10-minute heartbeat.
        time.sleep(600) 

if __name__ == '__main__':
    main()