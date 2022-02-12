cd src/jpcm/core
python core.py
cd ../../../dist
rm *
cd ..
python -m build
python -m twine upload dist/*
pip3 uninstall jpcm
pip3 install --upgrade jpcm