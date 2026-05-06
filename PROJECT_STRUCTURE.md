# 📚 PROJECT DOCUMENTATION & FILE STRUCTURE

Dokumentasi lengkap untuk Skincare Recommendation System - Streamlit Web App

---

## 📦 File Structure

```
skincare_recommendation/
│
├── 📄 Core Application Files
│   ├── app.py                     ← Main Streamlit application (UI/UX)
│   ├── model.py                   ← ML model logic & functions
│   ├── config.py                  ← Configuration & constants
│   └── utils.py                   ← Utility functions & helpers
│
├── 📄 Configuration Files
│   ├── requirements.txt            ← Python dependencies
│   ├── requirements-dev.txt        ← Development dependencies (optional)
│   ├── setup.sh                    ← Setup script (Linux/Mac)
│   └── .streamlit/config.toml      ← Streamlit configuration
│
├── 📄 Documentation
│   ├── README.md                   ← Complete documentation
│   ├── QUICKSTART.md               ← Quick start guide
│   └── PROJECT_STRUCTURE.md        ← This file
│
├── 📄 Testing & Development
│   ├── test_setup.py               ← Setup verification script
│   └── .gitignore                  ← Git ignore file
│
├── 📄 Original Project
│   └── NLP_2026 (1).ipynb          ← Original Jupyter notebook
│
└── 📁 Auto-generated
    ├── model_cache.pkl             ← Model cache (created on first run)
    └── .streamlit/                 ← Streamlit configuration directory
```

---

## 📄 File Details

### **Core Application Files**

#### 1. **app.py** - Main Streamlit Application
**Tujuan:** Aplikasi web utama dengan UI/UX yang menarik

**Key Features:**
- Layout modern dengan gradient styling
- Input area dengan text area dan contoh query
- Display hasil dalam bentuk product cards
- Animations dan CSS custom
- Metric display (total produk, model, features)
- Example queries buttons
- Loading spinner dan success messages

**Dependencies:**
- streamlit
- streamlit_extras
- config, model, utils modules

**Main Functions:**
- Load model cache
- Handle user input
- Display recommendations
- Show example queries

---

#### 2. **model.py** - ML Model & Logic
**Tujuan:** Core logic untuk TF-IDF dan recommendation system

**Key Functions:**
- `preprocess_text()` - Preprocessing teks input
- `load_or_create_model()` - Load/create TF-IDF model dengan caching
- `load_data_from_csv()` - Load data dari CSV files
- `create_demo_data()` - Buat demo data untuk testing
- `get_recommendations()` - Get recommendations based on input
- `get_product_details()` - Get product description

**Features:**
- TF-IDF Vectorizer dengan max_features=5000
- Cosine similarity calculation
- Model caching dengan pickle
- Demo data integration
- Flexible untuk use real data atau demo data

---

#### 3. **config.py** - Configuration & Constants
**Tujuan:** Centralized configuration untuk seluruh aplikasi

**Sections:**
- **APP CONFIGURATION** - Judul, subtitle, deskripsi
- **MODEL CONFIGURATION** - TF-IDF settings, cache path
- **UI CONFIGURATION** - Top N, input constraints, placeholder
- **STYLING & COLORS** - Warna palette dan styling
- **EMOJI MAPPING** - Emoji icons untuk UI
- **SIMILARITY SCORE THRESHOLDS** - Threshold untuk scoring
- **EXAMPLE QUERIES** - Contoh pencarian
- **MESSAGES** - Error, success, info messages
- **LOGGING** - Log configuration

**Usage:**
```python
from config import PRIMARY_COLOR, APP_TITLE, DEFAULT_TOP_N
```

---

#### 4. **utils.py** - Utility Functions & Helpers
**Tujuan:** Helper functions untuk logging, validation, display, dan utilities

**Key Functions:**
- `log_function_call()` - Decorator untuk logging
- `time_execution()` - Timing decorator
- `format_percentage()` - Format ke percentage
- `get_similarity_emoji()` - Get emoji for score
- `get_recommendation_message()` - Message untuk score
- `validate_text_input()` - Validate user input
- `display_product_card_enhanced()` - Enhanced card display
- `get_stats_summary()` - Stats dari recommendations
- `create_example_queries()` - Generate example queries

