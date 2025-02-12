import requests
import json
import os
from collections import defaultdict

# Load state and territory codes
STATE_CODES_FILE = "states_territories.txt"
API_URL = "https://api.covidtracking.com/v1/states/{}/daily.json"
OUTPUT_FOLDER = "Covid confirmed cases statistics"

def load_state_codes():
    """Load states from text file."""
    with open(STATE_CODES_FILE, "r") as file:
        return [line.strip().lower() for line in file.readlines()]

def fetch_covid_data(state_code):
    """Fetch COVID-19 data for a given state."""
    url = API_URL.format(state_code)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def save_json_data(state_code, data):
    """Save JSON data to a file."""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    file_path = os.path.join(OUTPUT_FOLDER, f"{state_code}.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def analyze_covid_data(state_code, data):
    """Perform analysis on the COVID-19 data."""
    if not data:
        return
    
    new_cases = []
    date_highest_cases = ""
    max_cases = 0
    
    date_no_cases = ""
    monthly_cases = defaultdict(int)
    
    for entry in data:
        date = str(entry.get("date"))
        year_month = date[:6]  # YYYYMM format
        new_case_count = entry.get("positiveIncrease", 0)
        
        new_cases.append(new_case_count)
        monthly_cases[year_month] += new_case_count
        
        if new_case_count > max_cases:
            max_cases = new_case_count
            date_highest_cases = date
        
        if new_case_count == 0:
            date_no_cases = date
    
    avg_new_cases = sum(new_cases) / len(new_cases) if new_cases else 0
    
    highest_month = max(monthly_cases, key=monthly_cases.get)
    lowest_month = min(monthly_cases, key=monthly_cases.get)
    
    print(f"State: {state_code.upper()}")
    print(f"Average daily new cases: {avg_new_cases:.2f}")
    print(f"Date with highest cases: {date_highest_cases}")
    print(f"Most recent date with no new cases: {date_no_cases}")
    print(f"Month-Year with highest cases: {highest_month[:4]}-{highest_month[4:]}")
    print(f"Month-Year with lowest cases: {lowest_month[:4]}-{lowest_month[4:]}")
    print("-" * 40)

if __name__ == "__main__":
    state_codes = load_state_codes()
    for state_code in state_codes:
        data = fetch_covid_data(state_code)
        if data:
            save_json_data(state_code, data)
            analyze_covid_data(state_code, data)
        else:
            print(f"Failed to fetch data for {state_code.upper()}")
