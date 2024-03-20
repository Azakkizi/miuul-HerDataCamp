#######################################################################
###   Görev - 1 : Verilen değerlerin veri yapılarını inceleyiniz.   ###
#######################################################################

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
t = ("Machine Learning", "Data science")
s = {"Python", "Machine Learning", "Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))


##################################################################################################################################################
###   Görev - 2 : Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.  ###
##################################################################################################################################################

text = "The goal is to turn data into information, and information into insight."
print(text.upper().replace(",", " ").replace(".", " ").split())


######################################################################
###   Görev - 3 : Verilen listeye aşağıdaki adımları uygulayınız.  ###
######################################################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım-1: Verilen listenin eleman sayısına bakınız.
print("1- Uzunluk: " + str(len(lst)))

# Adım-2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print("2- 0. eleman: " + lst[0] + " ve 10. eleman: " + lst[10])

# Adım-3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
new_list = list(lst[:4])
print("3- " + str(new_list))

# Adım-4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
print("4- " + str(lst))

# Adım-5: Yeni bir eleman ekleyiniz.
lst.append("is fun!")
print("5- " + str(lst))

# Adım-6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")
print("6- " + str(lst))


###############################################################################
###   Görev - 4 : Verilen sözlük yapısına aşağıdaki adımları uygulayınız.   ###
###############################################################################

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım-1: Key değerlerine erişiniz.
dict.keys()

# Adım-2: Value'lara erişiniz.
dict.values()

# Adım-3: Daisy key'ine ait 12 değerini 3 olarak güncelleyiniz.
dict.update({"Daisy": ["England", 13]})

# Adım-4: Key değeri Ahmet value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})

# Adım-5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")


#####################################################################################################################################################################
###   Görev - 5 : Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.  ###
#####################################################################################################################################################################

l = [2, 13, 18, 93, 22]

def func(list):
    evens = []
    odds = []
    for number in list:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds


even_list, odd_list = func(l)
print(even_list, odd_list)


########################################################################################################################
###   Görev - 6 : Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri   #######
###   bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrencide #
###   tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.  ###
########################################################################################################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

# Beklenen çıktı:
# Mühensilik Fakültesi 1 . öğrenci: Ali
# Mühensilik Fakültesi 2 . öğrenci: Veli
# Mühensilik Fakültesi 3 . öğrenci: Ayşe
# Tıp Fakültesi 1 . öğrenci: Talat
# Tıp Fakültesi 2 . öğrenci: Zeynep
# Tıp Fakültesi 3 . öğrenci: Ece

for sira, ogrenci in enumerate(ogrenciler):
    if sira < 3:
        print("Mühendislik Fakültesi", sira+1, ". öğrenci:", ogrenci)
    else:
        print("Tıp Fakültesi", sira-2, ". öğrenci:", ogrenci)


#####################################################################################################################
###   Görev - 7 : Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan   ###
###   bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.   #######################################
#####################################################################################################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

# Beklenen çıktı:
# Kredisi 3 olan CMP1005 kodlu dersin kontenjanı 30 kişidir.
# Kredisi 4 olan PSY1001 kodlu dersin kontenjanı 75 kişidir.
# Kredisi 2 olan HUK1005 kodlu dersin kontenjanı 150 kişidir.
# Kredisi 4 olan SEN2204 kodlu dersin kontenjanı 25 kişidir.

for ders, kred, kont in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi", kred, "olan", ders, "kodlu dersin kontenjanı", kont, "kişidir.")


########################################################################################################################
###   Görev - 8 : Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsıyor ise ortak   #########
###   elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.#
########################################################################################################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kapsama(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kapsama(kume1, kume2)
