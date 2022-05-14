cd dist
rm *
cd ..
python -m build
python -m twine upload dist/*
pip3 uninstall jpcm -y
pip3 install --upgrade jpcm
pip3 install --upgrade jpcm
cd src/jpcm/core
python core.py
cd ../../../