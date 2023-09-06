def isphonenumber("this is my phonenumber 415-555-4242"):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
         return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
    for i in range(len(isphonenumber)):
    chunk=isphonenumber[i:i+12]
    if isphonenumber(chunk):
        print('Phonenumber is found:'+ chunk)
    print('completed')
