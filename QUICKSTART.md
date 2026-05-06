# 🚀 QUICKSTART GUIDE

Panduan cepat untuk menjalankan Skincare Recommendation System dalam 2 menit!

---

## 📋 Prasyarat

- Python 3.8 atau lebih tinggi
- Terminal/Command Prompt

---

## ⚡ Setup (Linux/Mac)

### 1. Buat Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan otomatis membuka di browser: `http://localhost:8501`

---

## ⚡ Setup (Windows)

### 1. Buat Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Aplikasi
```bash
streamlit run app.py
```

---

## 🎯 Cara Menggunakan

1. **Input Kebutuhan Kulit**
   - Ketik deskripsi: "kulit berminyak, pori besar, berjerawat"
   - Atau klik contoh pencarian yang disediakan

2. **Klik Tombol Rekomendasikan**
   - Tunggu loading selesai

3. **Lihat Hasil**
   - 5 produk rekomendasi dengan similarity score
   - Setiap produk menampilkan ranking dan deskripsi

---

## 🔧 Troubleshooting Cepat

| Masalah | Solusi |
|---------|--------|
| `ModuleNotFoundError` | Pastikan virtual env aktif, jalankan `pip install -r requirements.txt` |
| Port 8501 sudah terpakai | Jalankan `streamlit run app.py --server.port 8502` |
| Aplikasi lambat | Pertama kali memang lebih lama karena loading model |
| Tidak ada rekomendasi | Coba input yang lebih detail/panjang |

---

## 📊 Struktur File Penting

```
📁 skincare_recommendation/
├── app.py              ← Main application
├── model.py            ← ML model & logic
├── config.py           ← Konfigurasi
├── utils.py            ← Helper functions
├── requirements.txt    ← Dependencies
└── README.md           ← Dokumentasi lengkap
```

---

## 🎨 Customize (Optional)

### Ubah Warna
Edit `config.py`:
```python
PRIMARY_COLOR = "#667eea"  # Ubah warna popup
```

### Ubah Jumlah Rekomendasi
Di `app.py`, cari `top_n=5` dan ubah jadi `top_n=10`

### Gunakan Data Asli
Di `app.py`, ubah line ini:
```python
return load_or_create_model(use_demo=False)  # Ubah dari True ke False
```

---

## ✨ Tips

- **Pertama kali jalan?** Model akan disimpan ke cache (`model_cache.pkl`) untuk loading lebih cepat
- **Contoh input yang bagus:** "rough texture, dark circles, need hydration"
- **Banyak rekomendasi similar?** Itu normal - input Anda cocok dengan beberapa produk

---

## 📞 Need Help?

Baca dokumentasi lengkap di `README.md` untuk:
- Konfigurasi lanjutan
- Menggunakan data custom
- Troubleshooting detail

---

**Siap? Jalankan `streamlit run app.py` sekarang!** 🎉
