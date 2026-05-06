"""
✨ Skincare Beauty Finder - Cute & Feminine UI
Cute skincare recommendation app with soft pastel aesthetic
"""

import streamlit as st
import time
from model import load_or_create_model, get_recommendations, get_product_details, preprocess_text

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="Skincare Beauty Finder ✨",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUTE PASTEL STYLING
# ============================================================================

cute_css = """
<style>
    /* Global Background - Soft Cream */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #FFF8F5 0%, #FFF5F7 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #FFE6F0 0%, #F0E6FF 100%);
    }
    
    /* Main Container */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* ===== HEADER STYLING ===== */
    .header-cute {
        background: linear-gradient(135deg, #FFB6D9 0%, #E6D9FF 100%);
        padding: 2.5rem 2rem;
        border-radius: 25px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(255, 182, 217, 0.25);
        text-align: center;
        border: 2px solid rgba(255, 255, 255, 0.8);
    }
    
    .header-title-cute {
        font-size: 2.8rem;
        font-weight: 800;
        color: #FF69B4;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }
    
    .header-subtitle-cute {
        font-size: 1.1rem;
        color: #BB5D8C;
        font-weight: 500;
        font-style: italic;
    }
    
    /* ===== INPUT CONTAINER ===== */
    .input-cute {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(255, 182, 217, 0.15);
        margin-bottom: 1.5rem;
        border: 2px solid #FFE6F0;
        transition: all 0.3s ease;
    }
    
    .input-cute:hover {
        box-shadow: 0 10px 30px rgba(255, 182, 217, 0.25);
        border-color: #FFB6D9;
    }
    
    /* ===== BUTTON STYLING ===== */
    .stButton > button {
        background: linear-gradient(135deg, #FFB6D9 0%, #DDA0DD 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 1rem 2rem !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(255, 182, 217, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(255, 182, 217, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    /* ===== PRODUCT CARDS ===== */
    .product-cute {
        background: linear-gradient(135deg, #FFFACD 0%, #FFE6F0 100%);
        border-radius: 20px;
        padding: 1.8rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 6px 20px rgba(255, 182, 217, 0.2);
        border: 2px solid rgba(255, 182, 217, 0.3);
        transition: all 0.3s ease;
        animation: float-in 0.5s ease-out;
    }
    
    .product-cute:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(255, 182, 217, 0.35);
        border-color: #FFB6D9;
    }
    
    .product-name-cute {
        font-size: 1.35rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF69B4, #DDA0DD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.8rem;
    }
    
    .score-cute {
        font-size: 1rem;
        color: #BB5D8C;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .score-bar-cute {
        background: linear-gradient(90deg, #FFB6D9 0%, #DDA0DD 100%);
        height: 10px;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .product-desc-cute {
        font-size: 0.95rem;
        color: #555;
        line-height: 1.7;
        font-style: italic;
    }
    
    /* ===== SUGGESTION BUTTONS ===== */
    .suggestion-btn {
        background: linear-gradient(135deg, #FFDAB9 0%, #FFE6F0 100%);
        color: #BB5D8C;
        border: 2px solid #FFB6D9;
        padding: 0.8rem 1.5rem;
        border-radius: 15px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .suggestion-btn:hover {
        background: linear-gradient(135deg, #FFB6D9 0%, #DDA0DD 100%);
        color: white;
        transform: scale(1.05);
        box-shadow: 0 6px 15px rgba(255, 182, 217, 0.3);
    }
    
    /* ===== METRICS ===== */
    .metric-cute {
        background: linear-gradient(135deg, #E6D9FF 0%, #FFE6F0 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255, 182, 217, 0.15);
        border: 2px solid rgba(255, 182, 217, 0.2);
        text-align: center;
    }
    
    /* ===== ANIMATIONS ===== */
    @keyframes float-in {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fade-in {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    /* ===== TEXT COLORS ===== */
    h1, h2, h3 {
        color: #BB5D8C !important;
    }
    
    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #FFE6F0 0%, #F0E6FF 100%) !important;
        border-radius: 12px !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #FFB6D9 0%, #E6D9FF 100%) !important;
    }
</style>
"""

st.markdown(cute_css, unsafe_allow_html=True)

# ============================================================================
# INITIALIZE SESSION STATE
# ============================================================================

@st.cache_resource
def load_model_cache():
    """Load model once and cache for session"""
    return load_or_create_model(use_demo=True)

# Load model
tfidf_matrix, df_grouped, tfidf_vectorizer = load_model_cache()

# ============================================================================
# HEADER SECTION
# ============================================================================

