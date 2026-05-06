# 📑 INDEX - Skincare Recommendation System

Quick reference guide untuk semua file dan dokumentasi.

---

## 🚀 START HERE

**Baru pertama kali?** Mulai dari sini dalam urutan:

1. **[QUICKSTART.md](QUICKSTART.md)** (2-3 min) ← START HERE
   - Setup cepat
   - Jalankan aplikasi dalam 3 langkah
   - Troubleshooting cepat

2. **[INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)** (5-10 min)
   - Instruksi detail per OS (Windows/Mac/Linux)
   - Virtual environment setup
   - Detailed troubleshooting

3. **[README.md](README.md)** (15-20 min)
   - Dokumentasi lengkap
   - Feature explanation
   - Advanced configuration

---

## 📂 FILE ORGANIZATION

### **Application Core** (Start di sini untuk development)

| File | Size | Purpose | Modified |
|------|------|---------|----------|
| [app.py](app.py) | ~5 KB | Main Streamlit UI/UX application | ✅ |
| [model.py](model.py) | ~8 KB | ML model & recommendation logic | ✅ |
| [config.py](config.py) | ~6 KB | Centralized configuration | ✅ |
| [utils.py](utils.py) | ~7 KB | Helper functions & utilities | ✅ |

**👉 Mulai baca:** Baca dalam urutan `app.py` → `model.py` → `config.py`

---

### **Configuration & Setup** (Jalankan ini terlebih dahulu)

| File | Purpose | Action |
|------|---------|--------|
| [requirements.txt](requirements.txt) | Python dependencies | `pip install -r requirements.txt` |
| [requirements-dev.txt](requirements-dev.txt) | Dev dependencies (optional) | `pip install -r requirements-dev.txt` |
| [setup.sh](setup.sh) | Automated setup script (macOS/Linux) | `chmod +x setup.sh && ./setup.sh` |
| [.streamlit/config.toml](.streamlit/config.toml) | Streamlit configuration | Auto-loaded |
| [.gitignore](.gitignore) | Git ignore rules | - |

**👉 Setup action:** `pip install -r requirements.txt`

---

### **Documentation** (Baca sesuai kebutuhan)

| Document | Length | When to Read |
|----------|--------|--------------|
| [QUICKSTART.md](QUICKSTART.md) | 2 pages | 👈 **Read first!** Quick setup |
| [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) | 8 pages | Detailed install by OS |
| [README.md](README.md) | 15 pages | Complete reference |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | 20 pages | Architecture & detailed overview |
| [FILES_INDEX.md](FILES_INDEX.md) | This file | Quick reference |

---

### **Testing & Development**

| File | Purpose | Command |
|------|---------|---------|
| [test_setup.py](test_setup.py) | Verify installation | `python test_setup.py` |
| [NLP_2026 (1).ipynb](NLP_2026%20(1).ipynb) | Original Jupyter notebook | (Reference only) |

**👉 Verify setup:**
```bash
python test_setup.py
```

---

## 🎯 Quick Commands

### **Setup & Run**
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (choose one)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify
python test_setup.py

# 5. Run app
streamlit run app.py
```

### **Troubleshooting**
```bash
# Clear model cache
rm model_cache.pkl

# Run on different port
streamlit run app.py --server.port 8502

# Check Python version
python --version

# Check installed packages
pip list
```

---

## 📊 Code Structure Map

```
app.py (UI Layer)
    │
    ├── Imports: streamlit, model, config
    ├── CSS Styling & Animations
    ├── Page configuration
    ├── Header & metrics display
    ├── Input handling
    ├── Recommendation display
    └── Example queries
    
model.py (Logic Layer)
    │
    ├── preprocess_text()
    ├── load_or_create_model()
    ├── load_data_from_csv()
    ├── create_demo_data()
    ├── get_recommendations()
    └── get_product_details()

config.py (Configuration Layer)
    │
    ├── App configuration
    ├── Model settings
    ├── UI colors & styling
    ├── Messages & examples
    └── Thresholds

utils.py (Utilities Layer)
    │
    ├── Validation functions
    ├── Display helpers
    ├── Logging decorators
    └── Message templates
