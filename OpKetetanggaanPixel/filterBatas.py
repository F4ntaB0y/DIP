import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar dalam mode grayscale
F = cv2.imread('Masukan lokasi gambar disini!', cv2.IMREAD_GRAYSCALE)

# Menyalin gambar asli ke G
G = F.copy()
tinggi, lebar = F.shape

# Melakukan filter batas
for baris in range(1, tinggi - 1):
    for kolom in range(1, lebar - 1):
        # Mengambil piksel tetangga (3x3 tanpa piksel pusat)
        tetangga = [
            F[baris-1, kolom-1], F[baris-1, kolom], F[baris-1, kolom+1],
            F[baris, kolom-1],                    F[baris, kolom+1],
            F[baris+1, kolom-1], F[baris+1, kolom], F[baris+1, kolom+1]
        ]

        min_piksel = min(tetangga)
        maks_piksel = max(tetangga)

        if F[baris, kolom] < min_piksel:
            G[baris, kolom] = min_piksel
        elif F[baris, kolom] > maks_piksel:
            G[baris, kolom] = maks_piksel
        else:
            G[baris, kolom] = F[baris, kolom]

# Menampilkan gambar asli dan hasil filter batas berdampingan
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(F, cmap='gray')
plt.title('Gambar Asli')
plt.axis('on')

plt.subplot(1, 2, 2)
plt.imshow(G, cmap='gray')
plt.title('Setelah Filter Batas')
plt.axis('on')

plt.tight_layout()
plt.show()
