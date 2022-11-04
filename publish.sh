cd dist
rm *
cd ..
python -m build
python -m twine upload dist/*
python -m pip uninstall jpcm -y
python -m pip install --upgrade jpcm
python -m pip install --upgrade jpcm

cd src/jpcm/core
python core.py
cd ../../../

git status
git add .
git commit -m "[auto] update"
git push