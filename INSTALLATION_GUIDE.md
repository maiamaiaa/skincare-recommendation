# 🛠️ DETAILED INSTALLATION GUIDE

Panduan instalasi lengkap untuk Skincare Recommendation System di berbagai platform.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Windows Installation](#windows-installation)
- [macOS Installation](#macos-installation)
- [Linux Installation](#linux-installation)
- [Troubleshooting](#troubleshooting)
- [Verification](#verification)

---

## 📦 Prerequisites

Sebelum memulai instalasi, pastikan Anda memiliki:

### **Required**
- **Python 3.8 or higher** (Download dari [python.org](https://www.python.org))
- **pip** (Python package manager - biasanya sudah included dengan Python)
- **Git** (Optional, untuk clone repository)

### **Recommended**
- **Virtual Environment tool** (venv - included dengan Python)
- **Terminal/Command Prompt** dengan akses admin (untuk Windows)
- **Code Editor** (VS Code, PyCharm, dll)

### **Minimal Hardware**
- **RAM:** 4 GB minimum
- **Disk Space:** 500 MB free
- **Processing:** Multi-core recommended

---

## 🪟 Windows Installation

### Step 1: Verify Python Installation

1. **Open Command Prompt** (Win+R → cmd → Enter)

2. **Check Python version:**
   ```cmd
   python --version
   ```
   
   Expected output: `Python 3.8.0` or higher

   ⚠️ **If not found:**
   - Download dari [python.org/downloads](https://www.python.org/downloads/)
   - **IMPORTANT**: Saat install, check "Add Python to PATH"
   - Restart Command Prompt setelah install

3. **Check pip:**
   ```cmd
   pip --version
   ```
   
   Expected output: `pip X.X.X`

---

### Step 2: Navigate to Project Directory

```cmd
cd C:\Users\YourUsername\Documents\uni\sem6\nlp\skincare_recommendation
```

Replace `YourUsername` dengan username Windows Anda.

---

### Step 3: Create Virtual Environment

```cmd
python -m venv venv
```

Output:
```
(venv folder will be created)
```

---

### Step 4: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

Expected prompt change: `(venv) C:\path\to\project>`

---

### Step 5: Upgrade pip (Optional but Recommended)

```cmd
python -m pip install --upgrade pip
```

---

### Step 6: Install Dependencies

```cmd
pip install -r requirements.txt
```

Output will show:
```
Collecting streamlit
Collecting pandas
...
Successfully installed streamlit pandas numpy scikit-learn streamlit-extras
```

⌛ **Takes ~2-5 minutes** depending on internet speed.

---

### Step 7: Run Verification Script

```cmd
python test_setup.py
```

Expected output:
```
============================================================
  SKINCARE RECOMMENDATION SYSTEM - SETUP TEST
============================================================

[1/5] Checking Python version...
✅ Python 3.10.11 - OK

[2/5] Checking required files...
   ✅ app.py
   ✅ model.py
   ...

[5/5] Testing recommendation function...
   ✅ Recommendations generated for 'dry skin moisturizer'
   ✅ 5 products recommended

============================================================
  ✅ ALL TESTS PASSED!
============================================================

🚀 Ready to run:

   streamlit run app.py
```

---

### Step 8: Run Application

```cmd
streamlit run app.py
```

Expected:
- A new browser window opens
- URL: `http://localhost:8501`
- Streamlit interface loads

---

### Step 9: Stop Application

Press `Ctrl+C` in Command Prompt to stop the server.

---

## 🍎 macOS Installation

### Step 1: Install Homebrew (if not installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### Step 2: Verify Python Installation

```bash
python3 --version
```

If Python not found:
```bash
brew install python@3.11
```

---

### Step 3: Navigate to Project Directory

```bash
cd ~/Documents/uni/sem6/nlp/skincare_recommendation
```

---

### Step 4: Create Virtual Environment

**Option A: Using venv (Recommended)**
```bash
python3 -m venv venv
```

**Option B: Using conda (if installed)**
```bash
conda create -n skincare python=3.10
conda activate skincare
```

---

### Step 5: Activate Virtual Environment

**Using venv:**
```bash
source venv/bin/activate
```

**Using conda:**
```bash
conda activate skincare
```

Expected prompt change: `(venv)` or `(skincare)` prefix

---

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 7: Run Verification Script

```bash
python test_setup.py
```

---

### Step 8: Run Application

```bash
streamlit run app.py
```

Browser akan otomatis membuka dengan aplikasi.

---

### Step 9: Using Setup Script (Optional)

Alternatif, gunakan provided setup script:

```bash
chmod +x setup.sh
./setup.sh
```

Script ini akan:
1. Create virtual environment
2. Activate environment
3. Install all dependencies
4. Show ready message

---

## 🐧 Linux Installation

### Step 1: Update Package Manager

**For Ubuntu/Debian:**
```bash
sudo apt update
sudo apt upgrade
```

**For Fedora:**
```bash
sudo dnf update
```

---

### Step 2: Install Python & pip (if needed)

**Ubuntu/Debian:**
```bash
sudo apt install python3 python3-pip python3-venv
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

---

### Step 3: Navigate to Project

```bash
cd ~/Documents/uni/sem6/nlp/skincare_recommendation
```

---

### Step 4: Create Virtual Environment

```bash
python3 -m venv venv
```

---

### Step 5: Activate Virtual Environment

```bash
source venv/bin/activate
```

---

### Step 6: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Step 7: Run Verification Script

```bash
python test_setup.py
```

---

### Step 8: Run Application

```bash
streamlit run app.py
```

---

### Step 9: Running as Service (Advanced)

Gunakan systemd untuk run aplikasi sebagai service:

```bash
sudo nano /etc/systemd/system/skincare-app.service
```

Add:
```ini
[Unit]
Description=Skincare Recommendation Streamlit App
After=network.target

[Service]
Type=simple
User=<your-username>
WorkingDirectory=/home/<your-username>/Documents/uni/sem6/nlp/skincare_recommendation
ExecStart=/home/<your-username>/Documents/uni/sem6/nlp/skincare_recommendation/venv/bin/streamlit run app.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl daemon-reload
sudo systemctl start skincare-app
sudo systemctl enable skincare-app  # Auto-start on boot
```

Check status:
```bash
sudo systemctl status skincare-app
```

---

## 🔧 Troubleshooting

### **Python Not Found**

**Windows:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
1. Download Python dari [python.org](https://www.python.org)
2. Run installer
3. ☑️ Check "Add Python to PATH"
4. Restart Command Prompt
5. Verify: `python --version`

---

### **Virtual Environment Not Activating**

**Windows:**
```cmd
# Wrong:
source venv/bin/activate

# Correct for Windows:
venv\Scripts\activate
```

**Correct by OS:**
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

---

### **pip Command Not Found**

```bash
python -m pip install --upgrade pip
```

Then use:
```bash
python -m pip install -r requirements.txt
```

---

### **Permission Denied (macOS/Linux)**

```bash
chmod +x setup.sh
./setup.sh
```

Or use:
```bash
python3 -m pip install --user -r requirements.txt
```

---

### **Port 8501 Already in Use**

Run on different port:
```bash
streamlit run app.py --server.port 8502
```

---

### **Module Import Errors**

Double-check aktivasi venv:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Then reinstall:
```bash
pip install -r requirements.txt
```

---

### **Slow Model Loading**

First run memang lebih lambat (1-2 menit):
- Model di-cache ke `model_cache.pkl`
- Run kedua dan seterusnya akan cepat
- Jika ingin reset, hapus `model_cache.pkl`

---

### **Out of Memory Error**

Kurangi `TFIDF_MAX_FEATURES` di `config.py`:
```python
TFIDF_MAX_FEATURES = 2000  # Turun dari 5000
```

Restart aplikasi.

---

## ✅ Verification

Setelah instalasi selesai, verify dengan checklist ini:

### **Basic Checks**
- [ ] Python 3.8+ installed
- [ ] pip working
- [ ] Virtual environment created
- [ ] `requirements.txt` installed without errors
- [ ] No permission errors

### **Application Checks**
- [ ] `python test_setup.py` shows all ✅
- [ ] Model loads without errors
- [ ] Can access `http://localhost:8501`
- [ ] UI displays correctly
- [ ] Can input text
- [ ] Get recommendations back

### **Advanced Checks**
- [ ] Product cards display properly
- [ ] CSS styling works
- [ ] Loading spinner shows
- [ ] Example buttons work
- [ ] No console errors in browser

---

### **Quick Test Command**

Run this untuk quick verification:

```bash
# Windows
python test_setup.py && echo Success!

# macOS/Linux
python test_setup.py && echo "Success! ✅" || echo "Failed ❌"
```

---

## 📞 Common Environment Issues by OS

| OS | Issue | Solution |
|----|----|----------|
| Windows | venv not recognized | Use `venv\Scripts\activate` |
| Windows | pip not found | Use `python -m pip` |
| macOS | Permission denied | Use `chmod +x` or `sudo` |
| macOS | Homebrew issues | Run `/bin/bash -c "$(curl...)` |
| Linux | Python version conflict | Use `python3` explicitly |
| Linux | systemd unit fails | Check WorkingDirectory & User |

---

## 🚀 Post-Installation Steps

1. **Test the app:**
   ```bash
   streamlit run app.py
   ```

2. **Try example inputs:**
   - "dry skin moisturizer"
   - "oily skin acne prone"
   - "brightening serum"

3. **Customize (optional):**
   - Edit `config.py` untuk ubah colors
   - Edit `app.py` untuk ubah UI

4. **Deploy (advanced):**
   - Use Streamlit Cloud: https://streamlit.io/cloud
   - Or deploy to Heroku/AWS/DigitalOcean

---

## 📚 Additional Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Python Docs:** https://docs.python.org/3/
- **Scikit-learn Docs:** https://scikit-learn.org/
- **Pandas Docs:** https://pandas.pydata.org/docs/

---

## ✨ Congratulations!

Instalasi selesai! Sekarang Anda siap untuk menggunakan Skincare Recommendation System.

Next: Read `QUICKSTART.md` untuk memulai!
