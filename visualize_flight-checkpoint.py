#!/usr/bin/env python3
"""
visualize_flight.py
-------------------
Launches a Jupyter notebook that shares this script's name.
If the notebook doesn't exist yet, it creates one with a starter
cell that imports the same code — so you can iterate inside the
notebook without losing your original script.
"""

import os
import sys
import json
import subprocess
import pathlib

# ── 1. Derive the notebook name from this script's filename ──────────────────
SCRIPT_PATH   = pathlib.Path(__file__).resolve()
NOTEBOOK_NAME = SCRIPT_PATH.stem + ".ipynb"          # visualize_flight.ipynb
NOTEBOOK_DIR  = SCRIPT_PATH.parent                   # same folder as script
NOTEBOOK_PATH = NOTEBOOK_DIR / NOTEBOOK_NAME

# ── 2. Create the notebook if it doesn't exist ───────────────────────────────
def create_notebook(path: pathlib.Path, script_path: pathlib.Path) -> None:
    """Build a minimal .ipynb with a helpful starter cell."""

    starter_code = (
        f"# Auto-generated notebook for: {script_path.name}\n"
        f"# Run the cells below to execute the flight visualisation.\n\n"
        f"# Uncomment the next line to run the whole script at once:\n"
        f"# %run '{script_path}'\n\n"
        f"# ── Or paste / import individual sections here ──────────────────\n"
        f"from dronekit import connect, VehicleMode\n"
        f"import matplotlib.pyplot as plt\n"
        f"from mpl_toolkits.mplot3d import Axes3D\n"
        f"import time\n\n"
        f"print('Notebook ready.  Edit cells below to start.')\n"
    )

    notebook = {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "cells": [
            {
                "cell_type": "markdown",
                "id": "title-cell",
                "metadata": {},
                "source": [
                    f"# {script_path.stem.replace('_', ' ').title()}\n",
                    f"Notebook auto-created from `{script_path.name}`."
                ]
            },
            {
                "cell_type": "code",
                "id": "starter-cell",
                "metadata": {},
                "execution_count": None,
                "outputs": [],
                "source": [starter_code]
            }
        ]
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)

    print(f"[+] Created notebook: {path}")


# ── 3. Open the notebook in Jupyter ──────────────────────────────────────────
def open_notebook(path: pathlib.Path) -> None:
    """
    Try jupyter notebook first, fall back to jupyter lab.
    Both are launched as a background subprocess so this script exits cleanly.
    """
    for cmd in (["jupyter", "notebook", str(path)],
                ["jupyter", "lab",      str(path)]):
        try:
            print(f"[+] Launching: {' '.join(cmd)}")
            subprocess.Popen(
                cmd,
                cwd=str(path.parent),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print(f"[+] Jupyter is starting — check your browser.")
            print(f"    Notebook: {path}")
            return
        except FileNotFoundError:
            continue

    # Neither found
    print("[!] Could not find 'jupyter notebook' or 'jupyter lab'.")
    print("    Install with:  pip install notebook   or   pip install jupyterlab")
    sys.exit(1)


# ── 4. Main ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"[*] Script : {SCRIPT_PATH}")
    print(f"[*] Notebook: {NOTEBOOK_PATH}")

    if not NOTEBOOK_PATH.exists():
        print("[*] Notebook not found — creating it...")
        create_notebook(NOTEBOOK_PATH, SCRIPT_PATH)
    else:
        print("[*] Notebook already exists — opening it.")

    open_notebook(NOTEBOOK_PATH)
