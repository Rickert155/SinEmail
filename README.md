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
Можно передать домен или имейл параметром
```sh
python3 SinEmail.py --domain test@domain.com
```
Записк из своего скрипта пример
```sh
#!/usr/bin/python3
# Пример test.py
from modules.checker import checkDNS

checkDNS(domain="google.com")
```
```sh
python3 test.py
```

