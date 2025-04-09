import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        print(f"\n🃏 Joke: {joke['setup']}")
        input("🤔 Press Enter for the punchline...")
        print(f"😂 Punchline: {joke['punchline']}\n")
    except requests.RequestException as e:
        print("❌ Error fetching joke:", e)

if __name__ == "__main__":
    get_joke()
