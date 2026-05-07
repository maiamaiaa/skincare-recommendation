# 💖 Skincare Beauty Finder ✨

A cute and modern skincare product recommendation system powered by NLP (Natural Language Processing) using TF-IDF and Cosine Similarity. Built with Streamlit for an interactive web experience.

🌐 **Live Demo:** [Skincare Beauty Finder on Streamlit Cloud](https://share.streamlit.io/maiamaiaa/skincare-recommendation/main/app.py)

---

## ✨ Features

- 🤖 **AI-Powered Recommendations**: Uses TF-IDF vectorization and cosine similarity to find matching skincare products
- 💖 **Cute & Feminine UI**: Soft pastel aesthetic with pink, lilac, and cream colors
- 🌍 **100% English Interface**: Fully localized in English
- 📱 **Responsive Design**: Works beautifully on desktop and mobile devices
- ⚡ **Fast Processing**: Instant recommendations with cached model
- 💾 **Demo Data Included**: Ready-to-use sample skincare products
- 🎨 **Beautiful Animations**: Smooth transitions and hover effects

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maiamaiaa/skincare-recommendation.git
   cd skincare-recommendation
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:8501`
   - Start exploring skincare recommendations!

---

## 📁 Project Structure

```
skincare-recommendation/
│
├── app.py                    # Main Streamlit application with cute UI
├── model.py                  # ML model with TF-IDF and cosine similarity
├── config.py                 # Configuration settings and constants
├── utils.py                  # Utility functions and helpers
├── test_setup.py             # Setup verification script
│
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── .streamlit/config.toml    # Streamlit configuration
│
└── README.md                # This file
```

---

## 🎯 How It Works

### 1. **Text Input**
   - Users describe their skin concerns and needs
   - Example: "oily skin, acne-prone, needs brightening"

### 2. **TF-IDF Processing**
   - User input is converted to TF-IDF vectors
   - Maximum 5000 text features with unigram & bigram

### 3. **Similarity Matching**
   - Cosine similarity calculates match scores (0-1)
   - Top 5 products ranked by relevance

### 4. **Results Display**
   - Products shown with:
     - Match percentage (🎯)
     - Product name
     - Description from reviews
     - Visual similarity progress bar

---

## 🛠️ Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >=1.28.0 | Web framework |
| pandas | >=2.0.0 | Data manipulation |
| numpy | >=1.24.0 | Numerical computing |
| scikit-learn | >=1.3.0 | TF-IDF & similarity |

---

## 🎨 UI Design

### Color Palette
- **Primary Pink**: `#FFB6D9` - Main action elements
- **Soft Lilac**: `#E6D9FF` - Backgrounds & containers
- **Cream Background**: `#FFF8F5` - Main page background
- **Accent Peach**: `#FFDAB9` - Hover states
- **Dark Pink**: `#BB5D8C` - Text & headers

### Features
- Gradient backgrounds with soft shadows
- Rounded corners and smooth animations
- Emoji-based visual indicators
- Responsive card-based layout
- Cute pastel aesthetic throughout

---

## 💡 Usage Example

1. **Enter your skin needs**: 
   ```
   "My skin is dry, sensitive, and I get redness. I need a gentle moisturizer."
   ```

2. **Click "✨ Find My Skincare ✨"**
   - The AI analyzes your input
   - Returns top 5 matching products

3. **Explore results**:
   - View match percentage for each product
   - Read product descriptions
   - Use example searches for inspiration

---

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push origin main
   ```

2. **Visit [Streamlit Share](https://share.streamlit.io/)**
   - Click "New app"
   - Select your GitHub repo
   - Choose `main` branch and `app.py` as the main file
   - Deploy!

3. **Your app is live!** 🎉
   - Access via: `https://share.streamlit.io/[username]/skincare-recommendation/main/app.py`

---

## 📊 Model Details

### TF-IDF Configuration
- **Stop words**: English
- **Max features**: 5000
- **N-gram range**: (1, 2) - Unigrams & Bigrams
- **Similarity metric**: Cosine Similarity

### Demo Data
- 10 sample skincare products
- Each with review text for analysis
- Categories: moisturizers, cleansers, serums, masks, creams

### Similarity Thresholds
- **90%+ Match**: 🟢 Perfect match
- **70-89% Match**: 🟡 Great match
- **50-69% Match**: 🟠 Fairly suitable
- **<50% Match**: 🔴 May suit your needs

---

## 🔧 Customization

### Add Your Own Data

Replace demo data in `model.py`:

```python
def create_demo_data():
    demo_data = {
        "product_name": ["Your Product 1", "Your Product 2"],
        "review_text": ["Review text 1", "Review text 2"]
    }
    return pd.DataFrame(demo_data)
```

### Change Colors

Edit color palette in `app.py`:

```python
# Pink tones
PRIMARY_PINK = "#FFB6D9"
DARK_PINK = "#BB5D8C"

# Backgrounds
BG_CREAM = "#FFF8F5"
BG_SOFT_PINK = "#FFE6F0"
```

### Adjust Recommendations

Edit defaults in `config.py`:

```python
DEFAULT_TOP_N = 5  # Number of products to show
MIN_INPUT_LENGTH = 3  # Minimum character input
MAX_INPUT_LENGTH = 500  # Maximum character input
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError" when running app
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Port 8501 already in use
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### Model loading errors
```bash
# Clear cache and rebuild model
rm model_cache.pkl
streamlit run app.py
```

---

## 📝 Example Searches

Try these to see the recommendation system in action:

- ✨ **Skin Brightening**: "skin brightening, dark spots, dull skin"
- 💧 **Dry Skin**: "dry skin, dehydrated, needs moisturizer"
- 🧴 **Anti-Acne**: "acne-prone, oily skin, breakout"
- 🌸 **Sensitive Skin**: "sensitive skin, redness, irritation"
- 🎯 **Anti-Aging**: "wrinkles, fine lines, mature skin"

---

## 👨‍💻 Development

### Run tests
```bash
python test_setup.py
```

### Code structure
- **app.py**: 400+ lines of Streamlit UI and styling
- **model.py**: TF-IDF vectorization and recommendations
- **config.py**: Centralized configuration
- **utils.py**: Helper functions and utilities

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add more skincare products

---

## ✉️ Contact & Support

For questions or issues, please visit the [GitHub repository](https://github.com/maiamaiaa/skincare-recommendation) and open an issue.

---

## 🌟 Future Enhancements

- [ ] User ratings and feedback system
- [ ] Save favorite products
- [ ] Personalized recommendation history
- [ ] Integration with real product databases
- [ ] Mobile app version

---

## 🎁 Acknowledgments

- Built with **Streamlit** for beautiful web apps
- Powered by **scikit-learn** for ML algorithms
- Designed with a love for skincare and cute aesthetic ✨

---

**Made with 💖 for skincare lovers everywhere!**

Try it now: [https://share.streamlit.io/maiamaiaa/skincare-recommendation/main/app.py](https://share.streamlit.io/maiamaiaa/skincare-recommendation/main/app.py)
