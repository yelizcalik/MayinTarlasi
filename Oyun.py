# kullandığımız kütüphaneler çağırıldı

import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QLabel, QGridLayout, QMessageBox
from Tarla import Bos  # imported Bos function
from Tarla import Tarla  # imported Tarla function


class Arayuz(
        QWidget):  # Created Arayuz with QWidget
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # tarla Tarla fonskiyonuna atandı dolayısıyla Tarla fonskiyonu tarla
        # şeklinde
        self.tarla = Tarla()
        # çağırılabilir ve kullanılabilir hale getirildi
        self.bos = Bos()  # bos'a tüm Bos fonksiyonu atandı
        # Tarla kontrolünü sağlamamız açısından tarla yazdırıldı
        print(self.tarla)
        # butonların yerleşimini sağlamak için button_layout
        self.buton_layout = QGridLayout()
        # isminde ızgara yerleşim şekli seçildi
        # widget kullanımı için ızgara yerleşimi seçildi
        self.widget_layout = QGridLayout()

        for buton_satir in range(0, 10):  # satırlara buton yerleşim döngüsü
            for buton_sutun in range(
                    0, 10):  # sütunlara buton yerleşim döngüsü
                buton = QToolButton()  # buton için QToolButton fonksiyonu çağırıldı
                # butonların minimum boyutu
                buton.setMinimumSize(QSize(50, 50))
                # 50*50ye ayarlandı (görünümü şekillendirmek için)
                # buton isimlerine satır ve sütun değerleri atandı
                buton.setObjectName('{:02d}'.format(
                    buton_satir * 10 + buton_sutun))
                # 10 ile çarpılmasının sebebi örneğin 1 1 değerlerini
                # 11 şekline getirebilmek dolayısıyla basamak ayırma yapılabilecek
                # butonlar buton_ozellik fonksiyonuna bağlandı
                buton.released.connect(self.buton_ozellik)
                # buton isimlerine önce satır sonra sütun değeri
                self.buton_layout.addWidget(buton, buton_satir, buton_sutun)
                # atanacak şekilde buton yerleşimleri yapıldı

         # Arayüze buton yerleşiminin yapılması için gerekli olan komutlar
        self.label = QLabel()
        self.widget_layout.addItem(self.buton_layout)
        self.widget_layout.addWidget(self.label)
        self.setLayout(self.widget_layout)

    def buton_ozellik(self):  # buton_ozellik fonksiyonu oluşturuldu
        # butonları gönderebilmek için buton_gonderme'ye sender fonksiyonu
        # atandı
        buton_gonderme = self.sender()
        # butonların değerlerini gönderip aldığımız değişkenin türü floata
        # çevrildi
        buton_ismi = float(buton_gonderme.objectName())
        # buton_isim değişkeni string'e çevrildi ve karakterlerine ayrıldı
        buton_ismi = str(buton_ismi / 10).split(".")
        # 10'a bölünmesinin sebebi değer float şeklinde yani 11.0 olarak gözükür
        # 10a bölerek 1.1 haline dönüştürülür, satır ve sütun okuması yapılabilir
        # buton_ismi stringe çevrildiğinden artık liste haline geçti
        # bu sayede satır ve sütun değerlerinin okunabileceği değişkenler
        # oluşturuldu ve ataması yapıldı

        x = int(buton_ismi[0])  # satırı veren değer listenin 0. sütununda
        y = int(buton_ismi[1])  # sütunu veren değer listenin 1. sütununda
        # butonlara tıklandığında mayın çıkıp çıkmadığı kontrol edildi
        if self.tarla[x][y] == "X":
            # Mayının çıktığı kutu kırmızıya ,
            self.sender().setStyleSheet(
                "background-color: rgba(255, 0, 0, 1); color:white; font-size:12pt;")
            # yazı tipi beyaza, boyutu da 12ye çıkarıldı
            self.sender().setText("X")  # mayının çıktığı butona X text olarak gönderildi
            msg = QMessageBox()  # game over yazısı için mesaj fonksiyonu çağırıldı ve msg oluşturuldu
            msg.setIcon(QMessageBox.Critical)  # kutu için ikon seçimi yapıldı
            # gösterilecek yazı belirlendi
            msg.setText("!!!   GAME OVER   !!!")
            msg.exec_()  # yazı çarpıya basana kadar kalsın diye exec fonksiyonu çağırıldı
            sys.exit()

        else:
            # basılan yerlerde mayın yoksa tarladaki koordinat numaraları text
            # olarak gösterildi
            self.sender().setText(str(self.tarla[x][y]))
            # mayın olmayan kutuların rengi belirlendi
            self.sender().setStyleSheet("background-color: rgba(212, 225, 87, 0.7);")
            self.bos -= 1  # Mayın olmayan kutucuk sayısı bir azaltıldı

        if (self.bos == 0):  # Eğer mayın olmayan kutucukların sayısı 0'a indiyse
            msg2 = QMessageBox()  # mesaj göstermek için messageBox fanksiyonu çağırıldı
            msg2.setIcon(QMessageBox.Warning)  # Mesaj kutusuna ikon kondu
            msg2.setText("!!!   KAZANDIN   !!!")  # Kazandın yazısı çıkarıldı
            msg2.exec_()  # Çarpıya basana kadar arayüzün açık kalması sağlandı
            sys.exit()


# Arayüz çağırma ve çalıştırma komutları
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Mayın Tarlası")
    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
