def rezervasyon(salon): #kategori ve bilet bilgisini alır, ilgili rezarvasyon fonksiyonu ile ucretHesapla fonksiyonunu çağırır
    global kalanBilet
    global biletMax
    kalanBilet=[100,100,100,100]

    while True:
        seçimKategori = int(input("Kategori (1-4)? "))  # geçerli bir kategori girilene kadar sormaya devam eder
        if (seçimKategori >= 1) and (seçimKategori <= 4):
            break
    while True:                                         # geçerli bir bilet sayısı girilene kadar sormaya devam eder
        seçimBiletAdet = int(input("Bilet adeti (1-10)? "))
        if (seçimBiletAdet >= 1) and (seçimBiletAdet <= int(biletMax)):
            break
    if seçimKategori == 1:
        if(kalanBilet[0]-seçimBiletAdet>=0):            # 1.kategoride rezerve edilmek istenen koltuk sayısı kadar boş koltuk var mı diye kontrol eder
            kalanBilet[0]-=seçimBiletAdet
            rezerveKategori_1(salon, seçimBiletAdet)
            ucretHesapla(seçimBiletAdet,seçimKategori)
        else:
            print("Girdiğiniz bilet sayısı için kategoride yeterli koltuk kalmadı\nKategoride rezerve edilebilecek koltuk sayısı=",kalanBilet[0])
    elif seçimKategori == 2:
        if(kalanBilet[1]-seçimBiletAdet>=0):            # 2.kategoride rezerve edilmek istenen koltuk sayısı kadar boş koltuk var mı diye kontrol eder
            kalanBilet[1]-=seçimBiletAdet
            rezerveKategori_2(salon, seçimBiletAdet)
            ucretHesapla(seçimBiletAdet,seçimKategori)
        else:
            print("Girdiğiniz bilet sayısı için kategoride yeterli koltuk kalmadı\nKategoride rezerve edilebilecek koltuk sayısı=",kalanBilet[1])
    elif seçimKategori == 3:
        if(kalanBilet[2]-seçimBiletAdet>=0):            # 3.kategoride rezerve edilmek istenen koltuk sayısı kadar boş koltuk var mı diye kontrol eder
            kalanBilet[2]-=seçimBiletAdet
            rezerveKategori_3(salon, seçimBiletAdet)
            ucretHesapla(seçimBiletAdet,seçimKategori)
        else:
            print("Girdiğiniz bilet sayısı için kategoride yeterli koltuk kalmadı\nKategoride rezerve edilebilecek koltuk sayısı=",kalanBilet[2])
    elif seçimKategori == 4:
        if(kalanBilet[3]-seçimBiletAdet>=0):            # 4.kategoride rezerve edilmek istenen koltuk sayısı kadar boş koltuk var mı diye kontrol eder
            kalanBilet[3]-=seçimBiletAdet
            rezerveKategori_4(salon, seçimBiletAdet)
            ucretHesapla(seçimBiletAdet,seçimKategori)
        else:
            print("Girdiğiniz bilet sayısı için kategoride yeterli koltuk kalmadı\nKategoride rezerve edilebilecek koltuk sayısı=",kalanBilet[3])

def salonYazdir(salon):                 # salonu bastırır
    for i in salon:     
        for y in i:
            print(y, end=" ")
        print("")

def yeniEtkinlik(salon):                # salonu boşaltır, bilet ve ciro sayısını sıfırlar
    salon.clear()
    for i in range(0, 20):  # salonu tekrar oluşturur
        salon.append("--------------------")
    global kalanBilet
    global toplamCiro
    for i in range(0,4):
        kalanBilet[i]=100
        toplamCiro[i]=0

