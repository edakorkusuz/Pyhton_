'''
ogrenciler={
'number'={
 ad:''
 soyad:''
telefon:''
}
}

Bilgileri verilen ögrencileri kullanıcıdan aldığınız bilgilerle dictionryde saklayınız.
Öğrenci numarasını kullanıcıdan isteyip ilgili öğrenci bilgisini gösterin.

'''

#Önce boş bir dizi oluşturuyoruz.

ogrenciler={}

isim=input("İsim giriniz: ")
soyisim=input("Soyisim giriniz: ")
telefon=input("Telefon girini: ")
numara=input("Ogrenci no: ")

ogrenciler[numara]={
    'ad':isim,
    'soyad':soyisim,
    'telefon':telefon

}

ogrenciler.update({   #Yukardakinin aynısıdır aslında ama update ile birden fala veri ekleyebiliriz.
    numara:{
         'ad': isim,
         'soyisim':soyisim,
         'telefon': telefon
    },

       numara:{
         'ad': isim,
         'soyisim':soyisim,
         'telefon': telefon
    },

       numara:{
         'ad': isim,
         'soyisim':soyisim,
         'telefon': telefon
    }
})



print(ogrenciler)

ogrno= input("Ogrenci numarasini giriniz: ")
ogrenci=ogrenciler[ogrno]
print(ogrenci)  #Burada input olarak numarasını verdiğimiz öğrencinin bilgilerini görebileceğim.