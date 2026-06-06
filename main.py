import sys
import time
from src.state_manager import SentinelState
from sentinel_qa_engine import SentinelQAEngine
from sentinel_scheduler import SentinelScheduler

FLEET_URLS = [
    "https://qatesting-store.preview.emergentagent.com/",
    "https://www.saucedemo.com/",
    "http://www.uitestingplayground.com/",
    "https://browserwire.io/"
]

def main():
    print("🛡️ Sentinel QA: Autonomous Reliability Engineer Starting...")
    state = SentinelState()
    engine = SentinelQAEngine()
    scheduler = SentinelScheduler(cron_expression='*/5 * * * *') # High-frequency 5-min cadence

    while True:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting fleet-wide reliability audit...")
        for url in FLEET_URLS:
            results = engine.run_scan(url)
        
        next_run = scheduler.get_next_run()
        print(f"Audit complete. Next autonomous run at: {next_run}")
        time.sleep(300) # Sleep for 5 minutes

if __name__ == '__main__':
    main()