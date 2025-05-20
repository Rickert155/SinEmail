import dns.resolver

def checkMX(domain:str):
    records = []
    err = None
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            records.append(x.to_text())
    except Exception as dns_error:
        records = None
        err = [dns_error, domain]
    return records, err


