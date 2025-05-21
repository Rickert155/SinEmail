#!/usr/bin/bash
cp -r ../SinEmail ../Sin
cp __init__.py ../
cp package.txt ../package.txt
cd ..
rm -rf SinEmail
mv Sin SinEmail
python3 -m venv venv
./venv/bin/pip install -r package.txt
