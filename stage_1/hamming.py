#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: f_densityPlot.ipynb
Conversion Date: 2025-11-09T05:20:19.916Z
"""

def hamming_distance(seq1, seq2):
    # --- Step 1: Clean inputs ---
    seq1 = seq1.replace(" ", "").replace("\n", "").upper()
    seq2 = seq2.replace(" ", "").replace("\n", "").upper()
    
    # --- Step 2: Make both sequences the same length ---
    if len(seq1) < len(seq2):
        seq1 += "0" * (len(seq2) - len(seq1))
    elif len(seq2) < len(seq1):
        seq2 += "0" * (len(seq1) - len(seq2))
    
    # --- Step 3: Initialize difference counter ---
    dif_count = 0
    
    # --- Step 4: Compare letters using zip ---
    for a, b in zip(seq1, seq2):
        if a != b:
            dif_count += 1
    
    # --- Step 5: Return the final Hamming score ---
    return dif_count


seq1 = 'joaaashua'
seq2 = 'joseph'

hamming_distance(seq1, seq2)