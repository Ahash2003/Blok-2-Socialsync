# Deploy je applicatie op de BIM Cloud omgeving (hva-fys)

ZMARD wil de applicaties als SAAS aanbieden. Daarvoor heeft ZMARD een deploy omgeving ingericht. Om je applicatie online te krijgen doorloop je in overleg met de student assistent de volgende stappen.

## Pipeline aanpassen
- Uncomment bim runner
## docker-compose.yml
Wijzig de `docker-compose.yml` die in je root van het project staat. Dus wijzig niet de `docker-compose.yml` in /db!
- Vervang de VARS door de juiste waarden, zie de uitleg in het bestand
- Controleer of de naam van de image GEEN HoofdLetters bevat. Dus `DB1-` moet `db1-` zijn.
## Runner activeren
- Laat de hva-fys runner activeren
- Voeg de juiste variabelen toe in CI/CD: ID_RSA_HVA_FYS, SERVER_IP en SERVER_USER

De runner zal nu in actie komen bij een commit in de `main` branch. Dus zorg ervoor dat je in branches werkt om code uit te proberen/te ontwikkelen en zorg ervoor dat de `main` branch alleen werkende code bevat die je tijdens de sprint review wilt laten zien.

## Error Permission Denied ##
Je volgende stap is het oplossen van de permission denied error. Hoe zorg je er voor dat je nu veilig in een docker omgeving kunt inloggen in een database, zonder je wachtwoord op te slaan in je repo?