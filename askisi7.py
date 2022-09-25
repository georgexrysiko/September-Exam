import requests

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'

def nag(lst):
    OPAP_RESULTS = 'https://api.opap.gr/draws/v3.0/1100/last-result-and-active'
    headers = {'User-Agent': UA}
    r = requests.get(OPAP_RESULTS, headers=headers)
    data = r.json()

    valid = []
    lst_kino = data["last"]["winningNumbers"]["list"]
    
    for i in lst:
        for n in range(i-1, i+1):
            if n in lst_kino:
                valid.append(i)
                break        

    return len(valid)