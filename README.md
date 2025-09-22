import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Judul Aplikasi
st.title("LMS Fisika Inti 🔬⚛️")
st.write("Selamat datang di Learning Management System Fisika Inti. Yuk belajar bareng!")

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu", ["📖 Materi", "📊 Visualisasi", "📝 Kuis", "ℹ️ Tentang"])

# ---------------- MATERI ----------------
if menu == "📖 Materi":
    st.header("Materi Fisika Inti")

    st.subheader("1. Manfaat dan Dampak Energi Nuklir")
    st.write("""
    **Manfaat Energi Nuklir:**
    - Sebagai pembangkit listrik tenaga nuklir (PLTN) yang mampu menghasilkan energi dalam jumlah besar.
    - Digunakan dalam bidang kedokteran, seperti radioterapi untuk pengobatan kanker.
    - Pemanfaatan dalam industri, misalnya untuk uji nondestruktif (NDT).
    - Dalam bidang pertanian, digunakan untuk mengendalikan hama dengan teknik serangga mandul.
    - Menjadi alternatif energi dengan emisi karbon rendah dibandingkan bahan bakar fosil.

    **Dampak Energi Nuklir:**
    - Limbah radioaktif yang berbahaya dan memerlukan penanganan khusus.
    - Potensi kecelakaan reaktor yang bisa menimbulkan bencana besar (contoh: Chernobyl, Fukushima).
    - Isu keamanan terkait penyalahgunaan teknologi nuklir untuk senjata.
    - Tingginya biaya pembangunan dan perawatan PLTN.
    """)

    st.subheader("2. Prinsip Reaksi Fisi dan Fusi")
    st.write("""
    **Reaksi Fisi:**
    - Fisi adalah proses pemecahan inti berat (contoh: Uranium-235 atau Plutonium-239) menjadi inti lebih ringan.
    - Menghasilkan neutron bebas yang bisa memicu reaksi berantai pada reaktor nuklir.
    - Energi dilepas karena perubahan energi ikatan nuklir yang besar.
    - Digunakan dalam PLTN dan juga menjadi prinsip dasar bom atom.

    **Reaksi Fusi:**
    - Fusi adalah penggabungan inti ringan (misalnya Deuterium + Tritium) menjadi inti lebih berat (Helium).
    - Menghasilkan energi sangat besar dan merupakan sumber energi utama pada matahari dan bintang.
    - Energi fusi jauh lebih besar dibandingkan fisi, dan limbahnya relatif lebih aman.
    - Tantangan: membutuhkan temperatur & tekanan ekstrem untuk mengatasi tolakan Coulomb antar inti.
    - Fusi berpotensi menjadi sumber energi masa depan yang lebih bersih.
    """)

# ---------------- VISUALISASI ----------------
elif menu == "📊 Visualisasi":
    st.header("Visualisasi Energi Ikatan per Nukleon")

    A = np.arange(1, 240)  # nomor massa
    E = 8.8 * (1 - np.exp(-A/20)) - 0.1*np.log(A+1)  # simulasi energi ikatan

    fig, ax = plt.subplots()
    ax.plot(A, E, label="Energi Ikatan per Nukleon")
    ax.axvline(56, linestyle="--", color="red", label="Fe-56 (Stabil)")
    ax.set_xlabel("Nomor Massa (A)")
    ax.set_ylabel("Energi Ikatan (MeV/nukleon)")
    ax.set_title("Kurva Energi Ikatan per Nukleon")
    ax.legend()
    st.pyplot(fig)

    st.info("Grafik ini menunjukkan bahwa inti ringan cenderung mengalami fusi, sedangkan inti berat cenderung mengalami fisi.")

# ---------------- KUIS ----------------
elif menu == "📝 Kuis":
    st.header("Kuis Fisika Inti")

    # Soal 1
    with st.form("soal_1"):
        q1 = st.radio(
            "1. Apa manfaat utama energi nuklir dalam kehidupan modern?",
            [
                "Menghasilkan listrik dalam jumlah besar",
                "Mengurangi limbah industri",
                "Menggantikan semua energi terbarukan",
            ],
        )
        submit1 = st.form_submit_button("Cek Jawaban Soal 1")
    if submit1:
        if q1 == "Menghasilkan listrik dalam jumlah besar":
            st.success("Benar! PLTN mampu menghasilkan energi besar dengan emisi karbon rendah.")
        else:
            st.error("Kurang tepat, coba lagi!")

    st.markdown("---")

    # Soal 2
    with st.form("soal_2"):
        q2 = st.radio(
            "2. Reaksi fusi secara alami terjadi di ...",
            ["Reaktor Nuklir", "Matahari", "Bumi"],
        )
        submit2 = st.form_submit_button("Cek Jawaban Soal 2")
    if submit2:
        if q2 == "Matahari":
            st.success("Betul! Fusi adalah reaksi utama di matahari dan bintang.")
        else:
            st.error("Salah, coba cek kembali teori fusi!")

    st.markdown("---")

    # Soal 3
    with st.form("soal_3"):
        q3 = st.radio(
            "3. Dampak negatif dari penggunaan energi nuklir adalah ...",
            ["Limbah radioaktif", "Mengurangi polusi udara", "Meningkatkan energi bersih"],
        )
        submit3 = st.form_submit_button("Cek Jawaban Soal 3")
    if submit3:
        if q3 == "Limbah radioaktif":
            st.success("Benar! Limbah radioaktif memerlukan penanganan khusus karena sangat berbahaya.")
        else:
            st.error("Kurang tepat, baca lagi bagian dampak nuklir!")

# ---------------- TENTANG ----------------
elif menu == "ℹ️ Tentang":
    st.header("Tentang Aplikasi")
    st.write(
        """
    LMS ini dibuat menggunakan **Streamlit** untuk membantu pembelajaran Fisika Inti.  

    **Fitur:**  
    - Materi: Manfaat & Dampak Energi Nuklir, Prinsip Reaksi Fisi & Fusi  
    - Visualisasi interaktif energi ikatan per nukleon  
    - Kuis latihan interaktif  
    - Mudah di-deploy ke Streamlit Cloud  

    Dibuat untuk tujuan edukasi 🔬⚡
    """
    )
