"""
"""Configuration file for Skincare Recommendation App
Contains all constants and customizable configurations
"""

# ============================================================================
# APP CONFIGURATION
# ============================================================================

APP_TITLE = "✨ Skincare Recommender"
APP_SUBTITLE = "Find your dream skincare with AI"
APP_DESCRIPTION = "Skincare product recommendation system based on NLP with TF-IDF and Cosine Similarity"

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# TF-IDF Settings
TFIDF_STOP_WORDS = 'english'
TFIDF_MAX_FEATURES = 5000
TFIDF_NGRAM_RANGE = (1, 2)  # Unigram and Bigram

# Model Cache
USE_DEMO_DATA = True  # Set to False if using real data
DATA_PATH = None  # Path to CSV data folder (set if not using demo)
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
INPUT_PLACEHOLDER = """Example: oily skin, acne-prone, needs brightening
Or: dry sensitive skin, anti-aging, hydrating
Or: acne prone, oily T-zone, needs cleanser"""

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

# To determine emoji and message based on similarity score
SIMILARITY_THRESHOLDS = {
    'excellent': 0.85,    # Very suitable
    'good': 0.70,         # Suitable
    'fair': 0.50,         # Fairly suitable
}

SIMILARITY_LABELS = {
    'excellent': ('🟢', 'Perfect match for your needs!'),
    'good': ('🟡', 'Great match for your needs'),
    'fair': ('🟠', 'Fairly suitable for your needs'),
    'poor': ('🔴', 'May suit your needs'),
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
        'description': 'For dry skin'
    },
    {
        'display': '🔎 For Oily Skin',
        'query': 'oily skin acne prone',
        'description': 'For oily & acne-prone skin'
    },
    {
        'display': '🔎 For Brightening',
        'query': 'skin brightening dark spots',
        'description': 'For dull skin'
    }
]

# ============================================================================
# ERROR & SUCCESS MESSAGES
# ============================================================================

MESSAGES = {
    'empty_input': '❌ Please enter your skin care needs!',
    'short_input': f'❌ Description too short. Minimum {MIN_INPUT_LENGTH} characters.',
    'long_input': f'❌ Description too long. Maximum {MAX_INPUT_LENGTH} characters.',
    'model_error': '❌ An error occurred while processing. Please try again.',
    'no_results': '❌ No recommendations found.',
    'recommendations_found': '✅ Recommendations created successfully!',
    'data_loaded': '✅ Data loaded successfully!',
    'processing': '⏳ Analyzing your needs...',
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
