import sys, codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

COMBINING_OVERLINE_CHAR = '\u0305'
SYMBOLS = [['I', 'X', 'C', 'M'], ['V', 'L', 'D']]
ROMAN = []

for i,_ in enumerate(SYMBOLS):
    ROMAN.append(SYMBOLS[i] + [s + COMBINING_OVERLINE_CHAR for s in SYMBOLS[i]])
ROMAN[0].remove(SYMBOLS[0][0] + COMBINING_OVERLINE_CHAR)


def latin(n):
    if n<1 or n>1000000: 
        return 

    latin_num=''
    n = str(n)[::-1] 
    for i,ch in enumerate(n):
        d = int(ch)
        if d<4:
            latin_d = d*ROMAN[0][i]
        elif d==4:
            latin_d = ROMAN[0][i] + ROMAN[1][i]
        elif d==5:
            latin_d = ROMAN[1][i]
        elif d<9:
            latin_d = ROMAN[1][i] + (d % 5)*ROMAN[0][i]
        elif d==9:
            latin_d = ROMAN[0][i] + ROMAN[0][i+1]
        latin_num = latin_d + latin_num
        
    return latin_num