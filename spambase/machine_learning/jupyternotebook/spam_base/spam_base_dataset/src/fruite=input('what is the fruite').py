fruite=input('what is the fruite')
match fruite:
    case 'apple' | 'orange' | 'bnana' :
     print('good fruit')
    case 'revas'| 'water melone' | 'melone' 'hamon sakhte' :
     print('bad fruite')
    case _:
     print('wtf bro')  