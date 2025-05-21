#!/usr/bin/bash
cp -r SinEmail ../Sin
cp __init__.py ../
cp requirements.txt ../requirements.txt
cd ..
rm -rf SinEmail
mv Sin SinEmail
python3 -m venv venv
source venv/bin/activate
pip install -r package.txt
