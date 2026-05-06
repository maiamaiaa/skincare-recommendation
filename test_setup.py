"""
Test script untuk verify Skincare Recommendation System
Jalankan dengan: python test_setup.py
"""

import sys
import os
from pathlib import Path

print("\n" + "="*60)
print("  SKINCARE RECOMMENDATION SYSTEM - SETUP TEST")
print("="*60 + "\n")

# Test 1: Check Python version
print("[1/5] Checking Python version...")
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 8:
    print(f"✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} - OK\n")
else:
    print(f"❌ Python {python_version.major}.{python_version.minor} - Need Python 3.8+\n")
    sys.exit(1)

# Test 2: Check required files
print("[2/5] Checking required files...")
required_files = ['app.py', 'model.py', 'config.py', 'utils.py', 'requirements.txt']
all_exist = True
for file in required_files:
    if Path(file).exists():
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} - NOT FOUND")
        all_exist = False

if all_exist:
    print()
else:
    print("\n❌ Some required files are missing!\n")
    sys.exit(1)

# Test 3: Check imports
print("[3/5] Checking package imports...")
packages = {
    'pandas': 'pd',
    'numpy': 'np',
    'sklearn': 'sklearn',
    'streamlit': 'st',
}

missing_packages = []
for package, alias in packages.items():
    try:
        __import__(package)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - NOT INSTALLED")
        missing_packages.append(package)

print()
if missing_packages:
    print(f"❌ Missing packages: {', '.join(missing_packages)}")
    print("   Run: pip install -r requirements.txt\n")
    sys.exit(1)

# Test 4: Load model configuration
print("[4/5] Testing model loading...")
try:
    # Import only if all packages available
    from model import load_or_create_model, get_recommendations, create_demo_data
    
    print("   Loading demo model...")
    tfidf_matrix, df_grouped, tfidf_vectorizer = load_or_create_model(use_demo=True)
    print(f"   ✅ Model loaded successfully")
    print(f"   ✅ {len(df_grouped)} products loaded")
    print()
except Exception as e:
    print(f"   ❌ Error loading model: {str(e)}\n")
    sys.exit(1)

# Test 5: Test recommendation function
print("[5/5] Testing recommendation function...")
try:
    test_input = "dry skin moisturizer"
    recommendations = get_recommendations(
        user_input=test_input,
        tfidf_matrix=tfidf_matrix,
        df_grouped=df_grouped,
        tfidf_vectorizer=tfidf_vectorizer,
        top_n=3
    )
    
    if recommendations is not None and len(recommendations) > 0:
        print(f"   ✅ Recommendations generated for '{test_input}'")
        print(f"   ✅ {len(recommendations)} products recommended")
        print("\n   Top recommendations:")
        for idx, row in recommendations.iterrows():
            print(f"      {idx+1}. {row['product_name']} ({row['similarity_score']:.1%})")
        print()
    else:
        print(f"   ⚠️  No recommendations found\n")
except Exception as e:
    print(f"   ❌ Error in recommendations: {str(e)}\n")
    sys.exit(1)

# Final status
print("="*60)
print("  ✅ ALL TESTS PASSED!")
print("="*60)
print("\n🚀 Ready to run:\n")
print("   streamlit run app.py\n")
print("="*60 + "\n")
