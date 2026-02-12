# ARES-X File 11: Attack Pattern Analysis
import json
import os

class AresStats:
    def __init__(self, log_file="logs/stats.json"):
        self.log_file = log_file

    def record_attack(self, module, target_industry, success):
        """Logs attack data to build a predictive model."""
        data = self._load_data()
        entry = {"module": module, "industry": target_industry, "success": success}
        data.append(entry)
        with open(self.log_file, "w") as f:
            json.dump(data, f)

    def get_success_rate(self, module):
        """Calculates the industrial success percentage of a module."""
        data = self._load_data()
        module_runs = [d for d in data if d['module'] == module]
        if not module_runs: return 0
        successes = len([d for d in module_runs if d['success']])
        return round((successes / len(module_runs)) * 100, 2)

    def _load_data(self):
        if not os.path.exists(self.log_file): return []
        with open(self.log_file, "r") as f:
            return json.load(f)
