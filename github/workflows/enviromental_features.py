import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def process_environmental_data():
    print("Processing Environmental Features...")
    # This is where you call your ML models or NDVI logic
    # habitat_score = calculate_ndvi(-2.4, 34.8)
    print("Processing Complete.")

if __name__ == "__main__":
    process_environmental_data()

