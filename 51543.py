#TASK 1 PARSOWANIE

import sys
import yaml
import xml.etree.ElementTree as TreeEl
import json
sys.stdout.reconfigure()
def parsowanie_arg():
    if len(sys.argv) !=3:
        print("program wejscia i wyjscia roznego formatu")
        sys.exit(0)

    plik_pocz = sys.argv[1]
    plik_konc = sys.argv[2]
    return plik_pocz, plik_konc


#TASK 2 WCZYTYWANIE DANYCH Z PLIKU JSON

def wczytaj_json(plik_pocz):
    try:
        with open(plik_pocz, 'r') as plik:
            dane = json.load(plik)
            return dane
    except FileNotFoundError:
        print("nie znaleziono takiego pliku, przepraszamy")
    except json.JSONDecodeError:
        print("nieprawidlowy plik!")
        sys.exit(1)


#TASK 3 ZAPISYWANIE DANYCH DO PLIKU JSON

def zapisz_json(dane, plik_konc):
    try:
        with open(plik_konc, 'w') as plik:
            json.dump(dane, plik, indent=4)
        print("plik zapisany jako json")
    except:
        print("niepowodzenie!")
        sys.exit(1)

#TASK 4 WCZYTYWANIE DANYCH Z PLIKU YML

def wczytaj_yaml(plik_pocz):
    try:
        with open(plik_pocz, 'r') as plik:
            dane = yaml.safe_load(plik)
            return dane
    except FileNotFoundError:
        print("nie znaleziono takiego pliku, przepraszamy")
    except yaml.YAMLError:
        print("nieprawidlowy plik!")
        sys.exit(1)

#TASK 5 ZAPISYWANIE DANYCH DO PLIKU YML


def zapisz_yml(dane, plik_konc):
    try:
        with open(plik_konc, 'w') as plik:
            yaml.dump(dane, plik)
        print("plik zapisany jako yml")
    except:
        print("niepowodzenie!")
        sys.exit(1)


#TASK 6 WCZYTYWANIE DANYCH Z PLIKU XML


def wczytaj_xml(plik_pocz):
    try:
        do_drzew = TreeEl.parse(plik_pocz)
        zrodlo = do_drzew.getroot()
        return zrodlo
    except FileNotFoundError:
        print("nie znaleziono takiego pliku, przepraszamy")
        sys.exit(1)
    except TreeEl.ParseError:
        print("nieprawidlowy plik")
        sys.exit(1)



#TASK 7 ZAPIS DANYCH DO PLIKU XML

def zapisz_xml(zrodlo, plik_konc):
    try:
        do_drzew = TreeEl.ElementTree(zrodlo)
        do_drzew.write(plik_konc, encoding='utf-8', xml_declaration=True) #format utf-8 (najpopularniejszy) pozwoli na interoperacyjność pliku i że zostanie on rozpoznany i prawidłowo sformatowany
        print("plik zapisany jako xml")
    except:
        print("niepowodzenie!")
        sys.exit(1)



#TUTAJ ZNAJDUJĘ SIĘ FUNKCJA TEGO PROGRAMU


def glowna_funkcja():
    plik_pocz, plik_konc = parsowanie_arg()
    dane = None

    if plik_pocz.endswith('.json'):
        dane = wczytaj_json(plik_pocz)
    elif plik_pocz.endswith('.yml') or plik_pocz.endswith('.yaml'):
        dane = wczytaj_yaml(plik_pocz)
    elif plik_pocz.endswith('.xml'):
        zrodlo = wczytaj_xml(plik_pocz)
    else:
        print("Nieobsługiwany format pliku.")
        sys.exit(1)

    if plik_konc.endswith('.json'):
        zapisz_json(dane, plik_konc)
    elif plik_konc.endswith('.yml') or plik_konc.endswith('.yaml'):
        zapisz_yaml(dane, plik_konc)
    elif plik_konc.endswith('.xml'):
        zapisz_xml(zrodlo, plik_konc)
    else:
        print("Nieobslugiwany format pliku.")
        sys.exit(1)

if __name__ == '__main__':
    glowna_funkcja()




