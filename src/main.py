import pandas as pd
from aco_algoritmasi import ACO

# Şehirler arası mesafeleri yükle
mesafeler = pd.read_csv("data/sehirler_arasi_mesafeler.csv", index_col=0).values

# Teslimat siparişlerini yükle
siparisler = pd.read_csv("data/teslimat_siparisleri.csv")

# ACO algoritmasını başlat
aco = ACO(mesafeler, karinca_sayisi=10, alpha=1, beta=2, rho=0.5, Q=100)

# Algoritmayı çalıştır ve en iyi rota ile en iyi uzunluğu al
en_iyi_rota, en_iyi_uzunluk = aco.calistir()

# Sonuçları yazdır
print("En İyi Rota:", en_iyi_rota)
print("En İyi Uzunluk (Mesafe):", en_iyi_uzunluk)
