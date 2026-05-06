"""
Configuration file untuk Skincare Recommendation App
Berisi semua konstanta dan konfigurasi yang dapat disesuaikan
"""

# ============================================================================
# APP CONFIGURATION
# ============================================================================

APP_TITLE = "✨ Skincare Recommender"
APP_SUBTITLE = "Turunkan skincare impian Anda dengan AI"
APP_DESCRIPTION = "Sistem rekomendasi produk skincare berbasis NLP dengan TF-IDF dan Cosine Similarity"

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# TF-IDF Settings
TFIDF_STOP_WORDS = 'english'
TFIDF_MAX_FEATURES = 5000
TFIDF_NGRAM_RANGE = (1, 2)  # Unigram dan Bigram

# Model Cache
USE_DEMO_DATA = True  # Set ke False jika menggunakan data asli
DATA_PATH = None  # Path ke folder data CSV (set jika tidak pakai demo)
MODEL_CACHE_FILE = "model_cache.pkl"

# ============================================================================
# UI CONFIGURATION
# ============================================================================

# Default number of recommendations
DEFAULT_TOP_N = 5

# Input constraints
MIN_INPUT_LENGTH = 3
MAX_INPUT_LENGTH = 500

# Placeholder text
INPUT_PLACEHOLDER = """Contoh: kulit berminyak, berjerawat, butuh skincare untuk mencerahkan
Atau: dry sensitive skin, anti-aging, hydrating
Atau: acne prone, oily T-zone, needs cleanser"""

# ============================================================================
# STYLING & COLORS
# ============================================================================

# Primary Color Palette
PRIMARY_COLOR = "#667eea"  # Purple
SECONDARY_COLOR = "#764ba2"  # Darker Purple
ACCENT_COLOR = "#00d4ff"  # Cyan

# Background Colors
BG_COLOR_PRIMARY = "#f5f7fa"  # Light Blue
BG_COLOR_SECONDARY = "#c3cfe2"  # Medium Blue
BG_COLOR_CARD = "#ffffff"  # White

# Text Colors
TEXT_PRIMARY = "#333333"
TEXT_SECONDARY = "#666666"
TEXT_LIGHT = "#999999"

# ============================================================================
# EMOJI MAPPING
# ============================================================================

EMOJI_ICONS = {
    'search': '🔍',
    'recommend': '🚀',
    'similarity': '🎯',
    'product': '📦',
    'rating': '⭐',
    'loading': '⏳',
    'success': '✅',
    'error': '❌',
    'info': 'ℹ️',
    'features': '🎨',
    'model': '🤖',
    'data': '📊',
    'example': '💡',
    'demo': '🎭',
}

# ============================================================================
# SIMILARITY SCORE THRESHOLDS
# ============================================================================

# Untuk menentukan emoji dan pesan berdasarkan similarity score
SIMILARITY_THRESHOLDS = {
    'excellent': 0.85,    # Sangat cocok
    'good': 0.70,         # Cocok
    'fair': 0.50,         # Cukup cocok
}

SIMILARITY_LABELS = {
    'excellent': ('🟢', 'Sangat cocok untuk kebutuhan Anda!'),
    'good': ('🟡', 'Cocok untuk kebutuhan Anda'),
    'fair': ('🟠', 'Cukup cocok dengan kebutuhan Anda'),
    'poor': ('🔴', 'Mungkin cocok dengan kebutuhan Anda'),
}

# ============================================================================
# PAGE LAYOUT
# ============================================================================

# Streamlit page config
PAGE_CONFIG = {
    'page_title': 'Skincare Recommendation System',
    'page_icon': '✨',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# ============================================================================
# EXAMPLE QUERIES
# ============================================================================

EXAMPLE_QUERIES = [
    {
        'display': '🔎 For Dry Skin',
        'query': 'dry skin moisturizer',
        'description': 'Untuk kulit kering'
    },
    {
        'display': '🔎 For Oily Skin',
        'query': 'oily skin acne prone',
        'description': 'Untuk kulit berminyak & berjerawat'
    },
    {
        'display': '🔎 For Brightening',
        'query': 'skin brightening dark spots',
        'description': 'Untuk kulit kusam'
    }
]

# ============================================================================
# ERROR & SUCCESS MESSAGES
# ============================================================================

MESSAGES = {
    'empty_input': '❌ Mohon masukkan deskripsi kebutuhan kulit Anda!',
    'short_input': f'❌ Deskripsi terlalu singkat. Minimal {MIN_INPUT_LENGTH} karakter.',
    'long_input': f'❌ Deskripsi terlalu panjang. Maksimal {MAX_INPUT_LENGTH} karakter.',
    'model_error': '❌ Terjadi error saat memproses. Silakan coba lagi.',
    'no_results': '❌ Tidak ada rekomendasi yang ditemukan.',
    'recommendations_found': '✅ Rekomendasi berhasil dibuat!',
    'data_loaded': '✅ Data berhasil dimuat!',
    'processing': '⏳ Menganalisis kebutuhan Anda...',
}

# ============================================================================
# METRICS CONFIGURATION
# ============================================================================

METRICS = {
    'total_products': f"{EMOJI_ICONS['product']} Total Products",
    'ai_model': f"{EMOJI_ICONS['model']} AI Model",
    'features': f"{EMOJI_ICONS['data']} Features"
}

# ============================================================================
# OPTIMIZATION
# ============================================================================

# Cache settings
CACHE_EXPIRATION = 3600  # Seconds (1 hour)
USE_CACHE = True

# Performance
SHOW_PROCESSING_TIME = True
PROCESSING_TIME_THRESHOLD = 1.0  # seconds

# ============================================================================
# LOGGING
# ============================================================================

LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'app.log'

# ============================================================================
# DEMO DATA
# ============================================================================

DEMO_PRODUCTS = [
    "Hydrating Moisturizer",
    "Anti-Acne Face Wash",
    "Brightening Serum",
    "Night Repair Cream",
    "Oil Control Toner",
    "Vitamin C Cleanser",
    "Sensitive Skin Balm",
    "Deep Pore Cleanser",
    "Hydrating Face Mask",
    "Anti-Aging Eye Cream"
]
