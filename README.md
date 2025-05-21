# SinEmail
### Утилита для проверки валидности имейлов

## MX Checker
Модуль написан написан при поддерждке библиотеки dnspython. Ее необходимо утсановить в окружение вместе с остальными пакетами
```sh
python3 -m venv venv

source venv/bin/activate

pip install -r package.txt
```
## Запуск
Можно передать домен или имейл параметром + тип записи
```sh
python3 SinEmail.py --domain test@domain.com MX
```
Записк из своего скрипта пример
```sh
#!/usr/bin/python3
# Пример test.py
from SinEmail.checker import checkDNS

checkDNS(domain="google.com", type_record="MX")
```
```sh
python3 test.py
```
## Прогон целой базы
Можно использовать данный модуль для прогона целой базы.
```sh
python3 SinEmail --calling test.csv
```
База должна быть в csv, миниму должна содержать колонку с доменами "Domain"

## Установка(как библиотеку)
При желании можно работать как с отдельной библитекой.   
Для этого можно:
- клонировать репозиторий
```sh
git clone https://github.com/rickert156/SinEmail.git
```
- запустить скрипт bash
```sh
./auth.sh
```
Далее можно будет импортировать модули таким образом:
```sh
#!/usr/bin/python3
from SinEmail.checker import checkDNS
```
