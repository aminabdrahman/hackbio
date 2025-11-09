#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-09T05:19:08.058Z
"""

import pandas as pd
import seaborn as snscorr(method='pearson', numeric_only = True).head()
import matplotlib.pyplot as plt

df = pd.read_csv('./hbr_uhr_top_deg_normalized_counts.csv', index_col=0)
df.head()

sns.clustermap(
    df,
    cmap="Blues",       # color palette
    figsize=(10, 8),
    cbar_kws={"label": "Expression level"},
    dendrogram_ratio=(.2, .2),
    linewidths = 0.5,
    linecolor = 'black'
)