**Usage:**
```python
from utils import validate_text_input, format_percentage
```

---

### **Configuration Files**

#### 5. **requirements.txt** - Python Dependencies
**Tujuan:** List semua package yang diperlukan untuk run aplikasi

**Packages:**
```
streamlit==1.28.1        - Web framework
pandas==2.0.3            - Data processing
numpy==1.24.3            - Numerical computing
scikit-learn==1.3.0      - ML library
streamlit-extras==0.3.6  - Extra Streamlit components
```

**Install:**
```bash
pip install -r requirements.txt
```

---

#### 6. **requirements-dev.txt** - Development Dependencies (Optional)
**Tujuan:** Additional packages untuk development, testing, code quality

**Packages:**
- pytest, pytest-cov - Testing
- black, flake8, pylint, isort - Code quality
- sphinx - Documentation
- ipython, ipdb - Debugging

**Install (Optional):**
```bash
pip install -r requirements-dev.txt
```

---

#### 7. **setup.sh** - Setup Script (Linux/Mac)
**Tujuan:** Automated setup script untuk membuat venv dan install dependencies

**Features:**
- Colored output
- Python version checking
- Virtual environment creation
- Dependency installation

**Usage:**
```bash
chmod +x setup.sh
./setup.sh
```

---

#### 8. **.streamlit/config.toml** - Streamlit Configuration
**Tujuan:** Configure Streamlit app behavior dan appearance

**Sections:**
- **[theme]** - Color scheme (primary, secondary, text, background)
- **[client]** - Client settings
- **[logger]** - Logging level
- **[server]** - Server settings (port, gzip, CORS)

---

### **Documentation Files**

#### 9. **README.md** - Complete Documentation
**Tujuan:** Dokumentasi lengkap untuk project

**Sections:**
- Features overview
- Technology stack
- Installation guide
- Usage instructions
- File structure
- Advanced settings
- Troubleshooting
- Development notes

**Length:** ~400 lines
**Target:** Technical users, developers

---

#### 10. **QUICKSTART.md** - Quick Start Guide
**Tujuan:** Panduan cepat untuk get started dalam 2 menit

**Sections:**
- Prerequisites
- Setup for Linux/Mac/Windows
- How to use
- Quick troubleshooting table
- Customization tips

**Length:** ~100 lines
**Target:** New users, rapid deployment

---

#### 11. **PROJECT_STRUCTURE.md** - This File
**Tujuan:** Detailed documentation dari semua files dan struktur

---

### **Testing & Development**

#### 12. **test_setup.py** - Setup Verification Script
**Tujuan:** Verify semua dependencies dan setup sudah correct

**Tests:**
1. Python version check (3.8+)
2. Required files check
3. Package import check
4. Model loading test
5. Recommendation function test

**Output:**
- ✅ Tests passed / ❌ Failed
- Detailed feedback untuk troubleshooting
- Ready-to-run command

**Usage:**
```bash
python test_setup.py
```

---

#### 13. **.gitignore** - Git Ignore File
**Tujuan:** Specify files yang tidak perlu di-commit ke git

**Ignores:**
- Python cache (__pycache__, *.pyc)
- Virtual environments (venv/, env/)
- IDE files (.vscode/, .idea/)
- Streamlit cache
- Model cache (*.pkl)
- Logs dan temp files
- Environment variables (.env)

---

### **Original Project**

#### 14. **NLP_2026 (1).ipynb** - Original Jupyter Notebook
**Tujuan:** Original notebook dengan semua analysis dan development

**Content:**
- Data loading dari Google Drive
- EDA dan preprocessing
- TF-IDF vectorizer creation
- Recommendation functions
- Model evaluation

---

## 🔄 Data Flow Diagram

```
User Input
    ↓
[app.py - Input Validation] ← (config.py - Input constraints)
    ↓
[model.py - preprocess_text()]
    ↓
[model.py - get_recommendations()]
    ├─→ [Load cached model] or [Create new model]
    ├─→ [TF-IDF Transform user input]
    ├─→ [Cosine Similarity calculation]
    └─→ [Ranking & top-N selection]
    ↓
[app.py - Format Results using utils.py]
    ↓
[Display Product Cards with CSS styling]
    ↓
User Sees Results
```

