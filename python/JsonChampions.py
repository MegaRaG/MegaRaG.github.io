import json
import requests
from bs4 import BeautifulSoup
import ChampionsNames as ChampionsNames

ChampionsNames.main()

with open("./python/champion_names.txt", "r") as file:
    champion_names = [line.strip() for line in file.readlines()]

base_url = "https://rankedkings.com/lol-champion-skins/"
champions_info = []
champions_without_1820_rp = 0

for champion_name in champion_names:
    champion_data = {
        "name": champion_name,
        "legendary_skin_count": 0,
        "legendary_skins": []
    }

    url = base_url + champion_name.lower()
    response = requests.get(url)
    
    has_1820_rp_skin = False  # Flag to check if the champion has any skin priced at 1820 RP
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        skins = soup.find_all('div', class_='hover:cursor-pointer rounded shadow overflow-hidden hover:shadow-xl hover:ring-2 hover:ring-blue-400 col-span-1 relative')
        
        for skin in skins:
            price_element = skin.find('div', class_='absolute top-0 right-0 bg-black/70 px-1 py-0.5 text-white text-[0.7rem] flex-center-row rounded-bl')
            
            if price_element and '1820' in price_element.text:
                has_1820_rp_skin = True
                skin_name = skin.find('p', class_='text-xs text-black text-center hyphens-auto break-words').text
                champion_data["legendary_skin_count"] += 1
                champion_data["legendary_skins"].append(skin_name)

        if not has_1820_rp_skin:
            champions_without_1820_rp += 1

        champions_info.append(champion_data)
    else:
        print(f"Error fetching data for {champion_name}.")

# Informations globales
global_info = {
    "total_champions": len(champion_names),
    "champions_without_1820_rp": champions_without_1820_rp
}

# Création du format JSON
final_data = [
    {
        "total_champions": global_info["total_champions"],
        "champions_without_1820_rp": global_info["champions_without_1820_rp"]
    },
    {
        "datas": champions_info
    }
]

# Écrire les informations dans un fichier JSON
with open("./python/champions_info.json", "w") as json_file:
    json.dump(final_data, json_file, indent=4)