header_html = """
<div class="header-cute">
    <h1 style="margin: 0; color: white; font-size: 2.5rem; text-align: center;">💖 Skincare Beauty Finder ✨</h1>
    <p style="margin: 0.5rem 0 0 0; color: rgba(255, 255, 255, 0.95); font-size: 1.1rem; text-align: center;">Find your perfect skincare with AI help 🌸</p>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# ============================================================================
# INFO SECTION
# ============================================================================

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🧴 Total Products", len(df_grouped), "Ready to Recommend")
    
    with col2:
        st.metric("🤖 AI Model", "TF-IDF", "Cosine Similarity")
    
    with col3:
        st.metric("📊 Features", "5000", "Text Features")

# ============================================================================
# INPUT SECTION
# ============================================================================

st.markdown("---")

input_col1, input_col2 = st.columns([3, 1])

with input_col1:
    user_input = st.text_area(
        label="🔍 Tell Us Your Skin Needs",
        placeholder="Example: oily skin, acne-prone, dull, sensitive, dry skin, anti-aging, wrinkles, hyperpigmentation, etc....",
        height=100,
        help="Describe your skin concerns and needs so AI can give you the best recommendations 💖"
    )

with input_col2:
    # Spacing for alignment
    st.write("")
    st.write("")
    recommend_button = st.button("✨ Find My Skincare ✨", use_container_width=True)

# ============================================================================
# RESULTS SECTION
# ============================================================================

if recommend_button:
    # Validate input
    if not user_input.strip():
        st.error("❌ Please enter your skin needs description!")
    else:
        # Loading state
        with st.spinner("⏳ Analyzing your needs..."):
            time.sleep(0.5)  # Simulating processing time
            
            # Get recommendations
            recommendations = get_recommendations(
                user_input=user_input,
                tfidf_matrix=tfidf_matrix,
                df_grouped=df_grouped,
                tfidf_vectorizer=tfidf_vectorizer,
                top_n=5
            )
        
        # Success message
        st.success("✅ Recommendations created successfully!")
        
        # Display results
        st.markdown("### 🎯 Product Recommendations For You:")
        
        if recommendations is not None and len(recommendations) > 0:
            for idx, row in recommendations.iterrows():
                product_name = row["product_name"]
                similarity_score = row["similarity_score"]
                
                # Create product card
                card_html = f"""
                <div class="product-cute">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div style="font-size: 1.3rem; font-weight: bold; color: #BB5D8C;">💅 #{idx + 1} {product_name}</div>
                        <div style="background: linear-gradient(135deg, #FFB6D9, #DDA0DD); color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">{similarity_score:.1%} Match 🎯</div>
                    </div>
                    <div style="background: linear-gradient(90deg, #FFB6D9 0%, #FFB6D9 {similarity_score * 100}%, #FFE6F0 {similarity_score * 100}%, #FFE6F0 100%); height: 6px; border-radius: 10px; margin-bottom: 0.8rem;"></div>
                    <div style="color: #666; line-height: 1.6; font-size: 0.95rem;">
                        <strong>✨ Description:</strong> {get_product_details(product_name, df_grouped)}
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            st.warning("⚠️ No recommendations found for your input. Try a more detailed description!")

# ============================================================================
# EXAMPLE QUERIES SECTION
# ============================================================================

st.markdown("---")

st.markdown("### 💡 Try Example Searches:")

col1, col2, col3 = st.columns(3)

example_queries = [
    ("skin brightening", "🌟 Skin Brightening"),
    ("dry skin moisturizer", "💧 Dry Skin"),
    ("acne face wash", "🧴 Anti Acne")
]

for col, (query, description) in zip([col1, col2, col3], example_queries):
    with col:
        if st.button(description, key=query, use_container_width=True):
            st.session_state.example_query = query
            st.rerun()

if "example_query" in st.session_state:
    user_input = st.session_state.example_query
    with st.spinner("⏳ Analyzing your needs..."):
        time.sleep(0.5)
        recommendations = get_recommendations(
            user_input=user_input,
            tfidf_matrix=tfidf_matrix,
            df_grouped=df_grouped,
            tfidf_vectorizer=tfidf_vectorizer,
            top_n=5
        )
    
    st.success("✅ Recommendations created successfully!")
    st.markdown("### 🎯 Product Recommendations:")
    
    if recommendations is not None and len(recommendations) > 0:
        for idx, row in recommendations.iterrows():
            product_name = row["product_name"]
            similarity_score = row["similarity_score"]
            
            card_html = f"""
            <div class="product-cute">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <div style="font-size: 1.3rem; font-weight: bold; color: #BB5D8C;">💅 #{idx + 1} {product_name}</div>
                    <div style="background: linear-gradient(135deg, #FFB6D9, #DDA0DD); color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem; font-weight: bold;">{similarity_score:.1%} Match 🎯</div>
                </div>
                <div style="background: linear-gradient(90deg, #FFB6D9 0%, #FFB6D9 {similarity_score * 100}%, #FFE6F0 {similarity_score * 100}%, #FFE6F0 100%); height: 6px; border-radius: 10px; margin-bottom: 0.8rem;"></div>
                <div style="color: #666; line-height: 1.6; font-size: 0.95rem;">
                    <strong>✨ Description:</strong> {get_product_details(product_name, df_grouped)}
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
<div style="text-align: center; margin-top: 2rem; padding: 1.5rem; background: linear-gradient(135deg, #FFE6F0 0%, #F0E6FF 100%); border-radius: 20px;">
    <p style="margin: 0; font-size: 1rem; color: #BB5D8C; font-weight: bold;">✨ Skincare Bestie Finder ✨</p>
    <p style="margin: 0.5rem 0 0 0; color: #999; font-size: 0.9rem;">💖 Powered by AI (TF-IDF & Cosine Similarity)</p>
    <p style="margin: 0.3rem 0 0 0; color: #999; font-size: 0.85rem;">Built with ❤️ using Streamlit | NLP Skincare Recommendation System</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
