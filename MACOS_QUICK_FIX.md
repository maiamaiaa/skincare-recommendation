# 🚀 MACOS QUICK FIX - Python 3 Setup

Your macOS has Python 3 installed but needs to use `python3` and `pip3` instead of `python` and `pip`.

---

## ⚡ Quick Setup (Copy & Paste)

Run these commands one by one in your terminal:

### Step 1: Navigate to project folder
```bash
cd ~/Documents/uni/sem6/nlp/skincare_recommendation
```

### Step 2: Create virtual environment
```bash
python3 -m venv venv
```

### Step 3: Activate virtual environment
```bash
source venv/bin/activate
```

After this, your prompt should show `(venv)` at the start.

### Step 4: Install dependencies
```bash
pip install -r requirements.txt
```

⏳ This will take 3-5 minutes (first time only). It's downloading packages.

### Step 5: Verify installation
```bash
python test_setup.py
```

You should see: `✅ ALL TESTS PASSED!`

### Step 6: Run the app!
```bash
streamlit run app.py
```

Browser will automatically open at `http://localhost:8501` 🎉

---

## ✅ Verification

After installation, check if everything is working:

```bash
# Check Python in venv
python --version

# Check if streamlit is installed
python -c "import streamlit; print('✅ Streamlit OK')"

# Check model can load
python test_setup.py
```

---

## 🔗 Create Alias (Optional - For Future Use)

If you want to use just `python` instead of `python3` in this project:

```bash
# Add to ~/.zshrc file:
echo "alias python=python3" >> ~/.zshrc

# Then reload:
source ~/.zshrc
```

After this, you can use `python` instead of `python3` everywhere.

---

## ❌ If Installation is Stuck

If it's taking too long, press `Ctrl+C` to stop and try:

```bash
pip install --no-cache-dir -r requirements.txt
```

Or upgrade pip first:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📊 What's Being Downloaded

The installation downloads (~150 MB):
- streamlit (8.4 MB) - Web framework
- numpy (19.8 MB) - Math library
- pandas (11.6 MB) - Data processing
- scikit-learn (10.1 MB) - ML library
- Plus dependencies (70+ MB)

All downloaded packages go into `venv/lib/` folder.

---

## 💾 Key Paths

- **Virtual env location:** `~/Documents/uni/sem6/nlp/skincare_recommendation/venv/`
- **Python executable:** `venv/bin/python`
- **Requirements file:** `requirements.txt`
- **App file:** `app.py`

---

## ⚠️ Common Issues

| Issue | Solution |
|-------|----------|
| `pip: command not found` | Use `pip3` or activate venv first |
| `ModuleNotFoundError: streamlit` | Make sure venv is activated (see `(venv)` in prompt) |
| Installation hanging | Press `Ctrl+C` and try with `--no-cache-dir` |
| Port 8501 in use | Run `streamlit run app.py --server.port 8502` |

---

## 🎯 Next Steps

1. Copy the commands from "Quick Setup" section
2. Run them in your terminal **one by one**
3. Wait for `pip install` to finish (~5 min)
4. Run `python test_setup.py` to verify
5. Run `streamlit run app.py` to start the app!

---

**Good luck! 🚀**
