import numpy as np
import matplotlib.pyplot as plt

# Asumsi parameter
tahun_awal = 2018
tahun_akhir = 2021
populasi = 1000000  # populasi awal
tingkat_kematian_awal = 0.008  # tingkat kematian 0.8% sebelum pandemi
peningkatan_kematian_tahunan = 0.0005  # peningkatan 0.05% per tahun pasca-pandemi

# Tahun dan skenario simulasi
tahun = np.arange(tahun_awal, tahun_akhir + 1)
angka_kematian_sebelum_pandemi = populasi * tingkat_kematian_awal

# Skenario: Angka kematian pasca-COVID
angka_kematian_pasca_covid = []
tingkat_kematian = tingkat_kematian_awal

for t in tahun:
    if t > tahun_awal:
        tingkat_kematian += peningkatan_kematian_tahunan
    angka_kematian_pasca_covid.append(populasi * tingkat_kematian)

# Visualisasi hasil
plt.figure(figsize=(10, 6))
plt.plot(tahun, [angka_kematian_sebelum_pandemi] * len(tahun), label="Angka Kematian Sebelum Pandemi", linestyle="--")
plt.plot(tahun, angka_kematian_pasca_covid, label="Angka Kematian Pasca-COVID", color="red")
plt.xlabel("Tahun")
plt.ylabel("Angka Kematian (Per Tahun)")
plt.title("Simulasi Peningkatan Angka Kematian Pasca-COVID")
plt.legend()
plt.grid(True)
plt.show()