---

## 🔌 Module Dependencies

```
app.py
├── streamlit
├── streamlit_extras
├── model.py ✓ (custom)
├── config.py ✓ (custom)
└── time

model.py
├── pandas
├── numpy
├── sklearn (TfidfVectorizer, cosine_similarity)
├── pickle
└── os, Path

config.py
└── (No dependencies - pure constants)

utils.py
├── streamlit
├── functools, time
└── logging

test_setup.py
├── sys, os, Path
└── Dynamic imports test
```

---

## ⚙️ How Everything Works Together

### 1. **Initialization**
```
streamlit run app.py
    ↓
[Load config from config.py]
    ↓
[Load model using model.py with caching]
    ↓
[Initialize Streamlit session state]
    ↓
[Display UI from app.py with styling]
```

### 2. **User Interaction**
```
User types input
    ↓
[app.py validates using utils.py]
    ↓
[Click "Rekomendasikan" button]
    ↓
[Call model.get_recommendations()]
    ↓
[Format results using utils.py]
    ↓
[Display using CSS from app.py]
```

### 3. **Model Usage**
```
Input: "dry skin moisturizer"
    ↓
[Preprocess: lowercase, strip]
    ↓
[TF-IDF Transform using cached vectorizer]
    ↓
[Cosine similarity with all 10 products]
    ↓
[Sort by score, return top-5]
    ↓
Output: DataFrame with [{product_name, similarity_score}]
```

---

## 🎨 Styling System

### CSS Injection Points
Located in `app.py`:
```html
<!-- Header with gradient -->
<div class="header-container">

<!-- Input area -->
<div class="input-container">

<!-- Product cards -->
<div class="product-card">

<!-- Score bars -->
<div class="score-bar">

<!-- Animations -->
@keyframes slideIn, fadeIn
```

### Color System (config.py)
```
PRIMARY: #667eea (Purple)
SECONDARY: #764ba2 (Darker Purple)
BACKGROUND: #f5f7fa (Light Blue)
ACCENT: #c3cfe2 (Medium Blue)
```

---

## 📊 Model Configuration

### TF-IDF Settings (config.py)
```python
TFIDF_STOP_WORDS = 'english'
TFIDF_MAX_FEATURES = 5000
TFIDF_NGRAM_RANGE = (1, 2)  # Unigram + Bigram
```

### Output Settings
```python
DEFAULT_TOP_N = 5  # Top 5 recommendations
SIMILARITY_THRESHOLDS = {
    'excellent': 0.85,
    'good': 0.70,
    'fair': 0.50,
}
```

---

## ✅ Verification Checklist

Gunakan ini untuk memastikan setup benar:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created dan aktif
- [ ] `pip install -r requirements.txt` executed
- [ ] Semua files ada (gunakan `test_setup.py`)
- [ ] Tidak ada import errors
- [ ] Model cache file created (model_cache.pkl)
- [ ] `streamlit run app.py` works
- [ ] Can access `http://localhost:8501`
- [ ] Can input text dan get recommendations
- [ ] No CSS errors di browser console

---

## 🚀 Next Steps

1. **Run test script:**
   ```bash
   python test_setup.py
   ```

2. **Start application:**
   ```bash
   streamlit run app.py
   ```

3. **Test recommendations:**
   - Input: "dry skin moisturizer"
   - Check: Get 5 results
   - Verify: Scores make sense

4. **Customize (Optional):**
   - Edit config.py untuk colors
   - Change DEFAULT_TOP_N untuk lebih banyak results
   - Upload real data ke model.py

---

## 📞 Troubleshooting by File

| File | Common Issues | Solution |
|------|---------------|----------|
| app.py | CSS not showing | Check browser console |
| app.py | Input validation fails | Check config.py for constraints |
| model.py | Model loading slow | First run caches model |
| model.py | No recommendations | Check model.create_demo_data() |
| config.py | Colors look wrong | Edit RGB/HEX values |
| test_setup.py | Import errors | Run test to identify missing package |

---

**Created for: Skincare Recommendation System - NLP 2026**
**Last Updated:** May 2026
