"""
Model module untuk Skincare Recommendation System
Berisi fungsi-fungsi untuk preprocessing, loading model, dan mendapatkan rekomendasi
"""

import pandas as pd
import numpy as np
import pickle
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text: str) -> str:
    """
    Preprocessing teks input dari user
    
    Args:
        text (str): Teks raw dari user
        
    Returns:
        str: Teks yang sudah diprocessing
    """
    text = text.lower().strip()
    return text


def load_or_create_model(data_path: str = None, use_demo: bool = False):
    """
    Load model yang sudah tersimpan atau membuat model baru dari data
    
    Args:
        data_path (str): Path ke folder data
        use_demo (bool): Jika True, gunakan demo data dengan produk dummy
        
    Returns:
        tuple: (tfidf_matrix, df_grouped, tfidf_vectorizer)
    """
    
    model_cache = Path("model_cache.pkl")
    
    # Jika ada cache model yang tersimpan, load dari sana
    if model_cache.exists() and not use_demo:
        try:
            with open(model_cache, 'rb') as f:
                cache_data = pickle.load(f)
            return cache_data['tfidf_matrix'], cache_data['df_grouped'], cache_data['tfidf_vectorizer']
        except:
            pass
    
    if use_demo:
        # Menggunakan demo data untuk testing
        df_grouped = create_demo_data()
    else:
        # Load dari CSV files jika data_path tersedia
        if data_path and os.path.exists(data_path):
            df_grouped = load_data_from_csv(data_path)
        else:
            # Fallback ke demo data
            print("⚠️ Data path tidak ditemukan, menggunakan demo data...")
            df_grouped = create_demo_data()
    
    # Buat TF-IDF Vectorizer
    tfidf = TfidfVectorizer(
        stop_words='english',
        max_features=5000,
        ngram_range=(1, 2)
    )
    
    # Fit dan transform
    tfidf_matrix = tfidf.fit_transform(df_grouped["review_text"])
    
    # Simpan ke cache
    if not use_demo:
        try:
            cache_data = {
                'tfidf_matrix': tfidf_matrix,
                'df_grouped': df_grouped,
                'tfidf_vectorizer': tfidf
            }
            with open(model_cache, 'wb') as f:
                pickle.dump(cache_data, f)
        except:
            pass
    
    return tfidf_matrix, df_grouped, tfidf


def load_data_from_csv(data_path: str):
    """
    Load data dari CSV files seperti di notebook original
    
    Args:
        data_path (str): Path ke folder data
        
    Returns:
        pd.DataFrame: Data yang sudah di-preprocess dan digroup
    """
    files = [
        "reviews_0-250_masked.csv",
        "reviews_250-500_masked.csv",
        "reviews_500-750_masked.csv",
        "reviews_750-1250_masked.csv",
        "reviews_1250-end_masked.csv"
    ]
    
    try:
        # Load reviews
        df_reviews = pd.concat(
            [pd.read_csv(os.path.join(data_path, f), encoding='latin-1') for f in files],
            ignore_index=True
        )
        
        # Load product info
        df_product = pd.read_csv(os.path.join(data_path, "product_info_skincare.csv"), encoding='latin-1')
        
        # Merge data
        df = pd.merge(df_reviews, df_product, on='product_id', how='left')
        df = df.rename(columns={"product_name_y": "product_name"})
        df = df[["product_id", "product_name", "review_text"]]
        
        # Preprocessing
        df = df.dropna(subset=["product_name", "review_text"])
        df["review_text"] = df["review_text"].astype(str).str.lower().str.strip()
        df = df.drop_duplicates().reset_index(drop=True)
        
        # Grouping by product name
        df_grouped = df.groupby("product_name")["review_text"] \
                       .apply(lambda x: " ".join(x)) \
                       .reset_index()
        
        return df_grouped
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return create_demo_data()


def create_demo_data():
    """
    Buat data demo untuk testing aplikasi
    
    Returns:
        pd.DataFrame: DataFrame dengan demo produk dan review
    """
    demo_data = {
        "product_name": [
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
        ],
        "review_text": [
            "very hydrating moisturizer perfect for dry skin keeps skin soft smooth all day long excellent for winter best product ever loved",
            "great face wash removes acne helps clear skin excellent antibacterial properties amazing for oily skin highly recommended by dermatologists",
            "brightening serum made skin glow instantly visible results after few days great for dark spots uneven skin tone love this product",
            "night cream incredible repair amazing for overnight skin recovery feels luxurious moisturizes deeply best night time product ever",
            "oil control toner perfect for oily skin mattifying effect lasts whole day balances skin pH great quality affordable price",
            "vitamin c face wash brightening cleansing excellent antioxidant protection fresh feeling best morning routine product",
            "sensitive skin balm gentle soothing calming irritation perfect for reactive skin dermatologist tested hypoallergenic love it",
            "deep pore cleanser removes blackheads thoroughly clean feeling powerful yet gentle best deep cleaning product highly effective",
            "hydrating face mask moisturizing nourishing spa treatment at home relaxing amazing for dry skin healing benefits",
            "anti aging eye cream reduces wrinkles fine lines brightens dark circles around eyes lifting effect noticeable results visible"
        ]
    }
    
    return pd.DataFrame(demo_data)


def get_recommendations(user_input: str, tfidf_matrix, df_grouped, tfidf_vectorizer, top_n: int = 5):
    """
    Dapatkan rekomendasi produk berdasarkan input user
    
    Args:
        user_input (str): Input teks dari user
        tfidf_matrix: TF-IDF matrix yang sudah di-fit
        df_grouped (pd.DataFrame): Data produk yang sudah digroup
        tfidf_vectorizer: TF-IDF vectorizer
        top_n (int): Jumlah rekomendasi yang ingin ditampilkan
        
    Returns:
        pd.DataFrame: DataFrame berisi rekomendasi produk dengan similarity score
    """
    
    if not user_input.strip():
        return None
    
    # Preprocess input
    processed_input = preprocess_text(user_input)
    
    # Transform input user
    user_vec = tfidf_vectorizer.transform([processed_input])
    
    # Hitung cosine similarity
    sim_scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Ambil top N
    top_scores = sim_scores[:top_n]
    
    product_indices = [i[0] for i in top_scores]
    similarity_scores = [i[1] for i in top_scores]
    
    # Buat hasil dataframe
    hasil = df_grouped.iloc[product_indices][["product_name"]].copy()
    hasil["similarity_score"] = similarity_scores
    hasil = hasil.reset_index(drop=True)
    
    return hasil


def get_product_details(product_name: str, df_grouped: pd.DataFrame) -> str:
    """
    Dapatkan detail produk berdasarkan nama
    
    Args:
        product_name (str): Nama produk
        df_grouped (pd.DataFrame): Data produk
        
    Returns:
        str: Detail produk (review text)
    """
    product = df_grouped[df_grouped["product_name"] == product_name]
    if len(product) > 0:
        review_text = product["review_text"].values[0]
        # Ambil summary dari review (first 150 characters)
        return review_text[:150] + "..." if len(review_text) > 150 else review_text
    return "No details available"
