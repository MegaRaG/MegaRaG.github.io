import json
import requests
from bs4 import BeautifulSoup
import ChampionsNames as ChampionsNames

ChampionsNames.main()

with open("champion_names.txt", "r") as file:
    champion_names = [line.strip() for line in file.readlines()]

print(f"Total number of champions: {len(champion_names)}")

base_url = "https://rankedkings.com/lol-champion-skins/"
skins_with_1820_rp = []
count_1820_rp_skins = 0
champions_without_1820_rp_skin = []

for champion_name in champion_names:
    url = base_url + champion_name.lower()
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        skins = soup.find_all('div', class_='hover:cursor-pointer rounded shadow overflow-hidden hover:shadow-xl hover:ring-2 hover:ring-blue-400 col-span-1 relative')
        
        for skin in skins:
            price_element = skin.find('div', class_='absolute top-0 right-0 bg-black/70 px-1 py-0.5 text-white text-[0.7rem] flex-center-row rounded-bl')
            
            if price_element and '1820' in price_element.text:
                skin_name = skin.find('p', class_='text-xs text-black text-center hyphens-auto break-words').text
                skins_with_1820_rp.append(f"{skin_name}")
                count_1820_rp_skins += 1

        if count_1820_rp_skins == 0:
            champions_without_1820_rp_skin.append(champion_name)
        
        count_1820_rp_skins = 0

    else:
        pass

result_data = {
    "total_champions": len(champion_names),
    "champions_without_1820_rp": len(champions_without_1820_rp_skin),
    "champions_without_1820_rp_list": champions_without_1820_rp_skin,
    "skins_1820_rp_list": skins_with_1820_rp
}

with open("results.json", "w") as json_file:
    json.dump(result_data, json_file, indent=4)