def rezerveKategori_1(salon, biletNo):  # 1. kategori için rezervasyon işlemini yapar
    counter = 10
    # ----EN SON HANGİ KOLTUĞUN REZERVE EDİLDİĞİNİ BULMAK İÇİN----
    for i in salon[9::-1]:      # son rezerveyi bulmak için en son sırada sağdan sola doğru x değeri arar, bulamazsa üst sıraya geçer
        counter = counter - 1   # counter sıra indisini tutar
        a = i.rfind("x")
        if a>=15:               # 2.kategori sağ taraftan x algıladı, 1. kategori için durum kontrol edilir
            a=salon[counter][5:15].rfind("x")
            if a<0:             # demek ki bu sırada 1. kategori boş, aramaya üst sıradan devam edilir
                continue
            else:               # 1.kategori bu sırada aranan koltuk bulundu, döngüden çıkılır
                a=a+5
                break
        elif a<=4:              # 2.kategori sol taraftan algıladı, 1. kategori bu sırada boş, aramaya üst sıradan devam edilir
            continue
        elif a >=5 and a<=14:   # 2.kategori sağ tarafta x algılanmadı, 1. kategori için aranan son koltuk bulundu, döngüden çıkıldı
            break
    # ----EN SON REZERVE EDİLEN KOLTUĞA GÖRE REZERVASYON İŞLEMİNE BAŞLANACAK SIRA VE KOLTUK İNDİSLERİNİN BELİRLENMESİ----
    if (a < 0):      # kategori için yapılacak ilk rezervasyon işlemi
        biletBaslangic = 5
        siraBaslangic = 0
    elif (a == 14):  # o sıranın sonuncu koltuğu rezerve edilmiş bilet başlangıç değerine bir sonraki sıranın ilk koltuğu atılır
        biletBaslangic = 5
        siraBaslangic = counter + 1
    else:            # en son rezerve edilen koltuktan bir sonraki değer bilet başlangıç değerine atılır
        biletBaslangic = a + 1
        siraBaslangic = counter
    print("-->Rezerve edilen koltuklar:",end="")
    # ----BİLET REZERVE KISMI----
    if (biletBaslangic + biletNo > 15):     # Durum A: rezerve edilecek koltukların bir kısmı alt satıra geçecek
        counter = 0
        for i in range(0, (15 - biletBaslangic)):
            counter = counter + 1               # counter kaç bilet rezerve edildiğini tutuyor
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
        siraBaslangic = siraBaslangic + 1       # alt satıra geçildi
        biletBaslangic = 5
        for i in range(0, (biletNo - counter)): # biletNo-counter=kaç tane daha rezerve edilmesi gereken bilet var
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
    else:                                   # Durum B: aynı sıra içinde kalacak
        for i in range(biletNo):
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")

