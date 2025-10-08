import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==========================
# Judul Utama
# ==========================
st.set_page_config(page_title="LMS Fisika Inti", page_icon="⚛️", layout="wide")

st.title("⚛️ LMS Fisika Inti")
st.write(
    """
    Selamat datang di platform pembelajaran interaktif **Fisika Inti**!  
    Yuk, pelajari konsep dasar energi nuklir dengan cara yang seru dan mudah dipahami 💡
    """
)

# ==========================
# Navigasi Sidebar
# ==========================
menu = st.sidebar.radio(
    "📚 Pilih Menu:",
    ["🏠 Beranda", "📘 Materi", "📊 Visualisasi", "🧩 Kuis", "ℹ️ Tentang"]
)

# ==========================
# BERANDA
# ==========================
if menu == "🏠 Beranda":
    st.header("Selamat Datang di LMS Fisika Inti 👋")
    st.write(
        """
        Fisika inti adalah cabang ilmu fisika yang mempelajari **struktur dan sifat-sifat inti atom**
        serta interaksi antar partikel di dalamnya.  
        Ilmu ini menjadi dasar bagi teknologi nuklir, baik dalam bidang **energi, kesehatan,** maupun **penelitian ilmiah.**

        Di LMS ini, kamu akan mempelajari dua submateri utama:
        - 🌱 **Manfaat dan Dampak Energi Nuklir**  
        - ☀️ **Prinsip Reaksi Fisi dan Fusi**
        """
    )

# ==========================
# MATERI
# ==========================
elif menu == "📘 Materi":
    st.header("📘 Materi Fisika Inti")

    # Submateri 1
    st.subheader("1️⃣ Manfaat dan Dampak Energi Nuklir")
    st.markdown(
        """
        ### 🔹 Manfaat Energi Nuklir
        1. **Pembangkit Listrik Tenaga Nuklir (PLTN)**  
           Energi nuklir digunakan untuk menghasilkan listrik dalam jumlah besar dengan emisi karbon yang rendah.

        2. **Bidang Kesehatan**  
           Radiasi nuklir digunakan untuk **radioterapi** dalam menghancurkan sel kanker serta **diagnosis penyakit** menggunakan alat seperti **PET Scan**.

        3. **Bidang Industri**  
           Digunakan untuk **uji nondestruktif (NDT)** dalam memeriksa kualitas material tanpa merusaknya, serta sterilisasi alat medis.

        4. **Bidang Pertanian dan Pangan**  
           Radiasi membantu memperpanjang masa simpan bahan makanan dan mengendalikan hama menggunakan teknik **serangga mandul**.

        5. **Penelitian dan Teknologi**  
           Digunakan untuk penelitian reaksi inti, fisika partikel, dan pengembangan sumber energi masa depan.
        """
    )

    st.markdown(
        """
        ### ⚠️ Dampak Energi Nuklir
        1. **Limbah Radioaktif**  
           Limbah dari reaktor nuklir sangat berbahaya dan membutuhkan penyimpanan jangka panjang dengan pengawasan ketat.

        2. **Risiko Kecelakaan Nuklir**  
           Contohnya tragedi **Chernobyl (1986)** dan **Fukushima (2011)** yang berdampak besar terhadap manusia dan lingkungan.

        3. **Isu Keamanan Global**  
           Teknologi nuklir bisa disalahgunakan untuk **membuat senjata pemusnah massal**.

        4. **Biaya Operasional Tinggi**  
           Pembangunan dan perawatan PLTN sangat mahal serta memerlukan sumber daya manusia berkompeten.
        """
    )

    st.markdown("---")

    # Submateri 2
    st.subheader("2️⃣ Prinsip Reaksi Fisi dan Fusi")
    st.markdown(
        """
        ### ⚛️ Reaksi Fisi
        - **Fisi** adalah proses **pembelahan inti atom berat menjadi dua inti yang lebih kecil**, disertai pelepasan energi besar dan beberapa neutron.  
        - Terjadi pada inti berat seperti **Uranium-235** dan **Plutonium-239**.  
        - Energi panas yang dihasilkan digunakan di **reaktor nuklir** untuk menggerakkan turbin pembangkit listrik.

        **Ciri-ciri Fisi:**
        - Terjadi pada inti berat  
        - Menghasilkan dua inti lebih ringan  
        - Melepaskan neutron dan energi panas  
        - Dapat memicu **reaksi berantai (chain reaction)**
        """
    )

    st.markdown(
        """
        ### 🌞 Reaksi Fusi
        - **Fusi** adalah proses **penggabungan dua inti ringan menjadi satu inti yang lebih berat**, disertai pelepasan energi sangat besar.  
        - Reaksi ini merupakan **sumber energi matahari dan bintang**.  
        - Contoh: **Deuterium + Tritium → Helium + Energi**

        **Ciri-ciri Fusi:**
        - Terjadi pada inti ringan seperti **Hidrogen dan Deuterium**  
        - Membutuhkan suhu dan tekanan sangat tinggi  
        - Menghasilkan energi lebih besar daripada fisi  
        - Limbah radioaktifnya lebih sedikit
        """
    )

    st.markdown(
        """
        ### 🔬 Perbandingan Fisi dan Fusi

        | Aspek | Fisi | Fusi |
        |--------|------|------|
        | Jenis Inti | Berat (U, Pu) | Ringan (H, D) |
        | Energi Dihasilkan | Besar | Sangat besar |
        | Limbah Radioaktif | Ada | Sedikit |
        | Aplikasi | PLTN | Energi Matahari, Reaktor Eksperimental |
        """
    )

