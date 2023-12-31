import requests

def clean_champion_name(name):
    name = name.replace(' ', '-')
    name = name.replace('.', '-')
    name = name.replace("'", "")
    name = name.replace('&', '--')
    
    if '--' in name:
        name = name.replace('--', '-')
    
    return name

def fetch_champion_data():
    url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json"
    
    try:
        response = requests.get(url)
        return response.json().get('data', {})
    except Exception as e:
        return {}

def get_champion_names():
    champions_data = fetch_champion_data()
    champion_names = [clean_champion_name(champion.get('name', '')) for champion in champions_data.values()]
    return champion_names

def write_to_file(champion_names, filename="champion_names.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        for name in champion_names:
            file.write(f"{name}\n")

def main():
    champion_names = get_champion_names()
    
    if champion_names:
        write_to_file(champion_names)

if __name__ == "__main__":
    main()
