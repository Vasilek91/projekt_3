import requests as r
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import re
import csv
import sys
import time
import threading

vysledky = []

adresa = sys.argv[1]  # První argument: URL územního celku
soubor = sys.argv[2]  # Druhý argument: Jméno výstupního souboru

# Funkce, která bude zobrazovat tečky během stahování dat
def tecky_efekt():
    while not dokoncen_stahovani:
        for i in range(3):
            if dokoncen_stahovani:
                break
            print('.', end='', flush=True)
            time.sleep(0.5)
        if not dokoncen_stahovani:
            print('\r   \r', end='', flush=True)  # Smazání teček před dalším cyklem

# Flag pro dokončení stahování
dokoncen_stahovani = False

# Zkontrolujeme, jestli je adresa dostupná
test_pripojeni = r.get(adresa)
if test_pripojeni.status_code != 200:
    print(f'Zadaná adresa není dostupná. Kód chyby {test_pripojeni.status_code}')
    sys.exit()
else:
    print(f'Připojení proběhlo úspěšně, stahuji data z adresy: {adresa}. \nČekejte prosím\n', end='', flush=True)

    # Spuštění vlákna pro tečky
    vlakno = threading.Thread(target=tecky_efekt)
    vlakno.start()

try:
    # Získání první části adresy
    prvni_cast_adresy = adresa[0:adresa.find('nss') + 4]

    # Načtení HTML obsahu
    html_adresy = r.get(adresa).text
    parsed_html = bs(html_adresy, 'html.parser')

    # Zpracování HTML
    td_tagy = parsed_html.find_all('td', {'class': 'cislo'})
    nazev_obce = parsed_html.find_all('td', {'class': 'overflow_name'})  # Najde název obce

    for td, obec in zip(td_tagy, nazev_obce):
        a_tag = td.find('a')  # Najdeme tag <a> přímo
        nazev_okrsku = obec.text  # Najdu jmeno obce
        cislo_okrsku = td.text

        if a_tag:
            href = a_tag.get('href')  # Získáme href přímo
            if href:
                odkazy_okrsku = urljoin(prvni_cast_adresy, href)  # Vytvoříme plnou URL
                adresa_okrsku = r.get(odkazy_okrsku).text

                parsed_okrsku = bs(adresa_okrsku, 'html.parser')
                tabulka_okrsku = parsed_okrsku.find_all('td', {'headers': re.compile('^sa(2|3|6)$')})

                volici_okrsku, obalky_okrsku, platne_hlasy = [td.text for td in tabulka_okrsku]

                tabulka_stran = parsed_okrsku.find_all('td', {'headers': re.compile(r'^t\d+sb(2|3)$')})

                vysledek = {
                    'cislo_okrsku': cislo_okrsku,
                    'nazev_okrsku': nazev_okrsku,
                    'volici': volici_okrsku,
                    'vydane_obalky': obalky_okrsku,
                    'platne_hlasy': platne_hlasy
                }

                for i in range(0, len(tabulka_stran), 2):
                    strana = tabulka_stran[i].text.strip()
                    hlasy = tabulka_stran[i + 1].text.strip()
                    vysledek[strana] = hlasy

                vysledky.append(vysledek)

    # Získání záhlaví pro CSV
    zahlavi = vysledky[0].keys()

    # Zápis do CSV souboru
    with open(soubor, mode='w', newline='', encoding='utf-8') as nove_csv:
        zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)
        zapisovac.writeheader()
        zapisovac.writerows(vysledky)

finally:
    # Zastavíme zobrazování teček, když je stahování dokončeno
    dokoncen_stahovani = True
    vlakno.join()  # Počkáme na dokončení vlákna

print(f"\nData byla uložena do souboru {soubor}.")
