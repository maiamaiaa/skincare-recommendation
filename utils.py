"""
Utility functions untuk Skincare Recommendation App
Helper functions untuk logging, debugging, dan utility lainnya
"""

import logging
import time
from functools import wraps
from datetime import datetime
import streamlit as st

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def log_function_call(func):
    """Decorator untuk log fungsi yang dipanggil"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function: {func.__name__}")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.info(f"Function {func.__name__} completed in {end_time - start_time:.2f}s")
            return result
        except Exception as e:
            logger.error(f"Error in function {func.__name__}: {str(e)}")
            raise
    return wrapper


def time_execution(func):
    """Decorator untuk mengukur waktu eksekusi"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


def format_percentage(value, decimal_places=1):
    """Format nilai menjadi persentase"""
    return f"{value * 100:.{decimal_places}f}%"


def get_similarity_emoji(score):
    """Dapatkan emoji berdasarkan similarity score"""
    if score >= 0.8:
        return "🟢"  # Green - Sangat cocok
    elif score >= 0.6:
        return "🟡"  # Yellow - Cocok
    elif score >= 0.4:
        return "🟠"  # Orange - Cukup cocok
    else:
        return "🔴"  # Red - Kurang cocok


def get_recommendation_message(score):
    """Dapatkan pesan rekomendasi berdasarkan score"""
    if score >= 0.85:
        return "Sangat cocok untuk kebutuhan Anda!"
    elif score >= 0.70:
        return "Cocok untuk kebutuhan Anda"
    elif score >= 0.50:
        return "Cukup cocok dengan kebutuhan Anda"
    else:
        return "Mungkin cocok dengan kebutuhan Anda"


def validate_text_input(text, min_length=3, max_length=500):
    """
    Validasi input teks dari user
    
    Args:
        text (str): Teks yang akan divalidasi
        min_length (int): Minimal panjang teks
        max_length (int): Maksimal panjang teks
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not text:
        return False, "Input tidak boleh kosong"
    
    text = text.strip()
    
    if len(text) < min_length:
        return False, f"Input minimal {min_length} karakter"
    
    if len(text) > max_length:
        return False, f"Input maksimal {max_length} karakter"
    
    return True, ""


def display_product_card_enhanced(product_name, similarity_score, description, rank, show_emoji=True):
    """
    Display product card dengan styling
    
    Args:
        product_name (str): Nama produk
        similarity_score (float): Score similarity (0-1)
        description (str): Deskripsi produk
        rank (int): Ranking produk
        show_emoji (bool): Apakah menampilkan emoji
    
    Returns:
        str: HTML string untuk ditampilkan
    """
    emoji = get_similarity_emoji(similarity_score) if show_emoji else ""
    percentage = format_percentage(similarity_score)
    bar_width = int(similarity_score * 100)
    
    html = f"""
    <div class="product-card">
        <div class="product-name">{emoji} #{rank} {product_name}</div>
        <div class="similarity-score">
            🎯 Kecocokan: {percentage}
        </div>
        <div class="score-bar" style="width: {bar_width}%"></div>
        <div class="product-description">
            {get_recommendation_message(similarity_score)}<br>
            <strong>Detail:</strong> {description}
        </div>
    </div>
    """
    return html


def get_stats_summary(recommendations_df):
    """
    Dapatkan summary statistics dari recommendations
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame dengan rekomendasi
        
    Returns:
        dict: Dictionary dengan stats
    """
    if recommendations_df is None or len(recommendations_df) == 0:
        return None
    
    scores = recommendations_df['similarity_score'].values
    
    stats = {
        'avg_score': scores.mean(),
        'max_score': scores.max(),
        'min_score': scores.min(),
        'std_score': scores.std(),
        'total_products': len(scores)
    }
    
    return stats


def print_app_info():
    """Print informasi aplikasi"""
    info = """
    ╔═══════════════════════════════════════════════════╗
    ║     Skincare Recommendation System                ║
    ║     Powered by TF-IDF & Cosine Similarity         ║
    ║                                                   ║
    ║     Version: 1.0.0                                ║
    ║     Framework: Streamlit                          ║
    ║     ML Model: Scikit-learn                        ║
    ╚═══════════════════════════════════════════════════╝
    """
    print(info)
    logger.info("Application started successfully")


def create_example_queries():
    """Buat list contoh query yang bagus"""
    return [
        {
            "query": "dry skin moisturizer",
            "label": "Untuk Kulit Kering",
            "description": "Perawatan untuk kulit kering dan dehidrasi"
        },
        {
            "query": "oily skin acne prone",
            "label": "Untuk Kulit Berminyak & Berjerawat",
            "description": "Perawatan untuk kulit berminyak dengan jerawat"
        },
        {
            "query": "skin brightening anti dark spots",
            "label": "Untuk Kulit Kusam",
            "description": "Produk pencerah dan penghilang noda hitam"
        },
        {
            "query": "sensitive skin gentle cleanser",
            "label": "Untuk Kulit Sensitif",
            "description": "Produk lembut untuk kulit sensitif"
        },
        {
            "query": "anti aging wrinkles fine lines",
            "label": "Untuk Anti-Aging",
            "description": "Produk untuk mengurangi kerutan dan garis halus"
        }
    ]


def export_recommendations_to_csv(recommendations_df, filename="recommendations.csv"):
    """
    Export recommendations ke CSV file untuk disimpan
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame dengan rekomendasi
        filename (str): Nama file output
        
    Returns:
        bytes: CSV file content
    """
    csv_content = recommendations_df.to_csv(index=False)
    return csv_content


# String templates untuk error dan success messages
ERROR_MESSAGES = {
    'empty_input': '❌ Mohon masukkan deskripsi kebutuhan kulit Anda!',
    'short_input': '❌ Deskripsi terlalu singkat. Minimal 3 karakter.',
    'long_input': '❌ Deskripsi terlalu panjang. Maksimal 500 karakter.',
    'model_error': '❌ Terjadi error saat memproses. Silakan coba lagi.',
    'no_results': '❌ Tidak ada rekomendasi yang ditemukan.'
}

SUCCESS_MESSAGES = {
    'recommendations_found': '✅ Rekomendasi berhasil dibuat!',
    'data_loaded': '✅ Data berhasil dimuat!',
    'model_ready': '✅ Model siap digunakan!'
}

INFO_MESSAGES = {
    'processing': '⏳ Menganalisis kebutuhan Anda...',
    'loading': '🔄 Sedang memproses...',
    'example_search': '💡 Mencoba pencarian contoh...'
}
