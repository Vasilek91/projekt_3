# Web Scraper pro volby do PS z webu volby.cz

Tento Python skript slouží k získání výsledků voleb z webu volby.cz a ukládání těchto výsledků do CSV souboru. Skript stahuje data o voličích, vydaných obálkách, platných hlasech a jednotlivých stranách zadaného územního celku.

## Požadavky

Před spuštěním tohoto skriptu je nutné mít nainstalované následující knihovny:

- `requests`
- `beautifulsoup4`
- `re`
- `csv`

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
python web_scraper.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105 vysledky.csv
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

Během stahování dat skript zobrazuje tečky, které signalizují probíhající stahování. Jakmile je stahování dokončeno, tečky přestanou "blikat" a uživatel bude informován o tom, že data byla uložena do CSV souboru.

Pokud URL není dostupná, skript vypíše chybu a ukončí program.

## Očekávaný výstup

Po dokončení stahování se v příkazové řádce zobrazí následující zpráva:

```
Připojení proběhlo úspěšně, stahuji data z adresy: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105. 
Čekejte prosím...
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

---

