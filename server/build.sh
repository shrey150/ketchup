rm -rf build dist
python3 setup.py py2app -A --emulate-shell-environment
open ./dist/contacts.app/Contents/MacOS