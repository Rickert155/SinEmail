def helper():
    info = """\
    --domain            Запуск скрипта с параметрами [domain] [type]
                        domain или email можно передать вторым параметром,
                        последним параметром передаем тип записи. Пример:
                        python3 SinEmail.py --domain my@email.com MX

    --calling           Запуск скрипта с параметром [file_name]
                        Поддерживается обработка CSV. Пример:
                        python3 SinEmail.py --calling test.csv
    """
    return info
