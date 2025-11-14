# app/utils/forecast.py

def forecast_disaster(location):
    # Replace this logic with actual ML model or dynamic lookup
    if "chennai" in location.lower():
        return {
            "type": "Flood",
            "severity": "High",
            "impact_zones": ["Zone A", "Zone C"]
        }
    elif "delhi" in location.lower():
        return {
            "type": "Heatwave",
            "severity": "Medium",
            "impact_zones": ["Zone D"]
        }
    elif "mumbai" in location.lower():
        return {
            "type": "Urban Flood",
            "severity": "Severe",
            "impact_zones": ["Zone M", "Zone N"]
        }
    elif "hyderabad" in location.lower():
        return {
            "type": "Urban Flood",
            "severity": "Severe",
            "impact_zones": ["Zone H", "Zone D"]
        }
    else:
        return {
            "type": "Landslide",
            "severity": "Low",
            "impact_zones": ["Unknown Zone"]
        }
