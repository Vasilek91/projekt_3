
# Třetí projekt: Stažení výsledků voleb do Poslanecké sněmovny (2017)

## Popis projektu
Tento projekt je vytvořen v rámci **Engeto Online Python Akademie**. Cílem projektu je stažení výsledků voleb do Poslanecké sněmovny z roku 2017 ze stránek volby.cz a jejich uložení do CSV souboru.

## Autor
- **Jméno**: Petr Novotný
- **Email**: hornstr@seznam.cz
- **Discord**: vasilek91_82724

## Instalace
Před spuštěním skriptu je třeba nainstalovat potřebné balíčky. Můžete je nainstalovat pomocí následujícího příkazu:

```bash
pip install -r requirements.txt
```

Seznam požadovaných knihoven:
- `requests`
- `beautifulsoup4`

## Použití
Skript se spouští z příkazové řádky s následujícími argumenty:
```bash
python <python_script> <URL_územního_celku> <výstupní_soubor.csv>
```

- `<URL_územního_celku>`: URL odkazující na územní celek z volební stránky volby.cz (např. „https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=5103“).
- `<výstupní_soubor.csv>`: Název souboru, do kterého budou uloženy výsledky voleb (např. „vysledky.csv“).

### Příklad spuštění
```bash
python web_scraper.py https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=5103 vysledky.csv
```

## Ověření a zpracování vstupních dat
- Skript kontroluje, zda zadaná URL odpovídá požadované struktuře stránky (musí začínat na „https://www.volby.cz/pls/ps2017nss/ps32“).
- Kontroluje, zda stránka vrací status kód 200 a zda obsahuje očekávanou strukturu (např. `<td class="cislo">` a `<td headers="sa1 sb1">`).
- Výstupní soubor musí mít formát `.csv` a nesmí obsahovat nepovolené znaky (`\/:*?"<>|`).

## Výstupní soubor
Skript zpracovává zadanou stránku, získává výsledky voleb a ukládá je do zadaného CSV souboru. CSV obsahuje následující data:
- Číslo okrsku
- Název okrsku
- Počet voličů, vydaných obálek a platných hlasů
- Hlasy pro jednotlivé strany v každém okrsku
