
names=['Eda','Yagmur','Beyza','Ilayda']
years=[2002,1998,2003,2001]

#'Cenk'ismini listenin sonuna ekleyin.
result=names.append('Cenk')

#'Sena' listenin başına ekleyin
names.insert(0,'Sena')

#Ilayda ismini listeden siliniz
names.remove('Ilayda')
names.pop(2) #indeks numarası 2 olan kayıtı silebilir

#'Eda'isminin indeksi nedir?
index=names.index('Eda')
names.pop(index) # indeksini bilmediğimiz verinin silinmesi için kullanılan yöntem

#'Ali' listenin bir elemanı mıdır?

result='Ali' in names
print (result)

#Liste elemanlarını ters çevir.
names.reverse()

#Liste elemanlarını alfabetik sıralayınız

names.sort()

#years listesini rakamsal sıraya göre sıralayınız

years.sort()

#str= 'Dacia, Chevrolet' karakterini dizeye çevirin
str= 'Dacia, Chevrolet'
str.split()
print(str)

#years dizisinin en büyük ve en küçük elemanı nedir?
max=max(years)
min=min(years)

print(max,' ', min)

#years dizisinde kaç tane 1988 değeri vardır

result = years.count(1988)
print(result)

#years dizisinin tüm elemanlarını siliniz
years.clear()


#Kullanicidan aldiğiniz üç tane marka bilgisini bir listede saklayınız

markalar=[]
marka=input("marka: ")
markalar.append(marka)

print(markalar)


print(names)
print(years)