#program sonuna girdiği notları kaçıncı not olduğu bilgisiyle beraber yazdır.
#kişi direkt ortalama not girmek yerine vize final notu girecek,siz oradan
#o dersin ortalamasını hesaplayıp geçip kalma durumuna göre işlem yapacaksınız
#vize %40 final %60

derssayisi = int(input("Ders sayısı giriniz: "))
ortalamalar = []
for note in range(derssayisi):
    vizenotu = float(input(f"{note+1}. dersin vize notu giriniz: "))
    finalnotu = float(input(f"{note+1}. dersin final notu giriniz: "))
    ortalama = vizenotu * 0.4 + finalnotu* 0.6 
    ortalamalar.append(ortalama)
print(ortalamalar)
for sonuc in range(len(ortalamalar)):
    if ortalamalar[sonuc] >= 50:
        print(f"{sonuc + 1}. dersi geçtiniz. ") 
    else:
        print(f"{sonuc + 1}. dersten kaldınız. ")
