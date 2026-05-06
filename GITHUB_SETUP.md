# 🐙 GitHub Setup - Complete Guide

Your git push needs a repository created on GitHub first.

---

## ✅ Step 1: Create GitHub Repository

### **Option A: Via Web Browser (Easiest)**

1. Go to https://github.com/new
2. Repository name: `skincare-recommendation`
3. Description: `NLP-based skincare product recommendation system using TF-IDF and Streamlit`
4. Choose **Public** (required for free Streamlit Cloud deployment)
5. ☐ Don't check "Initialize with README"
6. Click **Create repository**

### **Option B: Via GitHub CLI**

```bash
# Install GitHub CLI first from: https://cli.github.com
# Then create repo:

gh repo create skincare-recommendation --public --source=. --remote=origin --push
```

---

## 📝 Step 2: Push Code (After Creating Repo)

Once your GitHub repo is created, run these commands:

```bash
# Go to your project folder
cd ~/Documents/uni/sem6/nlp/skincare_recommendation

# Make sure you're on main branch
git branch -M main

# Set upstream and push
git push -u origin main
```

**What you'll see:**
```
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 8 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (20/20), 140 KiB | 2.5 MiB/s, done.
Total 20 (delta 0), reused 0 (delta 0)
To https://github.com/YOUR_USERNAME/skincare-recommendation.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## 🔐 Authentication Issues?

### **If asked for password:**

Modern GitHub requires **Personal Access Tokens** instead of passwords:

1. Go to https://github.com/settings/tokens
2. Click **Generate new token**
3. Select scopes: `repo`, `read:user`, `gist`
4. Copy the token
5. When git asks for password, paste the token

### **Or Setup SSH (More Secure):**

```bash
# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your-email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Get public key (copy this to GitHub)
cat ~/.ssh/id_ed25519.pub

# Go to https://github.com/settings/keys to add it
```

Then change your git remote:

```bash
git remote remove origin
git remote add origin git@github.com:YOUR_USERNAME/skincare-recommendation.git
git push -u origin main
```

---

## ✅ Verify Push Worked

Check your repository on GitHub:

1. Go to https://github.com/YOUR_USERNAME/skincare-recommendation
2. You should see all your files (app.py, model.py, etc.)
3. "main" branch should be created

---

## 🚀 Next: Deploy to Streamlit Cloud

Once pushed to GitHub:

1. Go to https://share.streamlit.io
2. Click **New app**
3. Select your `skincare-recommendation` repo
4. Select `app.py` as main file
5. Click Deploy!

---

## ⚡ Quick Reference

```bash
# Create repo on GitHub first at https://github.com/new

# Then in terminal:
cd ~/Documents/uni/sem6/nlp/skincare_recommendation

# Push code:
git push -u origin main

# Verify:
git log --oneline -3
```

---

## 🆘 Troubleshooting

| Error | Solution |
|-------|----------|
| `repository not found` | Create repo on GitHub first |
| `Authentication failed` | Use personal access token instead of password |
| `fatal: no upstream` | Run `git push -u origin main` (with -u flag) |
| `remote: Repository not found` | Check your username in git remote URL |

---

**All set? Create the repo and run:** 
```bash
git push -u origin main
```
