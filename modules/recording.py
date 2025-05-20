import csv, time, os
from modules.config import log_file 

def Log(err:[], type_record:str):
    if not os.path.exists(log_file):
        with open(log_file, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Type', 'Error'])

    with open(log_file, 'a+') as file:
        write = csv.writer(file)
        write.writerow([err[1], type_record, err[0]])
