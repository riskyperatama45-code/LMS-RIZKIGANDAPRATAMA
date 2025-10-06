import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# streamlit
st.title("LMS Fisika Inti")
st.write("Selamat datang di Learning Management System Fisika Inti. Yuk belajar bareng!")

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu", ["Materi"])

# MATERI
if menu == "Materi":
    st.header("Materi Fisika Inti")

    st.subheader("1. Manfaat dan Dampak Energi Nuklir")
    st.write("""
    **Manfaat dan Dampak Energi Nuklir

**Manfaat Energi Nuklir**:
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

Dampak Energi Nuklir:
1. Limbah Radioaktif
- Sangat berbahaya dan memerlukan penyimpanan khusus selama ribuan tahun.
- Jika bocor, bisa mencemari tanah, air, dan udara.
2. Risiko Kecelakaan Nuklir
- Seperti tragedi Chernobyl (1986) dan Fukushima (2011) yang menimbulkan dampak kesehatan dan lingkungan jangka panjang.
3. Isu Keamanan Global
- Teknologi nuklir bisa disalahgunakan untuk membuat senjata pemusnah massal.
- Ancaman terorisme nuklir juga jadi perhatian internasional.
4. Biaya Pembangunan dan Perawatan PLTN
- Sangat tinggi dibandingkan sumber energi lain.
- Jika tidak dikelola dengan baik, bisa jadi beban ekonomi.
    """)

    st.subheader("2. Prinsip Reaksi Fisi dan Fusi")
    st.write("""
    **Reaksi Fisi:**
    - Fisi adalah pemecahan inti berat menjadi dua (atau lebih) inti lebih ringan, biasanya disertai pelepasan neutron dan energi besar.
    **Reaksi Fusi:**
    - Fusi adalah penggabungan dua inti ringan menjadi inti yang lebih berat, juga melepaskan energi (sumber energi di bintang/matahari).
    """)
**Reaksi Fisi**
1. mekanisme & konsep
   > Langkah dasar:
     - Inti berat (contoh: Uranium-235) menyerap sebuah neutron.
     - Terbentuk compound nucleus yang berenergi tinggi → inti menjadi tak stabil → mengalami deformasi.
     - Inti terbelah menjadi dua fragmen (produk fisi) + biasanya 2–3 neutron bebas + energi kinetik fragmen + energi radiasi (gamma).
    contoh reaksi sederhana:   2H + 3H → 4He + n + 17.6 MeV
    > Sumber energi: selisih massa (massa awal > massa produk) diubah menjadi energi menurut rumus Einstein: E=mc^2.
    > Reaksi berantai: neutron bebas dapat memicu fisi inti lain → kalau rata-rata tiap fisi menghasilkan ≥1 neutron yang sukses memicu fisi lain, reaksi dapat berlanjut (→ kritikalitas).
      - Subkritis (reaksi mati), kritis (stabil), superkritis (bertambah cepat).
    > Pengendalian di reaktor:
      - Moderator (air ringan, air berat, grafit) memperlambat neutron agar probabilitas fisi meningkat (untuk isotop yang menyukai neutron lambat).
      - Control rods (mengandung boron, kadmium) menyerap neutron untuk mengatur laju reaksi.
      - Coolant (air, gas, sodium cair) mengangkut panas → dipakai untuk menghasilkan uap → turbin → listrik.
   > Perbandingan energi (angka):
      - Energi per peristiwa fisi ≈ 200 MeV.
        Konversi: 1 MeV = 1.602 × 10^−13 J →
        200 MeV ≈ 3.20 × 10^−11 J per atom yang fisi.
      - Jika seluruh 1 kg U-235 bereaksi (teoretis), energi total ≈ 8.21×10¹³ J (≈ 2.28×10⁷ kWh). (angka dibulatkan untuk ilustrasi).
   > Isu & tantangan: limbah radioaktif jangka panjang, risiko kecelakaan, proliferasi (senjata), biaya pembongkaran/penanganan.
**Reaksi Fusi**
mekanisme & konsep
   > Langkah dasar :
       - Dua inti ringan (mis. Deuterium 2H dan Tritium 3H) mendekat.
       - Mereka harus mengatasi tolakan Coulomb (tolakan elektrostatis antar muatan positif) — diperlukan energi kinetik sangat tinggi (suhu &/atau tekanan besar) atau               peluang melalui quantum tunneling.
       - Jika berhasil, inti bergabung membentuk inti lebih berat (mis. Helium) + neutron + energi.
Contoh reaksi D–T (paling mudah dicapai):
   2H + 3H → 4He + n + 17.6 MeV
   > Sumber energi: juga dari selisih massa — hasilnya dilepas sebagai energi kinetik partikel (helium, neutron).
   > Kondisi yang dibutuhkan: suhu ekstrem (10⁷–10⁸ K), atau densitas & waktu penahanan tinggi. Agar fusi memberi energi bersih, harus penuh Lawson criterion (produk kerapatan partikel × waktu konfinemen harus mencapai ambang tertentu untuk suhu tertentu).
        - Dua pendekatan praktis:
         - Magnetic confinement (mis. tokamak, stellarator) — plasma dipertahankan oleh medan magnet.
         - Inertial confinement (mis. laser, pellet) — bahan bakar dipadatkan dan dipanaskan sangat cepat sehingga reaksi terjadi sebelum bahan mengembang.
    > Perbandingan energi (angka):
       - Energi per reaksi D–T ≈ 17.6 MeV = 17.6 × 1.602 × 10^−13 J ≈ 2.82 × 10^-12 J per reaksi.
       - Karena massa reaktan (D+T) sangat kecil, energi per kg bahan bakar untuk fusi jauh besar; perkiraan kasar menunjukkan energi per kg (reaktan) dari D–T bisa sekitar 3.38×10¹⁴ J/kg (≈ 9.38×10⁷ kWh/kg). sekitar 4× lipat energi per kg dibandingkan U-235 bila semua massa benar-benar bereaksi. (angka ilustratif; praktik nyata bergantung efisiensi, fuel cycle, dll.)
   > Isu & tantangan: mencapai dan mempertahankan kondisi fusi yang stabil (plasma instabilities), material struktur yang tahan neutron dan suhu ekstrem, ketersediaan tritium (harus dibreed/rekayasa), manajemen neutron berenergi tinggi (aktivasi material).
**Perbandingan singkat & implikasi praktis**
   > Energi per reaksi: fisi (~200 MeV) > fusi D–T (~17.6 MeV) per event, tapi per massa bahan bakar fusi sering lebih “padat energi” karena reaktan lebih ringan.
   > Limbah: fisi → limbah radioaktif jangka panjang. fusi → produk radioaktif relatif lebih sedikit/lebih pendek umur, namun neutron energetik tetap dapat mengaktifkan material struktur.
   > Keamanan: reaktor fisi dapat mengalami kecelakaan (meski desain modern sangat aman) dan ada isu proliferasi; fusi tidak punya reaksi berantai seperti fisi (gampang mati sendiri) → lebih aman dari sisi runaway chain reaction, tetapi masih tantangan teknis besar.
   > Status teknologi: fisi: komersial sudah mapan (PLTN). fusi: masih eksperimen/ pilot (proyek internasional seperti tokamak besar dan percobaan inersial)."""
    )
