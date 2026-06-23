import requests
import pandas as pd
import os

# Create output folder
os.makedirs("data/raw/live_nav", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, amfi_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_data = pd.DataFrame(data["data"])

        file_path = f"data/raw/live_nav/{scheme_name}.csv"

        nav_data.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:

        print(f"Failed to fetch {scheme_name}") 