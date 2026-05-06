"""
Utility functions for Skincare Recommendation App
Helper functions for logging, debugging, and other utilities
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
    """Decorator to log called functions"""
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
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


def format_percentage(value, decimal_places=1):
    """Format value as percentage"""
    return f"{value * 100:.{decimal_places}f}%"


def get_similarity_emoji(score):
    """Get emoji based on similarity score"""
    if score >= 0.8:
        return "🟢"  # Green - Very suitable
    elif score >= 0.6:
        return "🟡"  # Yellow - Suitable
    elif score >= 0.4:
        return "🟠"  # Orange - Fairly suitable
    else:
        return "🔴"  # Red - Less suitable


def get_recommendation_message(score):
    """Get recommendation message based on score"""
    if score >= 0.85:
        return "Perfect match for your needs!"
    elif score >= 0.70:
        return "Great match for your needs"
    elif score >= 0.50:
        return "Fairly suitable for your needs"
    else:
        return "May suit your needs"


def validate_text_input(text, min_length=3, max_length=500):
    """
    Validate user text input
    
    Args:
        text (str): Text to validate
        min_length (int): Minimum text length
        max_length (int): Maximum text length
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not text:
        return False, "Input cannot be empty"
    
    text = text.strip()
    
    if len(text) < min_length:
        return False, f"Input must be at least {min_length} characters"
    
    if len(text) > max_length:
        return False, f"Input cannot exceed {max_length} characters"
    
    return True, ""


def display_product_card_enhanced(product_name, similarity_score, description, rank, show_emoji=True):
    """
    Display product card with styling
    
    Args:
        product_name (str): Product name
        similarity_score (float): Similarity score (0-1)
        description (str): Product description
        rank (int): Product ranking
        show_emoji (bool): Whether to show emoji
    
    Returns:
        str: HTML string to display
    """
    emoji = get_similarity_emoji(similarity_score) if show_emoji else ""
    percentage = format_percentage(similarity_score)
    bar_width = int(similarity_score * 100)
    
    html = f"""
    <div class="product-card">
        <div class="product-name">{emoji} #{rank} {product_name}</div>
        <div class="similarity-score">
            🎯 Match: {percentage}
        </div>
        <div class="score-bar" style="width: {bar_width}%"></div>
        <div class="product-description">
            {get_recommendation_message(similarity_score)}<br>
            <strong>Details:</strong> {description}
        </div>
    </div>
    """
    return html


def get_stats_summary(recommendations_df):
    """
    Get summary statistics from recommendations
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame with recommendations
        
    Returns:
        dict: Dictionary with stats
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
    """Create list of good example queries"""
    return [
        {
            "query": "dry skin moisturizer",
            "label": "For Dry Skin",
            "description": "Care for dry and dehydrated skin"
        },
        {
            "query": "oily skin acne prone",
            "label": "For Oily & Acne-Prone Skin",
            "description": "Care for oily skin with acne"
        },
        {
            "query": "skin brightening anti dark spots",
            "label": "For Dull Skin",
            "description": "Brightening products and dark spot removers"
        },
        {
            "query": "sensitive skin gentle cleanser",
            "label": "For Sensitive Skin",
            "description": "Gentle products for sensitive skin"
        },
        {
            "query": "anti aging wrinkles fine lines",
            "label": "For Anti-Aging",
            "description": "Products to reduce wrinkles and fine lines"
        }
    ]


def export_recommendations_to_csv(recommendations_df, filename="recommendations.csv"):
    """
    Export recommendations to CSV file for saving
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame with recommendations
        filename (str): Output file name
        
    Returns:
        bytes: CSV file content
    """
    csv_content = recommendations_df.to_csv(index=False)
    return csv_content


# String templates for error and success messages
ERROR_MESSAGES = {
    'empty_input': '❌ Please enter your skin care needs description!',
    'short_input': '❌ Description too short. Minimum 3 characters.',
    'long_input': '❌ Description too long. Maximum 500 characters.',
    'model_error': '❌ An error occurred while processing. Please try again.',
    'no_results': '❌ No recommendations found.'
}

SUCCESS_MESSAGES = {
    'recommendations_found': '✅ Recommendations created successfully!',
    'data_loaded': '✅ Data loaded successfully!',
    'model_ready': '✅ Model ready to use!'
}

INFO_MESSAGES = {
    'processing': '⏳ Analyzing your needs...',
    'loading': '🔄 Processing...',
    'example_search': '💡 Trying example search...'
}
