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