```

---

## 🔍 Find What You Need

### **"How do I...?"**

| Question | File | Section |
|----------|------|---------|
| Install the app? | QUICKSTART.md | Setup section |
| Run the application? | QUICKSTART.md | Top of file |
| Change the colors? | config.py | STYLING section |
| Modify recommendations? | model.py | get_recommendations() |
| Update input constraints? | config.py | UI CONFIGURATION |
| Add example queries? | config.py | EXAMPLE_QUERIES |
| Add logging? | utils.py | log_function_call() |
| Debug model? | test_setup.py | Run this first |
| Deploy to production? | README.md | Future enhancements |
| Customize UI? | app.py | custom_css section |

---

## 🎨 Common Customizations

### **Change Primary Color**
**File:** `config.py`
```python
PRIMARY_COLOR = "#667eea"  # Change this
```

### **Change Top-N Recommendations**
**File:** `app.py` (Search for `top_n=5`)
```python
recommendations = get_recommendations(..., top_n=5)  # Change 5
```

### **Modify TF-IDF Parameters**
**File:** `model.py` (In `load_or_create_model()`)
```python
tfidf = TfidfVectorizer(
    max_features=5000,  # Change this
    ngram_range=(1, 2)  # Or this
)
```

### **Add New Example Query**
**File:** `config.py` (In `EXAMPLE_QUERIES`)
```python
{
    'display': '🔎 Your text',
    'query': 'actual query',
    'description': 'description'
}
```

---

## 🚨 Emergency Troubleshooting

### **Everything broken? Do this:**

1. **Clear cache:**
   ```bash
   rm model_cache.pkl
   ```

2. **Verify environment:**
   ```bash
   python test_setup.py
   ```

3. **Reinstall packages:**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

4. **Check logs:**
   - Check browser console (F12)
   - Check terminal output

5. **Start fresh:**
   ```bash
   deactivate  # Exit venv
   rm -rf venv  # Delete venv
   python -m venv venv  # Recreate
   # Then follow setup steps
   ```

---

## 💾 File Statistics

| Category | Count | Total Size |
|----------|-------|-----------|
| Core Application | 4 | ~26 KB |
| Documentation | 5 | ~80 KB |
| Configuration | 4 | ~2 KB |
| Testing | 1 | ~3 KB |
| **TOTAL** | **14** | **~111 KB** |

---

## 🔗 Related Resources

### **Official Documentation**
- [Streamlit Docs](https://docs.streamlit.io)
- [Scikit-learn API](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### **Related Concepts**
- TF-IDF: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
- Cosine Similarity: https://en.wikipedia.org/wiki/Cosine_similarity
- Recommendation Systems: https://en.wikipedia.org/wiki/Recommender_system

---

## 📋 Development Checklist

### **Before First Run**
- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Run `python test_setup.py` successfully
- [ ] No import errors

### **Before Production**
- [ ] All tests pass
- [ ] Model caching works
- [ ] CSS displays correctly
- [ ] Loading spinner shows
- [ ] Error handling works
- [ ] Example queries functional

### **Before Deployment**
- [ ] Performance tested
- [ ] Memory usage acceptable
- [ ] Model loads fast
- [ ] UI responsive on mobile
- [ ] Browser compatibility checked
- [ ] Error messages user-friendly

---

## 🎓 Learning Path

**For Beginners:**
1. Read QUICKSTART.md
2. Run the app
3. Try example queries
4. Read README.md

**For Developers:**
1. Read INSTALLATION_GUIDE.md
2. Read PROJECT_STRUCTURE.md
3. Study app.py code
4. Study model.py code
5. Customize config.py

**For ML Engineers:**
1. Study model.py logic
2. Review TF-IDF implementation
3. Understand recommendation algorithm
4. Optimize model.py
5. Integrate custom ML models

---

## ⚡ Performance Tips

- **First run:** ~2-3 minutes (compiles model)
- **Subsequent runs:** <1 second (uses cache)
- **Clear cache:** `rm model_cache.pkl` to refresh
- **Optimize:** Reduce `TFIDF_MAX_FEATURES` if slow
- **Monitor:** Check system RAM usage

---

## 🎯 Success Criteria

App is working correctly when:

✅ Can start app with `streamlit run app.py`
✅ Browser loads at `http://localhost:8501`
✅ UI displays correctly with colors & styling
✅ Can type in input box
✅ Can click "Rekomendasikan" button
✅ Get 5 product recommendations back
✅ Each product shows name, score, bar
✅ No errors in console

---

## 📞 Support

- **Quick issues?** Check QUICKSTART.md
- **Setup issues?** See INSTALLATION_GUIDE.md
- **Code issues?** Read PROJECT_STRUCTURE.md
- **Features?** Read README.md
- **Still stuck?** Run `python test_setup.py` for diagnostics

---

## 📝 Version Info

- **Project:** Skincare Recommendation System
- **Version:** 1.0.0
- **Framework:** Streamlit
- **Python:** 3.8+
- **Last Updated:** May 2026

---

**Ready to start? Open [QUICKSTART.md](QUICKSTART.md) and run the setup! 🚀**
