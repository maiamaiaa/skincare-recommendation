# 🧴 Skincare Recommendation System - Streamlit App

Aplikasi web modern berbasis NLP untuk memberikan rekomendasi produk skincare berdasarkan kebutuhan dan masalah kulit Anda.

![Skincare Recommender](https://img.shields.io/badge/Built%20with-Streamlit-red) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![ML](https://img.shields.io/badge/ML-TF%2DIDF-green)

---

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi](#instalasi)
- [Cara Menggunakan](#cara-menggunakan)
- [Struktur File](#struktur-file)
- [Pengaturan Lanjutan](#pengaturan-lanjutan)
- [Troubleshooting](#troubleshooting)

---

## ✨ Fitur Utama

### 1. **UI/UX Modern**
- 🎨 Desain gradient yang menarik dan profesional
- 📱 Layout responsif dengan Streamlit columns
- 🎭 Animasi smooth dan transisi yang elegan
- 🌈 Custom CSS untuk styling yang unik

### 2. **Input yang User-Friendly**
- 📝 Text area dengan placeholder contoh
- 🔍 Quick example buttons untuk pencarian cepat
- ✅ Validasi input kosong dengan pesan yang jelas

### 3. **Rekomendasi Produk**
- 🎯 Similarity score dalam persentase
- 📊 Visual progress bar untuk setiap produk
- 📄 Deskripsi produk ringkas dari data
- 🏆 Ranking produk berdasarkan kecocokan

### 4. **Performance**
- ⚡ Model caching untuk kecepatan optimal
- 💾 Model cache simpan di disk setelah diload
- ⏳ Loading spinner untuk feedback visual

### 5. **Demo Data**
- 📦 10 produk skincare sampel dengan review
- 🤖 Siap digunakan tanpa setup data tambahan

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi | Fungsi |
|----------|-----------|--------|
| **Framework Web** | Streamlit | UI interaktif |
| **Data Processing** | Pandas, NumPy | Manipulasi data |
| **ML Model** | Scikit-learn | TF-IDF, Cosine Similarity |
| **Styling** | Custom CSS | UI/UX modern |
| **Caching** | Pickle | Model persistence |

---

## 📦 Instalasi

### Prasyarat
- Python 3.8 atau lebih tinggi
- pip atau conda

### Step 1: Clone atau Download Project
```bash
cd /path/to/skincare_recommendation
```

### Step 2: Buat Virtual Environment (Recommended)

**Menggunakan venv:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Menggunakan conda:**
```bash
conda create -n skincare-app python=3.10
conda activate skincare-app
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Menggunakan

### Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan membuka di browser default Anda di `http://localhost:8501`

### Cara Kerja

1. **Input Kebutuhan Kulit**
   - Ketikkan deskripsi kebutuhan kulit Anda (contoh: "kulit berminyak, pori besar, butuh cleanser")
   - Atau klik salah satu contoh pencarian yang tersedia

2. **Dapatkan Rekomendasi**
   - Klik tombol "🚀 Rekomendasikan"
   - Aplikasi akan menganalisis input Anda
   - Loading spinner akan muncul selama proses

3. **Lihat Hasil**
   - Produk ditampilkan dalam card yang menarik
   - Setiap produk menunjukkan:
     - Ranking/nomor urut
     - Nama produk
     - Similarity score (persentase kecocokan)
     - Visual progress bar
     - Deskripsi singkat dari review

---

## 📂 Struktur File

```
skincare_recommendation/
│
├── app.py                          # Main Streamlit application
├── model.py                        # Model logic dan utility functions
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation (file ini)
│
├── NLP_2026 (1).ipynb             # Original Jupyter notebook
├── model_cache.pkl                # Generated cache file (otomatis dibuat)
│
└── [optional] data/
    ├── reviews_0-250_masked.csv
    ├── reviews_250-500_masked.csv
    ├── reviews_500-750_masked.csv
    ├── reviews_750-1250_masked.csv
    ├── reviews_1250-end_masked.csv
    └── product_info_skincare.csv
```

---

## ⚙️ Pengaturan Lanjutan

### Menggunakan Data Asli (Bukan Demo)

Jika Anda ingin menggunakan dataset asli dari Google Drive atau file lokal:

**Edit file `app.py`** di bagian `load_model_cache()`:

```python
@st.cache_resource
def load_model_cache():
    # Ganti use_demo=True dengan use_demo=False
    # dan sediakan data_path ke folder dengan CSV files
    return load_or_create_model(
        data_path="/path/to/your/data/folder",  # Edit path ini
        use_demo=False  # Ubah ke False
    )
```

Struktur folder data harus mengandung:
- `reviews_0-250_masked.csv`
- `reviews_250-500_masked.csv`
- `reviews_500-750_masked.csv`
- `reviews_750-1250_masked.csv`
- `reviews_1250-end_masked.csv`
- `product_info_skincare.csv`

### Menyesuaikan Parameter TF-IDF

Edit file `model.py` dalam fungsi `load_or_create_model()`:

```python
tfidf = TfidfVectorizer(
    stop_words='english',
    max_features=5000,        # Tingkatkan untuk lebih banyak features
    ngram_range=(1, 2)        # Ubah untuk n-grams yang berbeda
)
```

### Mengubah Jumlah Rekomendasi

Di file `app.py`, ubah parameter `top_n`:

```python
recommendations = get_recommendations(
    user_input=user_input,
    tfidf_matrix=tfidf_matrix,
    df_grouped=df_grouped,
    tfidf_vectorizer=tfidf_vectorizer,
    top_n=5  # Ubah angka ini (default: 5)
)
```

### Menyesuaikan Styling

Edit section **CUSTOM CSS** di `app.py` untuk mengubah:
- Warna gradien: ubah nilai hex color (#667eea, #764ba2)
- Font size: ubah nilai rem/px
- Border radius: ubah efek rounded corners
- Animations: modify @keyframes

---

## 📊 Cara Kerja Model

### 1. **Data Preprocessing**
- Menghubungkan data reviews dengan product info
- Lowercase semua teks
- Hapus duplikasi
- Group by product_name untuk gabung review per produk

### 2. **Feature Extraction (TF-IDF)**
- Convert teks menjadi vector numeric
- Max 5000 features dari vocabulary
- Menggunakan unigram dan bigram

### 3. **Similarity Matching**
- Transform user input ke TF-IDF vector
- Hitung cosine similarity dengan semua produk
- Ranking berdasarkan similarity score tertinggi

### 4. **Result Display**
- Return top-5 produk dengan similarity score
- Tampilkan dengan visual yang menarik

---

## 🔧 Troubleshooting

### **Masalah: "Module not found"**
```bash
# Pastikan sudah di virtual environment yang benar
pip install -r requirements.txt
```

### **Masalah: Aplikasi berjalan lambat**
- Hapus file `model_cache.pkl` untuk refresh cache
- Periksa resources komputer (RAM, CPU)
- Kurangi `max_features` di TF-IDF vectorizer

### **Masalah: Tidak ada rekomendasi yang keluar**
- Periksa input text (jangan terlalu singkat)
- Coba input dengan keywords dari review produk
- Verifikasi data produk ter-load dengan benar

### **Masalah: Port 8501 sudah digunakan**
```bash
streamlit run app.py --server.port 8502
```

### **Masalah: Import Error untuk streamlit-extras**
```bash
pip install --upgrade streamlit-extras
```

---

## 🎥 Demo

### Contoh Input dan Output

**Input:** "kulit berminyak, pori besar, berjerawat"
```
Output:
1. Anti-Acne Face Wash (Similarity: 87%)
2. Oil Control Toner (Similarity: 84%)
3. Deep Pore Cleanser (Similarity: 79%)
...
```

---

## 📝 Notes

- **Demo Data**: Aplikasi menggunakan 10 produk dummy untuk demo. Untuk hasil lebih akurat, gunakan dataset asli Anda.
- **Model Caching**: Model akan di-cache otomatis di disk setelah run pertama untuk performa lebih cepat.
- **Multilingual**: Untuk saat ini, model optimal untuk English text. Bisa dikemangkan untuk Bahasa Indonesia.

---

## 🚀 Pengembangan Lanjutan (Future Enhancements)

- [ ] Tambah filter by product category
- [ ] Tambah rating/reviews dari user
- [ ] Integrasi dengan database real
- [ ] Support multiple language
- [ ] Machine learning retraining pipeline
- [ ] User preferences saving
- [ ] Admin dashboard

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik/demo. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

## 👨‍💻 Support

Jika ada pertanyaan atau issue:
1. Baca section Troubleshooting di atas
2. Periksa dokumentasi Streamlit: https://docs.streamlit.io
3. Lihat dokumentasi Scikit-learn: https://scikit-learn.org

---

**Happy skincare hunting!** ✨💅
