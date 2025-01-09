matn = " aeuio 'o/'' 'O'' AEIUO"

text = input("matnni kiriting:   ")

top = ''.join(filter(lambda x: x in matn,text)).upper()
print(top)
