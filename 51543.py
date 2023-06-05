#TASK 1 PARSOWANIE

import sys
import yaml
import xml.etree.ElementTree as TreeEl
import json

def parsowanie_arg():
    if len(sys.argv) !=3:
        print("program wejścia i wyjścia różnego formatu")
        sys.exit(1)

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
        print("nieprawidłowy plik!")
        sys.exit(1)

