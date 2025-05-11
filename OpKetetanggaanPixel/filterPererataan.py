from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Membaca citra dan mengubah ke grayscale jika perlu
image_path = 'Masukan lokasi gambar disini!'
F = Image.open(image_path).convert('L')
F_np = np.array(F, dtype=np.float64)

tinggi, lebar = F_np.shape
G = F_np.copy()

# Proses filter pererataan
for baris in range(1, tinggi - 1):
    for kolom in range(1, lebar - 1):
        jum = (F_np[baris-1, kolom-1] + F_np[baris-1, kolom] + F_np[baris-1, kolom+1] +
               F_np[baris, kolom-1] + F_np[baris, kolom] + F_np[baris, kolom+1] +
               F_np[baris+1, kolom-1] + F_np[baris+1, kolom] + F_np[baris+1, kolom+1])
        G[baris, kolom] = jum / 9

# Konversi hasil ke uint8
G = np.clip(G, 0, 255).astype(np.uint8)

# Tampilkan gambar asli dan hasilnya
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(F_np, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Setelah Filter Pererataan')
plt.imshow(G, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
