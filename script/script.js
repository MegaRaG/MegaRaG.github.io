// Récupération des données JSON depuis le fichier
fetch('../python/results.json')
  .then(response => response.json())
  .then(data => {
    // Affichage du nombre total de champions
    const totalChampionsElement = document.getElementById('totalChampionsValue');
    if (totalChampionsElement) {
      totalChampionsElement.textContent = data.total_champions;
    } else {
      console.error("Element with ID 'totalChampionsValue' not found!");
    }

    // Affichage du nombre de champions sans skins légendaires
    const without1820RPElement = document.getElementById('without1820RPValue');
    if (without1820RPElement) {
      without1820RPElement.textContent = data.champions_without_1820_rp;
    } else {
      console.error("Element with ID 'without1820RPValue' not found!");
    }

    // Affichage de la liste des champions sans skins 1820 RP
    const championsList = document.getElementById('championsList');
    championsList.innerHTML = ''; // Vidage de la liste
    data.champions_without_1820_rp_list.forEach(champion => {
      const listItem = document.createElement('li');
      listItem.textContent = champion;

      // Vérification si le champion est "Qiyana" et ajout d'une classe si nécessaire
      if (champion === "Qiyana") {
        listItem.classList.add('important-champion');
      }

      championsList.appendChild(listItem);
    });

    // Affichage de la liste des skins 1820 RP
    const skinsList = document.getElementById('skinsList');
    skinsList.innerHTML = ''; // Vidage de la liste
    data.skins_1820_rp_list.forEach(skin => {
      const listItem = document.createElement('li');
      listItem.textContent = skin;
      skinsList.appendChild(listItem);
    });

  })
  .catch(error => {
    console.error('Error fetching the JSON file:', error);
  });
