import streamlit as st
import streamlit.components.v1 as components
import base64

# Konfigurasi Halaman (Gunakan Wide Layout)
st.set_page_config(page_title="Naval Meteorology & Oceanography Command", layout="wide")

# CSS Streamlit: Menghapus padding agar banner bisa menempel ke ujung layar (Edge-to-Edge)
st.markdown("""
    <style>
        /* Menghapus padding container bawaan Streamlit secara agresif untuk layout utuh */
        .block-container { 
            padding-top: 0rem !important; 
            padding-bottom: 0rem !important; 
            padding-left: 0rem !important; 
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        /* Penyesuaian Sidebar */
        [data-testid="stSidebar"] { background-color: #222222; color: #ffffff; }
        
        /* Menghapus ruang kosong di atas header Streamlit (jika ada) */
        header[data-testid="stHeader"] { display: none; }
    </style>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# Pastikan path ini sesuai dengan direktori Anda
image_paths = ["assetdashboard/banner_atas1.png", "assetdashboard/banner_atas2.png", "assetdashboard/banner_atas3.png"]
slides_html = ""
for path in image_paths:
    img_b64 = get_base64_image(path)
    if img_b64:
         slides_html += f'<div class="swiper-slide"><img src="data:image/png;base64,{img_b64}" /></div>\n'

# PERBAIKAN HTML & CSS KOMPONEN
carousel_html = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />
    <style>
        /* Reset margin dan padding pada body iframe agar tidak memicu scrollbar */
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden; /* Mencegah munculnya scrollbar di dalam iframe */
            background-color: #2b3b4c; /* Warna background cadangan, sesuaikan dengan tema Anda */
        }}
        .swiper {{
            width: 100%;
            height: 100vh; /* Penuhi 100% dari tinggi iframe yang kita tentukan di bawah */
        }}
        .swiper-slide {{
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .swiper-slide img {{
            width: 100%;
            height: 100%;
            
            /* KUNCI UTAMA: 
               Gunakan 'contain' agar gambar 100% UTUH dan TIDAK TERPOTONG sama sekali (mungkin akan ada ruang kosong di sisi jika rasio tidak pas).
               Ganti ke 'cover' jika Anda ingin gambar menutupi seluruh area tanpa ruang kosong (namun akan mengorbankan sedikit potongan gambar). */
            object-fit: contain; 
            display: block;
        }}
    </style>
    
    <div class="swiper mySwiper">
        <div class="swiper-wrapper">{slides_html}</div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-pagination"></div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".mySwiper", {{
            loop: true, 
            autoplay: {{ delay: 4000, disableOnInteraction: false }}, 
            pagination: {{ el: ".swiper-pagination", clickable: true }}, 
            navigation: {{ nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" }} 
        }});
    </script>
"""

# Penentuan Tinggi Iframe
# Karena menggunakan object-fit: contain, sesuaikan nilai height ini 
# agar mendekati rasio asli (aspect ratio) dari gambar banner Anda 
# agar tidak terlalu banyak ruang kosong di atas/bawah banner.
components.html(carousel_html, height=350)
