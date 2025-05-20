import csv, time, os
from modules.config import (
        log_file, 
        result_file
        )

def CurrentTime():
    current_time = time.strftime("%H:%M:%S %d/%m/%Y") 
    return current_time

def RecordLog(err:list, type_record:str):
    if not os.path.exists(log_file):
        with open(log_file, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Type', 'Error', 'Date'])

    current_time = CurrentTime()
    with open(log_file, 'a+') as file:
        write = csv.writer(file)
        write.writerow([err[1], type_record, err[0], current_time])

def RecordResult(domain:str, record:str, type_record:str, name:str=None, company:str=None):
    if not os.path.exists(result_file):
        with open(result_file, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Company', 'Name', 'Type', 'Value', 'Date'])

    current_time = CurrentTime()
    with open(result_file, 'a+') as file:
        write = csv.writer(file)
        write.writerow([domain, company, name, type_record, record, current_time])
