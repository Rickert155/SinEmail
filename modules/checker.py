import dns.resolver
from modules.recording import RecordLog 

def checkDNS(domain:str, type_record:str):
    """Проверяем записи"""
    status_dns, err = checkRecords(domain=domain, type_record=type_record)
    if err == None:
        status_dns.sort()
        number_record = 0
        for record in status_dns:
            number_record+=1
            print(f"[{number_record}] {record}")

    else:
        print(f"Domain:\t{err[1]}\n{err[0]}")
        RecordLog(err=err, type_record=type_record)

def checkRecords(domain:str, type_record:str):
    records = []
    err = None
    try:
        for x in dns.resolver.resolve(domain, type_record):
            records.append(x.to_text())
    except Exception as dns_error:
        records = None
        err = [dns_error, domain]
    return records, err


