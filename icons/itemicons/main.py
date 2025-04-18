import os
from PIL import Image

# Sabitler
OUTPUT_FOLDER = "cropped"
CDN_BASE_URL = "https://cdn.jsdelivr.net/gh/CDNDG/cdn/icons/itemicons/cropped/"

# Çıktı klasörü oluştur
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# PNG dosyalarını bul
png_files = [f for f in os.listdir('.') if f.lower().endswith('.png')]

# Resimleri kırp ve kaydet
for file in png_files:
    img = Image.open(file)
    if img.size == (64, 64):
        cropped = img.crop((0, 0, 45, 45))  # Sol üstten 45x45
        cropped.save(os.path.join(OUTPUT_FOLDER, file))
    else:
        print(f"{file} atlandı (64x64 değil)")

# HTML içeriği
html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>CDN Galeri</title>
  <style>
    body {{
      background-color: black;
      margin: 0;
      padding: 10px;
      font-family: sans-serif;
    }}
    .gallery {{
      display: flex;
      flex-wrap: wrap;
      gap: 1px;
    }}
    .gallery a img {{
      width: 45px;
      height: 45px;
      display: block;
      transition: transform 0.2s ease;
    }}
    .gallery a img:hover {{
      transform: scale(1.5);
      z-index: 10;
    }}
    /* Lightbox stil */
    .lightbox {{
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background-color: rgba(0, 0, 0, 0.8);
      display: none;
      justify-content: center;
      align-items: center;
    }}
    .lightbox img {{
      max-width: 80%;
      max-height: 80%;
    }}
    .lightbox:target {{
      display: flex;
    }}
  </style>
</head>
<body>
  <div class="gallery">
'''

# Görselleri HTML'e ekle
for file in png_files:
    cdn_path = f"{CDN_BASE_URL}{file}"
    html += f'    <a href="{cdn_path}" download title="{file}"><img src="{cdn_path}" alt="{file}"></a>\n'

html += '''  </div>

  <!-- Lightbox script -->
  <div id="lightbox" class="lightbox" onclick="this.style.display='none'">
    <img id="lightbox-img" src="">
  </div>
  <script>
    document.querySelectorAll('.gallery a img').forEach(img => {
      img.addEventListener('click', function(e) {
        e.preventDefault();
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        lightboxImg.src = this.src;
        lightbox.style.display = 'flex';
      });
    });
  </script>
</body>
</html>
'''

# Dosyayı kaydet
with open("galeri.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"{len(png_files)} PNG işlendi. 'galeri.html' oluşturuldu (CDN yolu ayarlı).")