# ==========================
# VISUALISASI
# ==========================
elif menu == "📊 Visualisasi":
    st.header("📊 Visualisasi Energi Ikatan per Nukleon")

    A = np.arange(1, 240)
    E = 8.8 * (1 - np.exp(-A / 20)) - 0.1 * np.log(A + 1)

    fig, ax = plt.subplots()
    ax.plot(A, E, label="Energi Ikatan per Nukleon (simulasi)")
    ax.axvline(56, linestyle="--", color='r', label="Fe-56 (Paling Stabil)")
    ax.set_xlabel("Nomor Massa (A)")
    ax.set_ylabel("Energi Ikatan (MeV/nukleon)")
    ax.legend()
    st.pyplot(fig)

    st.info(
        "Grafik menunjukkan bahwa inti ringan cenderung mengalami **fusi**, sedangkan inti berat cenderung mengalami **fisi**."
    )

# ==========================
# KUIS
# ==========================
elif menu == "🧩 Kuis":
    st.header("🧠 Kuis Fisika Inti")

    skor = 0

    q1 = st.radio("1️⃣ Energi PLTN berasal dari proses apa?", ["A. Fusi", "B. Fisi", "C. Ionisasi"])
    if q1 == "B. Fisi":
        skor += 1
        st.success("✅ Benar! Energi PLTN berasal dari reaksi fisi Uranium-235.")
    elif q1:
        st.error("❌ Kurang tepat, bro. Coba cek lagi bagian reaksi fisi!")

    q2 = st.radio("2️⃣ Energi matahari dihasilkan melalui reaksi apa?", ["A. Fisi", "B. Fusi", "C. Disosiasi"])
    if q2 == "B. Fusi":
        skor += 1
        st.success("✅ Mantap! Energi matahari berasal dari reaksi fusi Hidrogen.")
    elif q2:
        st.error("❌ Kurang tepat, baca lagi bagian reaksi fusi ya!")

    q3 = st.radio("3️⃣ Dampak negatif energi nuklir yang paling serius adalah ...", ["A. Limbah radioaktif", "B. Suhu tinggi", "C. Tekanan rendah"])
    if q3 == "A. Limbah radioaktif":
        skor += 1
        st.success("✅ Yap! Limbah radioaktif memang perlu pengelolaan khusus.")
    elif q3:
        st.error("❌ Kurang tepat, coba ingat bagian dampak energi nuklir!")

    if st.button("💯 Lihat Skor Akhir"):
        st.info(f"Skor kamu: **{skor}/3**")
        if skor == 3:
            st.balloons()
            st.success("🔥 Keren banget bro! Kamu udah jago di Fisika Inti!")
        elif skor == 2:
            st.warning("✨ Bagus! Masih bisa lebih baik lagi 💪")
        else:
            st.error("😅 Belum maksimal nih, coba baca ulang materinya ya!")

# ==========================
# TENTANG
# ==========================
elif menu == "ℹ️ Tentang":
    st.header("ℹ️ Tentang LMS Fisika Inti")
    st.write(
        """
        Aplikasi ini dibuat dengan ❤️ menggunakan **Streamlit** untuk membantu pembelajaran Fisika Inti secara interaktif.  
        Fitur yang tersedia:
        - 📘 Materi lengkap dan interaktif  
        - 📊 Visualisasi energi ikatan nukleon  
        - 🧩 Kuis latihan dengan umpan balik langsung  
        - 🌐 Siap dijalankan di **Streamlit Cloud** atau **GitHub Codespaces**
        """
    )
