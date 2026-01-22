import streamlit as st
from PIL import Image

# Sayfa Yapılandırması
st.set_page_config(page_title="Mehmet Utku Çimen | Portfolyo", page_icon="⚡", layout="wide")

# --- HAVADA UÇUŞAN EL ALETLERİ (GÖRSEL EFEKT) ---
st.markdown("""
    <style>
    /* Arka planı biraz koyulaştıralım ki aletler belli olsun */
    .stApp {
        background-color: #f8f9fa;
    }
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
        50% { transform: translateY(-25px) rotate(15deg); opacity: 0.5; }
        100% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
    }
    .floating-icon {
        position: fixed;
        font-size: 45px;
        animation: float 5s ease-in-out infinite;
        z-index: 0;
        pointer-events: none; /* Fareyle tıklamaya engel olmasın */
    }
    </style>
    <div class="floating-icon" style="top: 15%; left: 20%;">🛠️</div>
    <div class="floating-icon" style="top: 10%; right: 25%;">⚡</div>
    <div class="floating-icon" style="top: 65%; left: 30%;">💻</div>
    <div class="floating-icon" style="top: 80%; right: 15%;">🔧</div>
    <div class="floating-icon" style="top: 40%; left: 45%;">🔌</div>
    <div class="floating-icon" style="top: 50%; right: 40%;">⚙️</div>
    <div class="floating-icon" style="top: 25%; left: 60%;">📐</div>
    <div class="floating-icon" style="top: 75%; left: 10%;">💡</div>
    """, unsafe_allow_html=True)

# --- FOTOĞRAFI YÜKLE ---
try:
    # Dosya adının klasördekiyle aynı olduğundan emin ol (profil.jpg)
    img = Image.open("profil.jpg")
except:
    img = None 

# --- SOL PANEL (SİDEBAR) ---
with st.sidebar:
    if img:
        st.image(img, width=150)
    st.title("Profil")
    st.write("📍 Tekirdağ, Kapaklı")
    st.write("🎂 20 Yaşında")
    st.write("🎓 Elektrik-Elektronik Mezunu")
    st.divider()
    
    st.write("### 🔗 İletişim & Sosyal Medya")
    st.write("📧 [utkucmn11@gmail.com](mailto:utkucmn11@gmail.com)")
    st.write("📸 [Instagram: 59.utkucimen_](https://www.instagram.com/59.utkucimen_/)")
    st.write("💼 [LinkedIn: Utku Çimen](https://www.linkedin.com/search/results/all/?keywords=Utku%20Çimen)")
    
    st.divider()
    st.write("### Hobiler")
    st.write("🎵 Müzik Dinlemek")
    st.write("🚶 Yürüyüş Yapmak")
    st.write("🎮 Oyun Oynamak")

# --- ANA SAYFA İÇERİĞİ ---
# İçeriği bir kutu içine alalım ki aletlerin altında kalmasın
container = st.container()
with container:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Mehmet Utku Çimen")
        st.subheader("Elektrik-Elektronik Teknisyeni & Geliştirici")
        st.write("""
        Merhaba! Ben Utku. Elektrik-elektronik lise mezunuyum ve aktif olarak bu sektörde çalışıyorum. 
        Teknolojiye olan tutkumla beraber Python dünyasında kendimi geliştiriyor ve dijital çözümler üretiyorum.
        """)

    # --- PROJELER BÖLÜMÜ ---
    st.divider()
    st.header("💻 Projelerim")
    col3, col4 = st.columns(2)

    with col3:
        with st.expander("🚀 Devam Eden Çalışmalar", expanded=True):
            st.write("Şu an üzerinde çalıştığım çok özel projeler var.")
            st.warning("Bu projeler şu an için gizli tutulmaktadır. 😂")

    with col4:
        with st.expander("🛠️ Uzmanlık Alanları", expanded=True):
            st.write("- Elektrik Devre Tasarımı")
            st.write("- Elektronik Bakım & Onarım")
            st.write("- Python ile Otomasyon")

    # Alt Bilgi
    st.write("##")
    st.caption("© 2026 Mehmet Utku Çimen - Tüm Hakları Saklıdır.")


