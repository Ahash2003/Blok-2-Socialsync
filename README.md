<img src=image.png>

## Opdrachtomschrijving

In het tweede blok word je uitgedaagd om als ondernemers samen met een andere student een zogenaamde Software as a Service (SaaS) oplossing te bedenken en te bouwen voor kleinere bedrijven.

[[_TOC_]]


## Wat je gaat maken ##

Na een kort onderzoek kom je tot een idee die je uitwerkt in een business plan. Gelijktijdig bouw je een [“Minimum Viable Product”](https://en.wikipedia.org/wiki/Minimum_viable_product), dat je gebruikt om feedback te krijgen van potentiële klanten. De beste teams presenteren aan het einde van het project hun business plan en product voor ondernemers in een zogenaamde Dragon's Den sessie, die vervolgens kiezen welke ze willen laten doorontwikkelen.

## Aan de slag als duo ##

Je hebt als duo nu 1 project aangemaakt in Gitlab. Zorg ervoor dat jullie beiden de juiste rechten hebben in dit Gitlab project. Kijk daarvoor bij Manage>Members (1 is owner, de ander minimaal maintainer). Clone daarna beiden dit project naar je eigen ontwikkelmachine (je eigen laptop). Dit doe je hetzelfde als in Blok 1 bij de Dokkie opdracht, dus via de blauwe `CLONE` knop.

Omdat je nu met meer dan 1 persoon gaat werken in dezelfde code, zul je moeten leren omgaan met branches. Branches zorgen ervoor dat wijzigingen in de code netjes in aparte vakjes komen. Oefen dit nu eerst.

1. Een persoon maakt een wijziging in de code.
2. Deze persoon doet nog geen commit.
3. Deze persoon maakt eerst een nieuwe branch aan in GIT, noem deze `dev`. [Lees na wat dit is](https://code.visualstudio.com/docs/sourcecontrol/overview#_branches-and-tags).
4. Nu pas doe je de commit. Zorg ervoor deze deze commit plaats vindt in de nieuwe branch `dev`.
5. Sync (oftewel push en pull) naar je `remote` (Gitlab project).
6. Controleer op Gitlab of je nu de nieuwe branch ziet (`Code > Branches`). Controleer of je daarbinnen de wijziging vindt die je verwacht.
7. Nu gaat de tweede persoon de wijzigingen binnenhalen, en daarmee de nieuwe branch (welk knop druk je dus op?)
8. Controleer op de ontwikkelmachine of je daar de wijzigingen ziet. Controleer of je de juiste branch ziet en erin werkt.

## Beschrijving van het project template Dragons Den ##
Je hebt een minimale Flask-applicatie gekregen: een zogenaamde hello world. Daarbinnen zijn een aantal Bueprints gedefinieerd en daarin vind je een voorbeeld van een deploy script van de SAAS oplossing. Lees deze beiden goed door.

In BIM Dokkie (blok 1) staat al heel veel voorbeeldcode. Deze gebruik je hier als inspiratie. Ook heb je de beschikking over de twee grote Flask manuals die we aanraden, zie hiervoor de desbetreffende learning story.

Bepaal beiden als allereerste de technische opzet van jullie applicatie. Welke handleiding gaan jullie gebruiken? Welke deploy techniek?
Bepaal ook de afspraken over het werken in branches. Werk niet in `main`, maar in `dev` of beter nog, in een branch per user story.

## Zo gebruik je deze repository als opdracht-template ##

- User stories 
    - Voor de opdracht zijn een aantal user stories opgesteld als start van het project, maar in dit blok maak je ook een aantal eigen user stories. Die ga je gebruiken om de webapplicatie te bouwen. Maar wat is een user story eigenlijk? Op [scrumguide.nl](https://scrumguide.nl/user-story/) vind je de volgende definitie:<br />
   “Een User Story is een korte beschrijving (Story) van wat een gebruiker (User) wil. User Stories worden gebruikt bij het ontwikkelen van producten of software binnen Agile raamwerken, waaronder Scrum. Een User Story bestaat uit enkele zinnen waarin staat wat de gebruiker van het product moet / wil doen. Een User Story is eigenlijk weinig gedetailleerd en zou moeten kunnen passen op een post-it. Via de User Story heeft de gebruiker invloed op het ontwikkelen van een systeem of product en uiteindelijk de functionaliteit ervan.”
    - Een user story noteer je volgens een vast format: 
_Als … (soort gebruiker) wil ik … (feature/actie), zodat … (doel/voordeel)._ Een voorbeeld van een user story: _“Als gamer wil ik met mijn ruimteschip kunnen schieten als ik op de spatiebalk druk, zodat ik vijandige aliens kan uitschakelen.”_
    - Deze user stories vormen zogenaamde Product Backlog. De product backlog vind je in deze Gitlab-repository onder `Issues > Selecteer <User Stories> in de dropdown`.Anders dan in het eerste blok is deze lijst nog niet compleet.
Via `Issues >` kun je user stories aanmaken voor de opdracht.  Het handigste is om deze dan het label `soort::user story` te geven. De user stories zijn daarmee te onderscheiden van bijvoorbeeld learning stories.
    - Tijdens het plannen van een sprint kan jullie de user story in een `Milestone` opnemen. Een Milestone gebruiken we hier synoniem van een sprint. Als een van jullie begint met het bouwen van een user story kan je je naam aan het issues koppelen en wordt het issues ongoing onder `Issues > Milestone > Sprint`. 

- Learning stories
    - De learning stories geven je houvast bij wat je moet of wilt leren. Tijdens het project werk je aan deze learning stories. Daarin staan de te leren vaardigheden en competenties binnen dit project. Deze learning stories vind je in de Gitlab-repository onder `Issues > Selecteer <Learning stories> in de dropdown`. 
    - Anders dan in het eerste blok leg je in dit blok ook eigen learning stories vast.
    - Via `Issues >` kun je learning stories aanmaken voor de opdracht.  Het handigste is om deze dan het label `soort::learning story` te geven. De user stories zijn daarmee te onderscheiden van bijvoorbeeld user stories.
    - Je kunt een milestone koppelen aan een learning story. 
    - Om een learning story te voltooien, zul je je user stories moeten afronden.

-   Milestones en sprintboard
    - Je werkt in zogeheten sprints. Tijdens een sprint selecteer je de learning stories en de user stories van de Product Backlog die je wil gaan oppakken en afronden in 2 of 3 weken (de duur van een sprint in deze opdracht). In totaal zijn er 3 sprints. Om een user story of learning story toe te wijzen aan een sprint wijs je deze toe aan een Milestone. Dit kun je doen bij de eigenschappen van een issue. Je kan hiervoor ook het board Planning Sprint 1 gebruiken.
    - Onder `Issues > Milestones > Sprint 1` kun je de burndown zien, wat er voor de sprint gepland staat, waar je mee bezig bent en wat af (done) is.
    - Aan het eind van een sprint moet er altijd een bruikbaar product zijn voor de eindgebruiker. User stories die niet af zijn gaan door naar de volgende sprint. Test en documenteer een user story dus goed voordat je deze op done zet.
    - Sprint 1 <br />In de eerste sprint bedenk je zelf een app waarmee je de MKB-markt kan bedienen of je sluit je aan bij een ZMARD-project. Tijdens de eerste sprint doe je een aantal korte onderzoeken om de markt te verkennen en maak je user- en learning stories voor de tweede sprint. 
    - Sprint 2<br /> In deze sprint ontwerp en bouw je de app. Om te beginnen zijn er daarvoor al een aantal user- en learning stories vastgelegd in GitLab maar deze zijn niet compleet. Aan jou de taak om deze af te maken. 
    - Sprint 3. <br />
In deze sprint bouw je de app en het business plan verder af en demonstreer je die aan mogelijke investeerders. 
    - Onder de pagina `Issues > Milestones `(te vinden via de balk links 👈🏽) vind je verschillende sprints en sprintboards:
    - Sprint 1 backlog (20 november - 3 december);
    - Sprint 2 backlog (4 december - 17 december);
    - Sprint 3 backlog (8 januari - 28 januari); 

- Technische documentatie 📄 
    - In de `docs` folder van de broncode komt de technische documentatie. Per learning story schrijft je uit wat je hebt geleerd. Het is belangrijk dat de documentatie onderdeel wordt van de broncode. Zo kan je vanuit de ontwikkelomgeving je documentatie bijhouden :).

## Kwaliteitsnormen

Je werkt volgende onderstaande kwaliteitsnormen:
- Je werkt volgens de agile methodiek van HBO-ICT.
- Je code voldoet aan de Google code conventions (https://google.github.io/styleguide/)
- Je code is (technisch) gedocumenteerd en relevant voor collega ontwikkelaars.

## Definition of Done (DoD)

Binnen scrum dient iedere user story te voldoen aan een zogenaamde Definition of Done (DoD). Door het opstellen en aanhouden van een Definition Of Done, zorg je ervoor dat het werk wat je aflevert ook daadwerkelijk gebruikt kan worden. Als je een user story hebt afgebouwd zet je 'm in _verify_ en controleer je of deze voldoet aan de _Definition of Done_ (zie hieronder). Pas als dat in orde is kun je de user story op _Done_ zetten.

### DoD generiek

- [ ] Alle acceptatiecriteria zijn afgevinkt.
- [ ] Het werk is (technische) gedocumenteerd en relevant voor collega-ontwikkelaars.
- [ ] Het werk is geschreven in Standaardnederlands.
- [ ] Het werk staat in de GitLab repository.
- [ ] Het werk is gereviewd door een peer.
- [ ] Het werk voldoet aan het Think-Make-Check (TMC) principe.

- [ ] De code is opgesteld volgens de HBO-ICT coding conventions.
- [ ] De code is handmatig functioneel getest op fouten.
- [ ] De code werkt zonder fouten bij normaal gebruik.
- [ ] De webapplicatie dient zowel op mobiele- als desktop-apparaten gebruikt te kunnen worden.

## Wanneer is <Opdracht> klaar?

Voor het bouwen van deze opdracht heb je 3 sprints de tijd. Aan het einde van die periode moet je applicatie aan een aantal verwachtingen voldoen. We noemen dit de kwaliteitscriteria. Voor dit blok zien de kwaliteitscriteria er als volgt uit:

| Cat.| Nr | Definition of Done | HBO-i model      |
|----|----|-----------------|------------------|
| 1 | K1 | Je werkt Agile volgens Agile Scrum methodiek. | G, S |
| 1| K2 | Je hebt de behoeftes van de doelgroep onderzocht en gebruikt om zelf een aantal user stories te schrijven.| G-A |
| 1| K3 | Je hebt de gebruikersinterface van jouw product aangepast door prototyping toe te passen. | G-A, G-O, G-R |
| 1| K4 | Je hebt een testplan geschreven en gebruikt om een gebruikerstest uit te voeren. | G-R|
| 2| K5 | Je hebt object georiënteerd geprogrammeerd en maak gebruik van objectgeoriënteerde technieken zoals abstraction, inheritance en encapsulation. | S-O, S-R |
| 2| K6 | Je hebt een genormaliseerde relationele database ontworpen en gebruikt om informatie uit je project in op te slaan, op te halen en te bewerken. | S-O, S-R |
| 2| K7 | Je hebt je werk beschreven met behulp van UML-technieken. | S-R, S-MC |

## Gedragscriteria

Om een IT-project succesvol op te leveren, is het noodzakelijk dat je leert om je als een professional te gedragen. Je hebt hiervoor vaardigheden nodig, die we binnen het hbo professional skills noemen. Voor dit project dient je gedrag aan de volgende criteria te voldoen:

| Cat. | Nr | Gedragscriteria | HBO-i model |
|----|----|------------|----------------|
| 3 | G1 | Je neemt verantwoordelijkheid voor je eigen handelen. Je aanvaardt consequenties van jouw gedrag. Je geeft op constructieve feedback aan medestudenten en ontvangt feedback. Je geeft aan hoe je die feedback gaat gebruiken. Je werkt resultaat gericht aan je opdracht of taak. Je hebt een actieve werkhouding. Je leert van en met elkaar en bent aanwezig op contactmomenten. Je herkent waar je leerbehoeftes zitten en stelt doelen op om deze te vervullen. Je reflecteert op je handelen en je evalueert je doelen.| PL-PO |
| 4| G4 | Je werkt volgens (gegeven) kwaliteitsnormen. | TO-M | 
| 4| G5 | Je kan constructief samenwerken in een duo. | DI-P | 
| 4| G6 | Je gebruikt bronnen om antwoorden te vinden op een passende manier *). | OP-O | 
| 4| G7 | Je kunt je doel door middel van een presentatie begrijpelijk overbrengen aan de doelgroep.| DI-C |
| 4| G8 | Je schrijft gestructureerde en begrijpelijke documentatie **). | DI-C | 
| 4| G10 | Je bent je bewust van de invloed die je uitoefent met jouw werk. | TO-E | 

*)    Je gebruikt diverse bronnen om inzicht te krijgen in de SAAS markt<br />
**)   Onderdeel van de documentatie is een businessplan, inclusief budgetplan waarmee investeerders inzicht krijgen in je project.

## Lesmateriaal

In de learning stories staan verwijzingen naar het lesmateriaal. Bijvoorbeeld de Knowledge Base, de Digitale Leeromgeving (DLO), videomateriaal, etc.

## HBO-i
_Binnen deze opdracht ligt de focus op de volgende beroepstaken:_

- Software ontwerpen (S-O) : niveau 1
- Software realiseren (S-R) : niveau 1
- Software manage & control (S-MC) : niveau 1
- Gebruikersinteractie analyseren (G-I) : niveau 1
- Gebruikersinteractie ontwerpen (G-O) : niveau 1
- Gebruikersinteractie realiseren (G-R) : niveau 1

_Binnen deze opdracht ligt de focus op de volgende professional skills:_

- Persoonlijk leiderschap (PL) :
  - Ondernemend zijn (PL-O) : niveau 1
  - Persoonlijke ontwikkeling (PL-PO): niveau 1
- Toekomstgericht organiseren (TO)
  - Managen (TO-M) : niveau 1
  - Ethiek (TO-E) : niveau 1
- Doelgericht interacteren (DI) 
  - Communiceren (DI-C) : niveau 1
- Onderzoekend probleemoplossen (OP) :
  - Onderzoeken (OP-O) : niveau 1

