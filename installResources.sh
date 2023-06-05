 #!/bin/bash

#za pomocą pipa instalujemy potrzebne elementy do pythona

echo"instalujemy pyinstallera"
pip install pyinstaller
echp "potem pyqt5 aby mieć możliwość korzystać z interfejsu bo taki był polecany"
pip install PyQt5
echp "i na koniec biblioteka pyyaml"
echo pip install pyYaml
echo "musimy sprawić by plik był możliwy do uruchomienia"
chmod +x installResources.sh

echo "RESZTA BIBLIOTEK"

pip install xmltodict
pip install jsonschema

