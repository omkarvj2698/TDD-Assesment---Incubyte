import sys
from pathlib import Path

# add the repo's /src directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))