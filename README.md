Zde je formátované `README.md`, které můžeš vložit přímo na GitHub. Text zůstává ve správném formátu a zachovává typické markdown konvence pro GitHub:

```markdown
# Web Scraper pro volby do Poslanecké sněmovny z roku 2017 z webu volby.cz

Tento Python skript slouží k získání výsledků voleb z webu volby.cz a ukládání těchto výsledků do CSV souboru. Skript stahuje data o voličích, vydaných obálkách, platných hlasech a jednotlivých stranách zadaného územního celku.

## Požadavky

Před spuštěním tohoto skriptu je nutné mít nainstalované následující knihovny:

- `requests`
- `beautifulsoup4`
- `re` (je součástí standardní knihovny Pythonu, není nutná instalace)
- `csv` (je součástí standardní knihovny Pythonu, není nutná instalace)

Pokud tyto knihovny nemáte, můžete je nainstalovat pomocí:

```bash
pip install requests beautifulsoup4
```

## Použití

Skript přijímá **dva argumenty**:

1. **URL adresa** územního celku z webu volby.cz
2. **Název výstupního CSV souboru**, do kterého budou uloženy výsledky

### Syntaxe:

```bash
python <název_skriptu.py> <url_adresy> <název_csv_souboru>
```

### Příklad použití:

```bash
python projekt_3.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105 vysledky.csv
```

### Popis argumentů:
- **`<url_adresy>`**: URL adresa stránky volebního okrsku, například: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105`.
- **`<název_csv_souboru>`**: Jméno souboru, kam budou výsledky uloženy (například `vysledky.csv`).

## Funkce

Skript načte data z dané URL adresy, analyzuje je pomocí knihovny **BeautifulSoup** a následně je uloží do CSV souboru s následujícími informacemi:

- Číslo okrsku
- Název okrsku
- Počet voličů
- Počet vydaných obálek
- Počet platných hlasů
- Strany a jejich hlasy

## Chování programu

Během zpracovávání dat skript zobrazuje procentuální dokončení zpracovaných okrsků. Jakmile je stahování dokončeno, uživatel bude informován o tom, že data byla uložena do CSV souboru.

Pokud URL není dostupná, nebo je neplatná, skript vypíše chybu a ukončí program.

## Očekávaný výstup

Po dokončení stahování se v příkazové řádce zobrazí následující zpráva:

```
Připojení na adresu proběhlo úspěšně!
Zpracováno 100 % okrsků
Data byla uložena do souboru vysledky.csv.
```

Výsledný soubor CSV bude obsahovat data ve formátu:

```
cislo_okrsku,nazev_okrsku,volici,vydane_obalky,platne_hlasy,Strana A,Strana B,Strana C
1234,Název Okrsku,1000,950,920,400,300,220
```

## Autor

- Jméno: Petr Novotný
- Kontakt: hornstr@seznam.cz
- Discord: vasilek91_82724
```

Tento text je připraven tak, aby byl ve správném formátu pro GitHub. Stačí ho uložit jako `README.md` soubor ve tvém repozitáři.
