print("Lütfen bölme için iki sayı giriniz.")
bolum=int(input("Lütfen bölme için ilk sayınızı giriniz:"))
bolen=int(input("Lütfen bölme için ikinci sayınızı giriniz:"))
if bolen != 0: # eğer bölne sıfır değilse
    print(bolum,"/",bolen,"=", bolum/bolen)
if bolen == 0: # sıfıra bölmeye çalışıldığında
    print("sıfıra bölme yapılamaz")