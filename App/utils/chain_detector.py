# app/utils/chain_detector.py

import json
from datetime import timedelta

def load_chain_rules(json_path):
    with open(json_path, "r") as f:
        return json.load(f)

def detect_disaster_chain(event_log, chain_rules):
    # Loop through primary events and generate alerts
    alerts = []
    for idx, row in event_log.iterrows():
        primary = row["Disaster_Type"]
        if primary in chain_rules:
            next_disaster = chain_rules[primary]["next"]
            delay = chain_rules[primary]["max_delay_hrs"]
            alerts.append(
                f"⚠️ Likely {next_disaster} after {primary} in {row['Location']} within {delay} hrs"
            )
    return alerts
