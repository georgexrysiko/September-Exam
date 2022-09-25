def ROT13(string):
    cipher =''
    shift = 13

    for ch in string:
        if ch.isupper():
            start = ord('A')
        else:
            start = ord('a')

        new_i = (ord(ch)-start + shift) % 26
        new_ch = chr(start + new_i)
        cipher += new_ch

    print(cipher)