# World News — 26 November 2026, in one image (make.fun news-image-20261126).
# The entry is the PNG beside this file; this program only copies it to
# /output/entry.png, so two runs write byte-identical output. No network.
# Run locally with:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(here / "entry.png", out_dir / "entry.png")
