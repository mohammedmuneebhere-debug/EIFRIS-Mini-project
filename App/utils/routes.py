# app/utils/routes.py

def recommend_routes(location, impact_zones):
    if "delhi" in location.lower():
        return ["Route A - via Ring Road", "Route B - via Yamuna Bypass"]
    elif "chennai" in location.lower():
        return ["Route C - via Marina Elevated", "Route D - via Safe Hill Rd"]
    elif "hyderabad" in location.lower():
        return ["Route C - via Banjara Hills Rd", "Route D - Jubliee Hills Rd", "Route E - via Necklace Rd"]
    elif "mumbai" in location.lower():
        return ["Route C - via Marine Drive Rd", "Route D - via Mira Rd"]
    else:
        return ["Generic Route 1", "Generic Route 2"]
