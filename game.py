# game.py
import json

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Brak pliku konfiguracyjnego! Skopiuj config.example.json do config.json.")
        return {}

def main():
    print("Uruchamianie fikcyjnej gry...")
    config = load_config()
    
    if "API_KEY" in config:
        print("Połączono z serwerem przy użyciu klucza API.")
    else:
        print("Tryb offline - brak klucza API.")

    print("Gra działa poprawnie!")

if __name__ == "__main__":
    main()