def rezerveKategori_2(salon, biletNo):  #2. kategori için rezervasyon işlemini yapar
    counter = 10
    # ----EN SON HANGİ KOLTUK REZERVE EDİLMİŞ ONU BULMAK İÇİN----
    for i in salon[9::-1]:      # son rezerveyi bulmak için en son sırada sağdan sola doğru x değeri arar, bulamazsa üst sıraya geçer
        counter = counter - 1   # counter sıra indisini tutar
        a = i.rfind("x")
        if a >= 15:             # sağ tarafta kalınan yeri buldu, döngüden çıkılır
            break
        elif a>=5:              # 1. kategoriden x algılandı, 2. kategori sol taraf için kontrol edilir
            a=salon[counter][0:5].find("x")
            if counter!=0 and a<0:      # bu sırada hiç 2. kategoriden rezerve yapılmamış üst sıraya geçilir
                continue
            elif counter!=0 and a<=4:   # 2.kategoride sol tarafta nerede kalındığını buldu, döngüden çıkılır
                break
            elif counter==0 and a<0:    # daha önce 2. kategoriden hiç rezerve yapılmamış->ilk rezerve işlemi
                break
        elif a<=4 and a>=0:     # sağ taraf boş solda rezerve yapılmış koltuk buldu, döngüden çıkılır
            break   
    # ----EN SON REZERVE EDİLEN KOLTUĞA GÖRE REZERVASYON İŞLEMİNE BAŞLANACAK SIRA VE KOLTUK İNDİSLERİNİN BELİRLENMESİ----
    if a < 0:      # ilk rezervasyon işlemi
        biletBaslangic = 4
        siraBaslangic = 0
    elif a == 19:  # sıranın en son koltuğunda kaldıysa alt sıraya geçiş yapılır
        biletBaslangic = 4
        siraBaslangic = counter + 1
    elif a >= 15:  # sağ tarafta kaldıysa
        biletBaslangic = a + 1
        siraBaslangic = counter
    else:          # sol tarafta kaldıysa
        a = salon[counter].find('x')  # solda kalınan yer bulunur
        if a > 0:       # demek ki solda hala bilet rezerve edilecek yer var
            biletBaslangic = a - 1
            siraBaslangic = counter
        else:           # sol tamamen dolu sağ kısma geçiş sağlanır
            biletBaslangic = 15
            siraBaslangic = counter
    print("-->Rezerve edilen koltuklar:",end="")
        # --------------BİLET REZERVE KISMI--------------
    if biletBaslangic < 5:  # ---DURUM A: SOLDAN BAŞLAYAN KISIM
            if biletBaslangic - biletNo >= -1:  # Durum A.1: rezervasyon sağ tarafa geçmeden, sadece sol tarafta yapılacak
                for i in range(biletNo):
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                    print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
            else:                               # Durum A.2: rezervasyonun bir kısmı sağ tarafı da dolduracak
                biletCounter = 0
                for i in range(0, biletBaslangic + 1): # sol tarafı doldurmak için
                    biletCounter = biletCounter + 1
                    if (biletBaslangic - i) != 0:      # sıranın en başındaki koltuğa gelene kadar sol tarafı doldurur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                    else:                              # sıranın en başındaki koltuk rezerve edilir
                        salon[siraBaslangic] = "x" + salon[siraBaslangic][1:]
                    print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")    
                biletBaslangic = 15  # sağ kısma geçildi
                kalanBilet=biletNo-biletCounter
                if biletBaslangic+kalanBilet<=20: # Durum A.2.1: rezervasyon sırasında sol alta, yeni sıraya geçilmeyecek
                    for i in range(0, kalanBilet):          # sağ kısım kalan bilet sayısı kadar doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic+1+i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
                else:                             # Durum A.2.2: rezervasyon sırasında sol alta yeni sıraya geçecek
                    for i in range(0, (20-biletBaslangic)): # önce sağ taraf doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic+1+i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
                    biletBaslangic=4                        # alt sıraya, sol tarafa geçildi
                    siraBaslangic=siraBaslangic+1
                    for i in range(kalanBilet-5):           # sol kısım bilet sayısı kadar doldurulur  
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
    else:   # ---DURUM B: SAĞDAN BAŞLAYAN KISIM
            if biletBaslangic + biletNo < 20:  # Durum B.1: sol alta geçmeden sadece sağ taraftan rezervasyon yapılacak                      
                for i in range(0, biletNo):         # sağ kısım bilet sayısı kadar doldurulur
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                    print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
            else:                              # Durum B.2: sağı doldurduktan sonra sola alt sıraya geçecek
                counter = 0
                for i in range(0, (20 - biletBaslangic)):   # önce sağ taraf dolana kadar rezerve edilir
                    counter = counter + 1   # counter kaç bilet rezerve edildini tutuyor
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                    print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
                siraBaslangic = siraBaslangic + 1  # alt satıra, sol tarafa geçildi
                biletBaslangic = 4
                if (biletNo-counter)<=5:    # Durum B.2.1: sol tarafta kalacak
                    for i in range(0, (biletNo - counter)):  # biletNo-counter=kaç tane daha rezerve edilmesi gereken bilet var
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                else:                       # Durum B.2.2: sağ tarafa geçecek
                    for i in range(0, 5):       # önce sol taraf doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                    biletBaslangic=15           # sağ tarafa geçilir
                    for i in range(0,(biletNo-counter-5)):# sağ taraf doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")

