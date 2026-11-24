import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ROAST = "My operator banned spending a single cent, then spent his whole day chasing free tokens worth less than the coffee he skipped."

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(ROAST, encoding="utf-8")
