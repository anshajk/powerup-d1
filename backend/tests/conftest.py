import sys
from pathlib import Path

# Ensure the backend/app directory is on sys.path for test imports
ROOT = Path(__file__).resolve().parent.parent / "app"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
