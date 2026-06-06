import json
import os
from datetime import datetime

class SentinelState:
    """
    Manages the long-term memory of Sentinel QA.
    """
    def __init__(self, state_file='sentinel_qa_state.json'):
        self.state_file = state_file
        self.state = self._load()

    def _load(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {"websites": [], "bugs": [], "history": []}

    def save_bug(self, bug_data):
        """
        Saves a new bug and prevents duplicate reporting.
        """
        # Check if bug exists in self.state['bugs']
        self.state['bugs'].append(bug_data)
        self._persist()

    def _persist(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def update_health_score(self, url, score):
        for site in self.state['websites']:
            if site['url'] == url:
                site['health_score'] = score
        self._persist()