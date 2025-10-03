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
    **Manfaat dan Dampak Energi Nuklir

🔹 **Manfaat Energi Nuklir**:
1. Pembangkit Listrik Tenaga Nuklir (PLTN)
- Mampu menghasilkan listrik dalam jumlah besar dengan emisi karbon yang sangat rendah.
- Cocok untuk mengurangi ketergantungan pada energi fosil seperti batu bara dan minyak.
2. Bidang Kesehatan
- Digunakan dalam radioterapi untuk menghancurkan sel kanker.
- Isotop radioaktif dipakai sebagai tracer untuk diagnosis penyakit (misalnya PET Scan).
3. Bidang Industri
- Untuk uji nondestruktif (NDT), mengecek kualitas material tanpa merusaknya (misalnya struktur pesawat atau jembatan).
- Sterilisasi alat medis menggunakan radiasi.
4. Bidang Pertanian dan Pangan
- Teknik serangga mandul untuk mengendalikan populasi hama.
- Radiasi gamma digunakan untuk memperpanjang masa simpan bahan makanan.
5. Riset dan Teknologi
- Energi nuklir digunakan dalam penelitian reaksi inti, fisika partikel, dan pengembangan energi masa depan.
- Menjadi alternatif energi yang efisien dan berkelanjutan.

🔻 Dampak Energi Nuklir:

Limbah Radioaktif

Sangat berbahaya dan memerlukan penyimpanan khusus selama ribuan tahun.

Jika bocor, bisa mencemari tanah, air, dan udara.

Risiko Kecelakaan Nuklir

Seperti tragedi Chernobyl (1986) dan Fukushima (2011) yang menimbulkan dampak kesehatan dan lingkungan jangka panjang.

Isu Keamanan Global

Teknologi nuklir bisa disalahgunakan untuk membuat senjata pemusnah massal.

Ancaman terorisme nuklir juga jadi perhatian internasional.

Biaya Pembangunan dan Perawatan PLTN

Sangat tinggi dibandingkan sumber energi lain.

Jika tidak dikelola dengan baik, bisa jadi beban ekonomi.
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
