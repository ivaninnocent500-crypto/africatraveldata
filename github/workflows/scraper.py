import os
import asyncio
from supabase import create_client, Client

# Use the Env Variables from GitHub Secrets
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

async def run_scraper():
    print("Starting Scraper...")
    # Add your scraping logic here
    # Example: 
    # data = {"source": "GitHub_Action", "content": "Lion spotted near Seronera"}
    # supabase.table("crowdsourced_reports").insert(data).execute()
    print("Scraping Complete.")

if __name__ == "__main__":
    asyncio.run(run_scraper())

