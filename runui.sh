pyuic5 -x window.ui -o window.py
if [[ $1 != "-c" ]]; then
python window.py
rm window.py
:
fi
