#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: a_heatmap.ipynb
Conversion Date: 2025-11-09T05:19:19.028Z
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./hbr_uhr_deg_chr22_with_significance.csv', index_col = 0)
df.head()

plt.figure(figsize=(8, 6))

sns.scatterplot(df, 
                x='log2FoldChange', y='-log10PAdj',
               hue = 'significance')

plt.axvline(x=-1, color='black', linestyle='--', linewidth=1)
plt.axvline(x=1, color='black', linestyle='--', linewidth=1)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)