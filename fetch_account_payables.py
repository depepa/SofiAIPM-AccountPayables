import requests
import json
from typing import Optional, Dict, Any


def get_account_payables(ticker: str, year: int, api_key: str) -> Optional[Dict[str, Any]]: 
    """
    Fetch and retrieve accountPayables information for a company from the API.
    
    Args:
        ticker (str): Company ticker symbol (e.g., "RELIANCE.NS")
        year (int): Fiscal year for which to fetch data (e.g., 2025)
        api_key (str): API key for authentication
    
    Returns:
        Optional[Dict[str, Any]]:  Dictionary containing the year's financial data with accountPayables,
                                  or None if data not found
    
    Raises:
        requests.exceptions.RequestException: If API request fails
        ValueError: If ticker or year is invalid
    """
    
    if not ticker or not isinstance(ticker, str):
        raise ValueError("Ticker must be a non-empty string")
    
    if not isinstance(year, int) or year < 1900 or year > 2100:
        raise ValueError("Year must be a valid integer between 1900 and 2100")
    
    if not api_key or not isinstance(api_key, str):
        raise ValueError("API key must be a non-empty string")
    
    # Construct the API URL
    url = f"https://ac-api-server.vercel.app/server/company/{ticker}"
    
    # Set up headers with API key
    headers = {
        "x-api-key": "APIKEYINSERT",
        "Content-Type":  "application/json"
    }
    
    try:
        # Make the GET request to the API
        print(f"\nFetching data for {ticker}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Check if response contains data
        if not data. get("status") == "success" or not data.get("data"):
            print(f"API Error: {data.get('status', 'Unknown error')}")
            return None
        
        # Extract the financial records
        financial_records = data.get("data", [])
        
        if not isinstance(financial_records, list):
            print("Error: Expected data to be a list of records")
            return None
        
        # Search for the record matching the specified year
        for record in financial_records:
            if record.get("calendarYear") == year:
                # Extract relevant accountPayables information
                result = {
                    "ticker": record.get("symbol"),
                    "company_name": record.get("company_name"),
                    "year": record.get("calendarYear"),
                    "period": record.get("period"),
                    "filing_date": record.get("fillingDate"),
                    "accepted_date": record.get("acceptedDate"),
                    "accountPayables": record.get("accountPayables"),
                    "currency": record. get("reportedCurrency"),
                }
                return result
        
        # If no matching year found
        print(f"No data found for year {year}")
        return None
    
    except requests.exceptions. Timeout:
        print(f"Request timed out while fetching data for {ticker}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Connection error while fetching data for {ticker}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        return None
    except json.JSONDecodeError:
        print("Error: Could not parse API response as JSON")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None


def display_account_payables(result: Dict[str, Any]) -> None:
    """
    Display the accountPayables information in a formatted manner.
    
    Args:
        result (Dict[str, Any]): Dictionary containing the financial data
    """
    if result is None:
        print("No data to display")
        return
    
    print("\n" + "="*70)
    print("ACCOUNT PAYABLES INFORMATION")
    print("="*70)
    print(f"Company:             {result['company_name']}")
    print(f"Ticker:              {result['ticker']}")
    print(f"Year:                {result['year']}")
    print(f"Period:              {result['period']}")
    print(f"Filing Date:         {result['filing_date']}")
    print(f"Currency:            {result['currency']}")
    print("-"*70)
    print(f"Account Payables:     {result['accountPayables']: ,} {result['currency']}")
    print("="*70 + "\n")


def main():
    """Main function to handle user input and fetch data."""
    import sys
    
    # API Key - replace with your actual API key
    API_KEY = "INSERT YOUR API KEY"
    
    # Check if API key has been set
    if API_KEY == "INSERT YOUR API KEY":
        print("Error: Please set your API key in the script first.")
        print("Replace 'INSERT YOUR API KEY' with your actual API key.")
        sys.exit(1)
    
    # Take input from user
    print("\n" + "="*70)
    print("COMPANY ACCOUNT PAYABLES FETCHER")
    print("="*70)
    
    # Get ticker input
    ticker = input("Enter company ticker (e.g., RELIANCE.NS): ").strip().upper()
    
    if not ticker:
        print("Error: Ticker cannot be empty")
        sys.exit(1)
    
    # Get year input
    try:
        year = int(input("Enter the year (e.g., 2025): ").strip())
    except ValueError: 
        print("Error: Year must be a valid integer")
        sys.exit(1)
    
    # Validate inputs
    try:
        # Fetch data
        result = get_account_payables(ticker, year, API_KEY)
        
        # Display result
        if result:
            display_account_payables(result)
            print(f"✓ Successfully retrieved Account Payables:  {result['accountPayables']: ,}")
        else:
            print(f"✗ Failed to retrieve data for {ticker} in year {year}")
    
    except ValueError as e: 
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()