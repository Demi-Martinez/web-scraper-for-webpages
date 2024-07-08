import requests
import pandas as pd

def extract_wikipedia_table(url):
    """Extracts and prints the first HTML table from a Wikipedia page."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    tables = pd.read_html(response.content)  # Extract all tables using pandas

    if tables:
        df = tables[0]  # Get the first table (modify index if needed)
        print(df)
    else:
        print("No tables found on this page.")


# Example usage:
url = "https://en.wikipedia.org/wiki/Visa_requirements_for_Uzbekistani_citizens"
extract_wikipedia_table(url)
