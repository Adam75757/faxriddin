def eng_katta(numbers):
    maxs = numbers[0]

    for i in numbers:
        if i>maxs:
            maxs = i
    return maxs
    
sonlar = input("raqamlar kiriting:")

sonlar2 = list(map(int,sonlar.split()))

eng_ke = min(sonlar2)
eng_k = eng_katta(sonlar2)

print(eng_k)
print(eng_ke)
