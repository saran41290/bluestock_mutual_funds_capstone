import requests
from pathlib import Path
import pandas as pd

codes = [
    125497,
    119551,
    120503,
    118632,
    119092
]
# Set up paths relative to this script file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "data" / "raw" / "live_nav"
RAW_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

# Ensure directories exist
RAW_DATA.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

for code in codes:
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print(response.status_code)
    print(data.keys())

    nav_df = pd.DataFrame(data["data"])
    print(nav_df.head(2))
    
    nav_df.to_csv(
        f"{RAW_DATA}/{code}_live_nav.csv",
        index=False
    )
    print("done exporting")
    



