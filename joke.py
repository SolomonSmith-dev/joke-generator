import requests
import logging
import argparse  # Handles command-line arguments

# Configure logging output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_joke():
    """
    Fetch a single random joke from the API.
    Returns:
        dict: Joke with 'setup' and 'punchline', or None on failure.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        logging.warning("⏰ Joke request timed out.")
    except requests.RequestException as e:
        logging.error("❌ Request failed: %s", e)
    return None

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="🃏 CLI Joke Generator")
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of jokes to fetch (1-10)"
    )

    args = parser.parse_args()

    # Clamp joke count between 1 and 10
    count = max(1, min(args.count, 10))
    logging.info("Fetching %d joke(s)...", count)

    for i in range(count):
        logging.info("Fetching joke #%d", i + 1)
        joke = get_joke()
        if joke:
            print(f"\n🃏 Joke {i+1}: {joke['setup']}")
            input("🤔 Press Enter for the punchline...")
            print(f"😂 Punchline: {joke['punchline']}\n")
        else:
            print("⚠️ Skipped due to fetch error.")

# Standard Python entry point
if __name__ == "__main__":
    main()