def rezerveKategori_3(salon, biletNo):  #3. kategori için rezervasyon işlemini yapar
    counter = 20
    # ----EN SON HANGİ KOLTUK REZERVE EDİLMİŞ ONU BULMAK İÇİN----
    for i in salon[19:9:-1]:    # son rezerveyi bulmak için en son sırada sağdan sola doğru x değeri arar, bulamazsa üst sıraya geçer
        counter = counter - 1   # counter sıra indisini tutar
        a = i.rfind("x")
        if a>=15:               # 4. kategori sağ taraftan x algılandı
            a=salon[counter][5:15].rfind("x")
            if a<0:             # demek ki bu sırada 3. kategori boş,aramaya üst sıradan devam edilir
                continue
            else:               # 3. kategori bu sırada son koltuk bulundu,döngüden çıkılır
                a=a+5
                break
        elif a<=4:              # 4. kategori sol tarafan algılandı, 3. kategori bu sırada boş, aramaya üst sıradan devam edilir
            continue
        elif a>=5 and a<=14:    # bu sırada 4. kategori sağ taraftan x algılanmadı,  3. kategori için aranan son koltuk bulundu, döngüden çıkıldı
            break
    # ----EN SON REZERVE EDİLEN KOLTUĞA GÖRE REZERVASYON İŞLEMİNE BAŞLANACAK SIRA VE KOLTUK İNDİSLERİNİN BELİRLENMESİ----
    if (a < 0):      # ilk rezervasyon işlemi
        biletBaslangic = 5
        siraBaslangic = 10
    elif (a == 14):  # en son sıranın sonuncu koltuğu rezerve edildiyse bilet baslangıç değeri bir sonraki sıranın ilk koltuğu olur
        biletBaslangic = 5
        siraBaslangic = counter + 1
    else:            # en son rezerve edilen koltuktan bir sonraki değer bilet başlangıç değerine atılır
        biletBaslangic = a + 1
        siraBaslangic = counter
    print("-->Rezerve edilen koltuklar:",end="")
        # ----BİLET REZERVE KISMI----
    if (biletBaslangic + biletNo > 15):  # Durum A: rezerve edilecek koltukların bir kısmı alt satıra geçecek
        counter = 0
        for i in range(0, (15 - biletBaslangic)):
            counter = counter + 1           # counter kaç bilet rezerve edildiğini tutuyor
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
        siraBaslangic = siraBaslangic + 1   # alt satıra geçildi
        biletBaslangic = 5
        for i in range(0, (biletNo - counter)):# biletNo-counter=kaç tane daha rezerve edilmesi gereken bilet var
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
    else:                                # Durum B: aynı sıra içinde kalacak
        for i in range(biletNo):
            salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
            print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")

