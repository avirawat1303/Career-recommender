"""
Test if ML model imports work
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

print("Testing imports...")

try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ml_model'))
    from predict import predict_careers
    print("✓ predict_careers imported successfully")
    
    from career_data import CAREER_LIST
    print(f"✓ career_data imported successfully ({len(CAREER_LIST)} careers)")
    
    print("\n✓ All imports successful!")
    
except ImportError as e:
    print(f"\n✗ Import failed: {e}")
    print("\nTroubleshooting:")
    print("1. Check if ml_model/__init__.py exists")
    print("2. Check if ml_model/predict.py exists")
    print("3. Check if ml_model/career_data.py exists")