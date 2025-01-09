def sum(number):
    s=0
    for i in number:
        s+=i
    return s
    
sonlar = input("Raqamlarni kiriting:")
sonlar2 = list(map(int,sonlar.split()))

topla = sum(sonlar2)

print(f"Sonlarning yeg'indisi: {topla}")