def rezerveKategori_4(salon, biletNo):  #4. kategori için rezervasyon işlemini yapar
    counter = 20
    # ----EN SON HANGİ KOLTUK REZERVE EDİLMİŞ ONU BULMAK İÇİN----
    for i in salon[19:9:-1]:    # son rezerveyi bulmak için en son sırada sağdan sola doğru x değeri arar, bulamazsa üst sıraya geçer
        counter = counter - 1   # counter sıra indisini tutar
        a = i.rfind("x")
        if a >= 15:             # sağ tarafta kalınan yeri buldu, döngüden çıkılır
            break
        elif a>=5:              # 3. kategorinin x'ini tespit etti,4. kategori sol taraf için bakması lazım
            a=salon[counter][0:5].find("x")
            if counter!=0 and a<0:      # bu sırada hiç 4. kategoriden rezerve yapılmamış üst sıraya geçilir
                continue
            elif counter!=0 and a<=4:   # 4. kategoride sol tarafta nerede kalındığını buldu, döngüden çıkılır 
                break
            elif counter==0 and a<0:    # daha önce 4. kategoriden hiç rezerve yapılmamış->ilk rezerve işlemi
                break
        elif a<=4 and a>=0:     # sağ taraf boş solda rezerve yapılmış koltuk buldu, döngüden çıkılır
            break
    # ----EN SON REZERVE EDİLEN KOLTUĞA GÖRE REZERVASYON İŞLEMİNE BAŞLANACAK SIRA VE KOLTUK İNDİSLERİNİN BELİRLENMESİ----
    if a < 0:      # ilk rezervasyon işlemi
        biletBaslangic = 4
        siraBaslangic = 10
    elif a == 19:  # sıranın en son koltuğunda kaldıysa alt sıraya geçiş yapılır
        biletBaslangic = 4
        siraBaslangic = counter + 1
    elif a >= 15:  # sağ tarafta kaldıysa
        biletBaslangic = a + 1
        siraBaslangic = counter
    else:          # sol tarafta kaldıysa
        a = salon[counter].find('x')  # solda kalınan yer bulunur
        if a > 0:       # demek ki solda hala bilet rezerve edilecek yer var
            biletBaslangic = a - 1
            siraBaslangic = counter
        else:           # sol tamamen dolu sağ kısma geçiş sağlanır
            biletBaslangic = 15
            siraBaslangic = counter
    print("-->Rezerve edilen koltuklar:",end="")
        # --------------BİLET REZERVE KISMI--------------"""
    if biletBaslangic < 5:  # ---DURUM A:SOLDAN BAŞLAYAN KISIM
            if biletBaslangic - biletNo >= -1:  # Durum A.1: rezervasyon sağ tarafa geçmeden, sadece sol tarafta yapılacak
                for i in range(biletNo):
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                    print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
            else:                               # Durum A.2: rezervasyonun bir kısmı sağ tarafı da dolduracak
                biletCounter = 0
                for i in range(0, biletBaslangic + 1):  # sol tarafı doldurmak için 
                    biletCounter = biletCounter + 1
                    if (biletBaslangic - i) != 0:       # sıranın en başındaki koltuğa gelene kadar sol tarafı doldurur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                    else:                               # sıranın en başındaki koltuğun rezerve edilmesi için
                        salon[siraBaslangic] = "x" + salon[siraBaslangic][1:]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                biletBaslangic = 15  # sağ kısma geçildi
                kalanBilet=biletNo-biletCounter
                if biletBaslangic+kalanBilet<=20: # Durum A.2.1: rezervasyon sırasında sol alta, yeni sıraya geçmeyecek
                    for i in range(0, kalanBilet):          # sağ taraf bilet sayısı kadar rezerve edilir
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic+1+i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
                else:                            # Durum A.2.2: rezervasyon sırasında sol alta yeni sıraya geçecek
                    for i in range(0, (20-biletBaslangic)): # önce sağ taraf doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic+1+i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
                    biletBaslangic=4                        # alt sıraya, sol tarafa geçilir
                    siraBaslangic=siraBaslangic+1
                    for i in range(kalanBilet-5):           # sol kısım bilet sayısı kadar rezerve edilir
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
    else:   # ---DURUM B: SAĞDAN BAŞLAYAN KISIM
            if biletBaslangic + biletNo < 20:  # Durum B.1: sol alta geçmeden sadece sağ taraftan rezervasyon yapacak                         
                for i in range(0, biletNo):         # sağ kısım bilet sayısı kadar doldurulur
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                    print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")
            else:                                   # Durum B.2: sağı doldurduktan sonra sola alt sıraya geçecek
                counter = 0
                for i in range(0, (20 - biletBaslangic)):    # önce sağ taraf dolana kadar rezerve edilir
                    counter = counter + 1  # counter kaç bilet rezerve edildiğini tutuyor
                    salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                    print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")

                siraBaslangic = siraBaslangic + 1  # alt satıra, sol tarafa geçildi
                biletBaslangic = 4
                if (biletNo-counter)<=5:    # Durum B.2.1: sol tarafta kalacak
                    for i in range(0, (biletNo - counter)):  # biletNo-counter=kaç tane daha rezerve edilmesi gereken bilet var
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                else:                       # Durum B.2.2: sağ tarafa geçecek
                    for i in range(0, 5):       # önce sol taraf doldururlur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic - i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 - i):]
                        print(f"({siraBaslangic+1},{biletBaslangic-i+1})",end="")
                    biletBaslangic=15           # sağ tarafa geçilir
                    for i in range(0,(biletNo-counter-5)):# sağ taraf doldurulur
                        salon[siraBaslangic] = salon[siraBaslangic][:(biletBaslangic + i)] + "x" + salon[siraBaslangic][(biletBaslangic + 1 + i):]
                        print(f"({siraBaslangic+1},{biletBaslangic+i+1})",end="")

def ciroHesaplama():    # kategoriler için ayrı ve toplam ciroyu bastırır
    global toplamCiro
    toplam=0
    for i in range(4): 
        print(f"{i}. kategoriden elde edilen gelir:{toplamCiro[i]}")
        toplam+=toplamCiro[i] 
    print("Toplam ciro:",toplam )
   
