import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Membaca gambar asli
F = np.array(Image.open('Masukan lokasi gambar disini!').convert('L'))

# Mendapatkan dimensi gambar
tinggi, lebar = F.shape

# Membuat array hasil filter median
G = np.zeros_like(F)

# Melakukan filter median
for baris in range(1, tinggi - 1):
    for kolom in range(1, lebar - 1):
        # Mengambil nilai piksel dan tetangga
        data = [
            F[baris-1, kolom-1], F[baris-1, kolom], F[baris-1, kolom+1],
            F[baris, kolom-1], F[baris, kolom], F[baris, kolom+1],
            F[baris+1, kolom-1], F[baris+1, kolom], F[baris+1, kolom+1]
        ]
        # Mengurutkan data dan mengambil nilai median
        data.sort()
        G[baris, kolom] = data[4]

# Menampilkan gambar sebelum dan sesudah filter
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Menampilkan gambar asli
ax[0].imshow(F, cmap='gray')
ax[0].set_title('Gambar Sebelum Filter')
ax[0].axis('on')

# Menampilkan gambar hasil filter median
ax[1].imshow(G, cmap='gray')
ax[1].set_title('Gambar Setelah Filter Median')
ax[1].axis('off')

plt.show()
