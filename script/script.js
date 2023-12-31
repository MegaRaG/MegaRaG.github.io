// Récupération des données JSON depuis le fichier
fetch('./python/champions_info.json')
  .then(response => response.json())
  .then(data => {
    // Affichage du nombre total de champions
    const totalChampionsElement = document.getElementById('totalChampionsValue');
    totalChampionsElement.textContent = data[0].total_champions;

    // Affichage du nombre de champions sans skins légendaires
    const without1820RPElement = document.getElementById('without1820RPValue');
    without1820RPElement.textContent = data[0].champions_without_1820_rp;

    // Accédez au conteneur global pour les champions
    const championsContainer = document.getElementById('championsContainer');

    // Parcourez chaque champion dans 'datas'
    data[1].datas.forEach(champion => {
      const championDiv = document.createElement('div');
      championDiv.className = 'champion-item';  // Ajout de la classe champion-item

      const championHeader = document.createElement('div');
      championHeader.className = 'list-header';
      championHeader.textContent = `${champion.name} - Legendary Skins: ${champion.legendary_skin_count}`;

      const skinsList = document.createElement('ul');
      champion.legendary_skins.forEach(skin => {
        const skinItem = document.createElement('li');
        skinItem.textContent = skin;
        skinsList.appendChild(skinItem);
      });

      championDiv.appendChild(championHeader);
      championDiv.appendChild(skinsList);

      championsContainer.appendChild(championDiv);
    });

  })
  .catch(error => {
    console.error('Error fetching the JSON file:', error);
  });