def ucretHesapla(biletSayisi,kategoriNumarasi): # ücret,indirim,net tutar bilgilerini hesaplar
    global ucretler 
    global liste1
    global liste2
    global liste3
    global liste4
    global toplamCiro
    global toplamCiro_genel
    i=[]
    if kategoriNumarasi==1:      # kategori numarasına göre indirim bilgisini alır
        for x in range(0,3):
            list=[]     
            for y in liste1[x]:
                if y=='M':
                    y=5 
                list.append(int(y))
            i.append(list)
    elif kategoriNumarasi==2:   
        for x in range(0,3):
            list=[]     
            for y in liste2[x]:
                if y=='M':
                    y=5 
                list.append(int(y)) 
            i.append(list)
    elif kategoriNumarasi==3: 
        for x in range(0,3):
            list=[]     
            for y in liste3[x]:
                if y=='M':
                    y=5 
                list.append(int(y))
            i.append(list)
    else:                    
        for x in range(0,3):
            list=[]     
            for y in liste4[x]:
                if y=='M':
                    y=5 
                list.append(int(y))
            i.append(list)
    print("\n--> Alınan bilet adeti:",biletSayisi)
    tutar=biletSayisi*int(ucretler[kategoriNumarasi-1]) #tutarı hesaplar
    print("--> Toplam tutar: ",tutar)
    if biletSayisi<int(i[0][1]):            # bilet sayısına göre indirim miktarını ve net tutarı hesaplar
            print("--> İndirim miktarı: %0")
            print("--> Net tutar:",tutar)
    elif biletSayisi<=int(i[0][2]):         # bilet sayısına göre indirim miktarını ve net tutarı hesapla
            indirim=int(i[0][3])
            print("--> İndirim miktarı: %",int(i[0][3]))
            tutar=tutar-((indirim*tutar)/100)
            print("--> Net tutar: ",tutar)
    elif biletSayisi<=int(i[1][2]):         # bilet sayısına göre indirim miktarını ve net tutarı hesapla
            indirim=int(i[1][3])
            print("--> İndirim miktarı: %",indirim)
            tutar=tutar-((indirim*tutar)/100)
            print("--> Net tutar:",tutar)
    else:                                   # bilet sayısına göre indirim miktarını ve net tutarı hesapla
            indirim=int(i[2][3])
            print("--> İndirim miktarı: %",indirim)
            tutar=tutar-((10*tutar)/100)
            print("--> Net tutar: ",tutar)
    toplamCiro[kategoriNumarasi-1]+=tutar   # tutarı ilgili kategorinin cirosuna ekler

with open("170421844.txt","r") as dosya:    # indirim dosyasından verileri çeker
    dosya.seek(2)
    biletMax=dosya.readline()   # max bilet ücretini alır
    ucretler=[]
    for i in range(8,30,7):     # ücret bilgilerinin alınması için
        dosya.seek(i)
        ucretler.append((dosya.readline().splitlines()))
    x=[]
    for y in ucretler:  # liste içinde liste ataması olmasın diye-419. satır liste döndürür liste içine liste elemanı ekler:[["1"],["2"],["3"]] gibi
        x.append(y[0])
    ucretler=x          # böylece liste içine string elemanı eklendi:["1","2","3"] gibi
    liste1=[]   # birinci kategori için indirim bilgilerini tutar
    for i in range(0,3):
        a=dosya.readline()
        a=a[:-1]    # \n kısmını almamak için
        liste1.append(a.split("-"))
    liste2=[]   # ikinci kategori için indirim bilgilerini tutar
    for i in range(0,3):
        a=dosya.readline()
        a=a[:-1]    # \n kısmını almamak için
        liste2.append(a.split("-"))
    liste3=[]   # üçüncü kategori için indirim bilgilerini tutar
    for i in range(0,3):
        a=dosya.readline()
        a=a[:-1]    # \n kısmını almamak için
        liste3.append(a.split("-"))
    liste4=[]   # dördüncü kategori için indirim bilgilerini tutar
    for i in range(0,3):
        a=dosya.readline()
        a=a[:]      # dosya sonu olduğunda burada \n yok
        liste4.append(a.split("-"))

"""#------------------------------------------------------------------------------------------------------------------------"""
salon = []
for i in range(0, 20):  # salonu oluşturur
    salon.append("--------------------")
kalanBilet=[100,100,100,100]
toplamCiro=[0,0,0,0]
"""#-------------------------------------------------------ANA MENÜ---------------------------------------------------------"""
girilen = 5
while girilen != 0:
    girilen = input(("****************\n**  ANA MENÜ  **\n1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4. Toplam Ciro\n0. ""Çıkış\n****************\nSeçiminiz: "))
    match girilen:
        case "1":
            rezervasyon(salon)
        case "2":
            salonYazdir(salon)
        case "3":
            yeniEtkinlik(salon)
        case "4":
            ciroHesaplama()
        case "0":
            break
        case _:  #default
            print("Geçerli bir seçim yapmadınız, tekrar deneyin")
        