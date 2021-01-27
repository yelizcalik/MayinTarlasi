import numpy as np  # numpy kütüphanesi çağırıldı
import random  # random komutunun kullanılması için random kütüphanesi çağırıldı


def Tarla():  # Tarla fonksiyonu oluşturuldu

    tarla = np.zeros((10, 10), tuple)  # tarla için 0 matrisi oluşturuldu
    m = 0  # mayın sayısını belirlemek için mayın değişkeni oluşturuldu
    b = 80

    while (m < 20):  # mayın sayısı 10 olana kadar devam etmesi için döngü oluşturuldu
        sr = random.randint(0, 9)  # random satır
        sn = random.randint(0, 9)  # random sütun
        if (tarla[sr, sn] == 0):  # tarlaya mayın döşemeye başlandı
            tarla[sr, sn] = "X"  # random olarak tarlanın bir yerine mayın kondu
            m += 1  # mayın sayısı bir artırıldı

    x = 0  # satır taraması için değişken oluşturuldu

    # Komşu taraması yapılacak. Köşeler hariç her noktanın 8 tane komşusu var.
    # Eğer bakılan noktada mayın yoksa etraftaki mayınlar taranacak ve bulunan mayın
    # sayısına göre o kutucuğun değeri bir artacak
    # dolayısıyla başta 0 olan noktaların hepsi komşularındaki mayın sayısına göre değer değiştirecek.
    # mayın olan noktalar es geçilecek.
    # matrisin dışına çıkılmaması için her noktada satır ve sütun değerlendirmesi yapılacak.
    # Örneğin 3,3 noktasındayız. While içerisinde bu noktanın 8 komşusu
    # taranacak.

    while(10 > x > -1):  # satırlar 0'dan küçük 9'dan büyük olamayacağı için 10 ile -1 arasında döngü oluşturuldu
        y = 9  # sütun gezebilmek için değişken atandı
        while(10 > y > -1):  # sütunlar 10 ile -1 arasında olacak şekilde döngü oluşturuldu
            if(tarla[x, y] != 'X' and x - 1 > -1 and y - 1 > -1 and tarla[x - 1, y - 1] == 'X'):
                tarla[x, y] += 1
            if(tarla[x, y] != 'X' and x - 1 > -1 and tarla[x - 1, y] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and x - 1 > -1 and 10 >
                    y + 1 and tarla[x - 1, y + 1] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and y - 1 > -1 and tarla[x, y - 1] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and 10 > y + 1 and tarla[x, y + 1] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and 10 > x + 1 and y -
                    1 > -1 and tarla[x + 1, y - 1] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and 10 > x + 1 and tarla[x + 1, y] == 'X'):
                tarla[x, y] += 1
            if (tarla[x, y] != 'X' and 10 > x + 1 and 10 >
                    y + 1 and tarla[x + 1, y + 1] == 'X'):
                tarla[x, y] += 1
            y -= 1  # yeni sütun için sütun değişkeni bir azaltıldı
        x += 1  # yeni satır için satır değişkeni bir artırıldı
    return tarla


def Bos():  # Bos kutucukları saymada kullanmak için baştan sayı belirlendi
    bos = 90  # 10 mayın olduğundan kalan kutu sayısı 90 olduğundan bos değişkenine 90 atandı
    return bos
