import random

class ACO:
    def __init__(self, mesafeler, karinca_sayisi, alpha, beta, rho, Q):
        self.mesafeler = mesafeler
        self.karinca_sayisi = karinca_sayisi
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.sehir_sayisi = len(mesafeler)
        self.feromonlar = [[1 for _ in range(self.sehir_sayisi)] for _ in range(self.sehir_sayisi)]

    def sonraki_sehri_sec(self, mevcut_sehir, ziyaret_edilen_sehirler):
        olasiliklar = []
        toplam_feromon = 0
        for sehir in range(self.sehir_sayisi):
            if sehir not in ziyaret_edilen_sehirler:
                feromon = self.feromonlar[mevcut_sehir][sehir] ** self.alpha
                mesafe = (1.0 / self.mesafeler[mevcut_sehir][sehir]) ** self.beta
                toplam_feromon += feromon * mesafe
                olasiliklar.append((feromon * mesafe, sehir))
        
        toplam_olasilik = sum([p[0] for p in olasiliklar])
        olasiliklar = [(p[0] / toplam_olasilik, p[1]) for p in olasiliklar]
        
        rastgele_secim = random.random()
        kümülatif_olasilik = 0.0
        for olasilik, sehir in olasiliklar:
            kümülatif_olasilik += olasilik
            if rastgele_secim < kümülatif_olasilik:
                return sehir

    def feromonlari_guncelle(self, rotalar, uzunluklar):
        for i in range(self.sehir_sayisi):
            for j in range(self.sehir_sayisi):
                self.feromonlar[i][j] *= (1 - self.rho)
        
        for rota, uzunluk in zip(rotalar, uzunluklar):
            for i in range(len(rota) - 1):
                self.feromonlar[rota[i]][rota[i + 1]] += self.Q / uzunluk

    def calistir(self, iterasyonlar=100):
        en_iyi_rota = None
        en_iyi_uzunluk = float('inf')
        
        for _ in range(iterasyonlar):
            rotalar = []
            uzunluklar = []
            
            for _ in range(self.karinca_sayisi):
                ziyaret_edilen_sehirler = [random.randint(0, self.sehir_sayisi - 1)]
                mevcut_sehir = ziyaret_edilen_sehirler[0]
                
                while len(ziyaret_edilen_sehirler) < self.sehir_sayisi:
                    sonraki_sehir = self.sonraki_sehri_sec(mevcut_sehir, ziyaret_edilen_sehirler)
                    ziyaret_edilen_sehirler.append(sonraki_sehir)
                    mevcut_sehir = sonraki_sehir
                
                uzunluk = sum(self.mesafeler[ziyaret_edilen_sehirler[i]][ziyaret_edilen_sehirler[i + 1]] for i in range(len(ziyaret_edilen_sehirler) - 1))
                rotalar.append(ziyaret_edilen_sehirler)
                uzunluklar.append(uzunluk)
                
                if uzunluk < en_iyi_uzunluk:
                    en_iyi_uzunluk = uzunluk
                    en_iyi_rota = ziyaret_edilen_sehirler
            
            self.feromonlari_guncelle(rotalar, uzunluklar)
        
        return en_iyi_rota, en_iyi_uzunluk
