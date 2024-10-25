"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Petr Novotný
email: hornstr@seznam.cz
discord: vasilek91_82724
"""

import requests as r
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import re
import csv
import sys

# Vstupní argumenty
adresa = sys.argv[1]  # První argument: URL územního celku
soubor = sys.argv[2]  # Druhý argument: Jméno výstupního souboru
prvni_cast_adresy = adresa[0:adresa.find('nss') + 4]


# Kontrola připojení a validace stránky
def zkontroluj_adresu_a_obsah(adresa):
    if not adresa.startswith('https://www.volby.cz/pls/ps2017nss/ps32'):
        print(f'\nDošlo k chybě. Prosím zkontroluj vloženou adresu, zda odpovídá požadavku uvedenému v README.\n')
        sys.exit(1)

    try:
        response = r.get(adresa)
        parsed = bs(response.text, 'html.parser')

        if response.status_code != 200:
            print(f"\nDošlo k chybě. Stránka vrátila status code {response.status_code}\n")
            sys.exit(1)
        elif "page not found" in parsed.get_text().lower():
            print('\nDošlo k chybě. Zadaná stránka nebyla nalezena. Prosím zkontroluj vloženou adresu.\n')
            sys.exit(1)
        # Kontrola, zda stránka obsahuje očekávaný <td> element s class "cislo" a headers "sa1 sb1"
        elif not parsed.find('td',{'class':'cislo'}):
            print("\nDošlo k chybě. Stránka neobsahuje očekávaná data nebo strukturu.\n")
            sys.exit(1)
        else:
            print(f'\nPřipojení na adresu proběhlo úspěšně!\n')

    except r.exceptions.RequestException as e:
        print(f"\nDošlo k chybě. Chyba při pokusu o připojení: {e}\n")
        sys.exit(1)

# Kontrola názvu souboru
def kontrola_nazvu_souboru(soubor):
    if any(char in soubor for char in '\\/:*?"<>|'):
        print(f'\nProsím nepoužívejte nepovolené znaky \'\\/:*?"<>|\' \n')
        sys.exit(1)
    elif not soubor.endswith('csv'):
        print(f'\nUvedl jsi nesprávný formát výstupního souboru. Uveď prosím název s koncovkou .csv.\n')
        sys.exit(1)

# Zápis výsledků do souboru
def zapis_vysledku(soubor, vysledky):
    zahlavi = vysledky[0].keys()

    # Zápis do CSV souboru
    with open(soubor, mode='w', newline='', encoding='utf-8') as nove_csv:
        zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)
        zapisovac.writeheader()
        zapisovac.writerows(vysledky)
    print(f"\n\nData byla uložena do souboru {soubor}.\n")

def stahni_stranku(adresa):
    html_adresy = r.get(adresa).text
    parsed_html = bs(html_adresy, 'html.parser')    


# Zpracování okrsku
def zpracuj_okrsek(td, obec, prvni_cast_adresy):
    a_tag = td.find('a')
    nazev_okrsku = obec.text
    cislo_okrsku = td.text

    if a_tag:
        href = a_tag.get('href')
        if href:
            odkazy_okrsku = urljoin(prvni_cast_adresy, href)
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

            return vysledek
    return None

# Zpracování okrksů do seznamu
def zpracuj_vsechny_okrsky(td_tagy, nazev_obce, prvni_cast_adresy):
    vysledky = []
    total_okrsky = len(td_tagy)

    for index, (td, obec) in enumerate(zip(td_tagy, nazev_obce), 1):
        # Výpočet procent dokončení
        percent_done = (index / total_okrsky) * 100
        print(f"\rZpracováno {int(percent_done)} % okrsků", end='', flush=True)

        vysledek = zpracuj_okrsek(td, obec, prvni_cast_adresy)
        if vysledek:
            vysledky.append(vysledek)
    
    return vysledky

# Zpracuje zadanou adresu
def zpracovani_stranky(adresa, prvni_cast_adresy):
    html_adresy = r.get(adresa).text
    parsed_html = bs(html_adresy, 'html.parser')

    # Zpracování HTML
    td_tagy = parsed_html.find_all('td', {'class': 'cislo'})
    nazev_obce = parsed_html.find_all('td', {'class': 'overflow_name'})

    vysledky = zpracuj_vsechny_okrsky(td_tagy, nazev_obce, prvni_cast_adresy)
    return vysledky


# Kontrola vstupů
zkontroluj_adresu_a_obsah(adresa)
kontrola_nazvu_souboru(soubor)

# Zpracování stránky a získání výsledků
vysledky = zpracovani_stranky(adresa, prvni_cast_adresy)

# Zápis do CSV
zapis_vysledku(soubor, vysledky)

