#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: c_scatterplot.ipynb
Conversion Date: 2025-11-09T05:19:43.427Z
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data-3.csv', index_col = 0)
df.head()

matrix = df[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean']].corr(method='pearson', numeric_only = True)
matrix.head()

sns.heatmap(matrix,
           vmin = 0,
           vmax = 1,
           cmap = 'Blues',
           annot = True,
           fmt = '0.1f')