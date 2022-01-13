git clone https://github.com/autorope/donkeycar
cd donkeycar/
pip install -e .[pc]
cd ..

git clone https://github.com/tawnkramer/gym-donkeycar
cd gym-donkeycar/
pip install -e .[gym-donkeycar]
cd ..

donkey createcar --path mysim
cd mysim
