
# Třetí projekt: Stažení výsledků voleb do Poslanecké sněmovny (2017)

## Popis projektu
Tento projekt je vytvořen v rámci **Engeto Online Python Akademie**. Cílem projektu je stažení výsledků voleb do Poslanecké sněmovny z roku 2017 ze stránek volby.cz a jejich uložení do CSV souboru.

## Autor
- **Jméno**: Petr Novotný
- **Email**: hornstr@seznam.cz
- **Discord**: vasilek91_82724

## Instalace
Před spuštěním skriptu je třeba nainstalovat potřebné balíčky. Pro jejich instalaci vytvořte soubor `requirements.txt` se seznamem potřebných knihoven:

Seznam požadovaných knihoven:
- `requests`
- `beautifulsoup4`
- `urllib.parse`
- `re`
- `csv`
- `sys`

Následně spustíte příkaz:

```bash
pip install -r requirements.txt
```

Tímto příkazem se nainstalují všechny potřebné knihovny.

## Použití
Skript se spouští z příkazové řádky s následujícími argumenty:
```bash
python web_scraper.py <URL_územního_celku> <výstupní_soubor.csv>
```

- `<URL_územního_celku>`: URL odkazující na územní celek z volební stránky volby.cz (např. „https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=5103“).
- `<výstupní_soubor.csv>`: Název souboru, do kterého budou uloženy výsledky voleb (např. „vysledky.csv“).

### Příklad spuštění
Pro ukázku si vezmeme konkrétní odkaz na výsledky voleb pro část Středočeského kraje:

```bash
python projekt_3.py https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2 vysledky_stredocesky.csv
```

Po spuštění skriptu se výstupní soubor `vysledky_stredocesky.csv` naplní výsledky z jednotlivých okrsků ve formátu CSV. Každý okrsek bude obsahovat následující informace:
- Číslo okrsku
- Název okrsku
- Počet voličů
- Vydané obálky
- Platné hlasy
- Hlasy pro jednotlivé politické strany

### Ukázka výpisu výsledků
Po dokončení se vygeneruje soubor `vysledky_stredocesky.csv`, který bude obsahovat strukturovaná data, například takto:

| cislo_okrsku | nazev_okrsku | volici | vydane_obalky | platne_hlasy | Strana A | Strana B |
|--------------|--------------|--------|---------------|--------------|----------|----------|
| 1            | Okrsek 1     | 500    | 450           | 440          | 200      | 240      |
| 2            | Okrsek 2     | 300    | 280           | 270          | 120      | 150      |
| ...          | ...          | ...    | ...           | ...          | ...      | ...      |
