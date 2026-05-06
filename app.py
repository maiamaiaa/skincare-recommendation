"""
Streamlit App - Skincare Recommendation System
Aplikasi web modern untuk memberikan rekomendasi produk skincare berdasarkan input user
"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import time
from model import load_or_create_model, get_recommendations, get_product_details, preprocess_text

# ============================================================================
# PAGE CONFIG & STYLING
# ============================================================================

st.set_page_config(
    page_title="Skincare Recommendation System",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling modern
custom_css = """
<style>
    /* General Styling */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Remove default streamlit styling */
    .stMainBlockContainer {
        padding-top: 2rem;
    }
    
    /* Header Styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
        text-align: center;
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        opacity: 0.95;
        font-weight: 300;
    }
    
    /* Input Container */
    .input-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        border-left: 5px solid #667eea;
    }
    
    /* Product Card Styling */
    .product-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out;
    }
    
    .product-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        border-left-color: #764ba2;
    }
    
    .product-name {
        font-size: 1.3rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .similarity-score {
        font-size: 0.95rem;
        color: #667eea;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    
    .score-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 8px;
        border-radius: 4px;
        margin-bottom: 1rem;
    }
    
    .product-description {
        font-size: 0.9rem;
        color: #666;
        line-height: 1.6;
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 3rem 2rem;
        color: #999;
        font-style: italic;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3) !important;
    }
    
    /* Results Container */
    .results-container {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Loading Spinner Styling */
    .loading-text {
        font-size: 1.1rem;
        color: #667eea;
        font-weight: 600;
        text-align: center;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================

@st.cache_resource
def load_model_cache():
    """Load model sekali saja dan cache untuk session"""
    return load_or_create_model(use_demo=True)

# Load model
tfidf_matrix, df_grouped, tfidf_vectorizer = load_model_cache()

# ============================================================================
# HEADER SECTION
# ============================================================================

header_html = """
<div class="header-container">
    <div class="header-title">✨ Skincare Recommender</div>
    <div class="header-subtitle">Turunkan skidcare impian Anda dengan AI</div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# ============================================================================
# INFO SECTION
# ============================================================================

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📦 Total Products", len(df_grouped), "Ready to recommend")
    
    with col2:
        st.metric("🤖 AI Model", "TF-IDF", "Cosine Similarity")
    
    with col3:
        st.metric("📊 Features", "5000", "Text features")

# ============================================================================
# INPUT SECTION
# ============================================================================

st.markdown("---")

input_col1, input_col2 = st.columns([3, 1])

with input_col1:
    user_input = st.text_area(
        label="🔍 Apa kebutuhan kulit Anda?",
        placeholder="Contoh: kulit berminyak, berjerawat, butuh skincare untuk mencerahkan, sensitif, dry skin, anti-aging, dll...",
        height=100,
        help="Deskripsikan kebutuhan atau masalah kulit Anda dengan detail"
    )

with input_col2:
    # Spacer untuk alignment
    st.write("")
    st.write("")
    recommend_button = st.button("🚀 Rekomendasikan", use_container_width=True)

# ============================================================================
# RESULTS SECTION
# ============================================================================

if recommend_button:
    # Validasi input
    if not user_input.strip():
        st.error("❌ Mohon masukkan deskripsi kebutuhan kulit Anda!")
    else:
        # Loading state
        with st.spinner("⏳ Analisis kebutuhan Anda..."):
            time.sleep(0.5)  # Simulasi processing
            
            # Get recommendations
            recommendations = get_recommendations(
                user_input=user_input,
                tfidf_matrix=tfidf_matrix,
                df_grouped=df_grouped,
                tfidf_vectorizer=tfidf_vectorizer,
                top_n=5
            )
        
        # Success message
        st.success("✅ Rekomendasi berhasil dibuat!")
        
        # Display results
        st.markdown("### 🎯 Rekomendasi Produk Untuk Anda:")
        
        if recommendations is not None and len(recommendations) > 0:
            for idx, row in recommendations.iterrows():
                product_name = row["product_name"]
                similarity_score = row["similarity_score"]
                
                # Create product card
                card_html = f"""
                <div class="product-card">
                    <div class="product-name">#{idx + 1} {product_name}</div>
                    <div class="similarity-score">
                        🎯 Kecocokan: {similarity_score:.1%}
                    </div>
                    <div class="score-bar" style="width: {similarity_score * 100}%"></div>
                    <div class="product-description">
                        <strong>Deskripsi:</strong> {get_product_details(product_name, df_grouped)}
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Tidak ada rekomendasi yang ditemukan untuk input Anda. Coba deskripsi yang lebih detail!")

# ============================================================================
# EXAMPLE QUERIES SECTION
# ============================================================================

st.markdown("---")

st.markdown("### 💡 Contoh Pencarian:")

col1, col2, col3 = st.columns(3)

example_queries = [
    ("skin brightening", "Untuk kulit kusam"),
    ("dry skin moisturizer", "Untuk kulit kering"),
    ("acne face wash", "Untuk kulit berjerawat")
]

for col, (query, description) in zip([col1, col2, col3], example_queries):
    with col:
        if st.button(f"🔎 {description}", key=query, use_container_width=True):
            st.session_state.example_query = query
            st.rerun()

if "example_query" in st.session_state:
    user_input = st.session_state.example_query
    with st.spinner("⏳ Analisis kebutuhan Anda..."):
        time.sleep(0.5)
        recommendations = get_recommendations(
            user_input=user_input,
            tfidf_matrix=tfidf_matrix,
            df_grouped=df_grouped,
            tfidf_vectorizer=tfidf_vectorizer,
            top_n=5
        )
    
    st.success("✅ Rekomendasi berhasil dibuat!")
    st.markdown("### 🎯 Rekomendasi Produk:")
    
    if recommendations is not None and len(recommendations) > 0:
        for idx, row in recommendations.iterrows():
            product_name = row["product_name"]
            similarity_score = row["similarity_score"]
            
            card_html = f"""
            <div class="product-card">
                <div class="product-name">#{idx + 1} {product_name}</div>
                <div class="similarity-score">
                    🎯 Kecocokan: {similarity_score:.1%}
                </div>
                <div class="score-bar" style="width: {similarity_score * 100}%"></div>
                <div class="product-description">
                    <strong>Deskripsi:</strong> {get_product_details(product_name, df_grouped)}
                </div>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
    
    del st.session_state.example_query

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")

footer_html = """
<div style="text-align: center; color: #999; font-size: 0.9rem; margin-top: 2rem;">
    <p>✨ Powered by TF-IDF & Cosine Similarity | NLP Skincare Recommendation System</p>
    <p style="margin-top: 0.5rem;">Built with ❤️ using Streamlit</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
