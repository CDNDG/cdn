import os

# Ayarlar
CDN_BASE_URL = "https://cdn.jsdelivr.net/gh/CDNDG/cdn/icons/skillicons/"

# PNG dosyalarını bul
png_files = [f for f in os.listdir('.') if f.lower().endswith('.png')]

# Geçerli boyutta olanları filtrele (isteğe bağlı kontrol)
valid_icons = []
for file in png_files:
    try:
        from PIL import Image
        img = Image.open(file)
        if img.size == (32, 32):
            valid_icons.append(file)
        else:
            print(f"{file} atlandı (32x32 değil)")
    except:
        print(f"{file} okunamadı")

# HTML içeriği
html = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Skillicons Galeri</title>
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
      width: 32px;
      height: 32px;
      display: block;
      transition: transform 0.2s ease;
    }}
    .gallery a img:hover {{
      transform: scale(1.5);
      z-index: 10;
    }}
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

# Görselleri CDN yoluyla ekle
for file in valid_icons:
    cdn_path = f"{CDN_BASE_URL}{file}"
    html += f'    <a href="{cdn_path}" download title="{file}"><img src="{cdn_path}" alt="{file}"></a>\n'

html += '''  </div>

  <!-- Lightbox -->
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

# HTML dosyasını kaydet
with open("skillicons_galeri.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"{len(valid_icons)} ikon işlendi. 'skillicons_galeri.html' oluşturuldu (CDN ile).")
