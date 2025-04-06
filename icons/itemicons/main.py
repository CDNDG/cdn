import os
from PIL import Image

# Çıktı klasörü
output_folder = "cropped"
os.makedirs(output_folder, exist_ok=True)

# PNG dosyalarını bul
png_files = [f for f in os.listdir('.') if f.lower().endswith('.png')]

# Resimleri kırp ve yeni klasöre kaydet
for file in png_files:
    img = Image.open(file)
    if img.size == (64, 64):
        cropped = img.crop((0, 0, 45, 45))  # Sol üstten 45x45
        cropped.save(os.path.join(output_folder, file))
    else:
        print(f"{file} atlandı (boyut 64x64 değil)")

# HTML oluştur
html_content = '''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <title>Yan Yana PNG Galeri</title>
  <style>
    body {
      background-color: black;
      margin: 0;
      padding: 10px;
    }
    .gallery {
      display: flex;
      flex-wrap: wrap;
      gap: 1px;
    }
    .gallery a img {
      width: 45px;
      height: 45px;
      display: block;
    }
  </style>
</head>
<body>
  <div class="gallery">
'''

# Her resmi <a href=... download> ile ekle
for file in png_files:
    html_content += f'    <a href="{output_folder}/{file}" download><img src="{output_folder}/{file}" alt="{file}"></a>\n'

html_content += '''  </div>
</body>
</html>
'''

# HTML dosyasını kaydet
with open("galeri.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"{len(png_files)} resim işlendi. 'galeri.html' oluşturuldu.")
