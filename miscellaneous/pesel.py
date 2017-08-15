from datetime import date
from textwrap import wrap

def sex(n):
    ''' returns the sex of a person based on pesel '''
    print(n)
    return 'M' if n%2 else 'F'

def list_to_int(l):
    ''' age helper converting list of len =2 to an int '''
    return 10*l[0] + l[1]

def age(birth):
    ''' returns the age of a person based on pesel '''
    year  = list_to_int(birth[:2])
    month = list_to_int(birth[2:4])
    day   = list_to_int(birth[4:6])
    if month < 13:
        year = 1900 + year
    elif month < 33:
        year = 2000 + year
        month -= 20
    elif month > 80:
        year = 1800 + year
        month -= 80
    birth = date(year, month, day)
    today = date.today()
    return (today-birth).days//365

def pesel():
    ''' returns age and sex based on pesel '''
    pesel = list(map(int, wrap(input(), 1)))
    a   = age(pesel[:6])
    s   = sex(pesel[9])
    return a, s

if __name__ == '__main__':
    print(pesel())
