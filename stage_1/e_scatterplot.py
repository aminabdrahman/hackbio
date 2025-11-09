#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: dna_to_aa.ipynb
Conversion Date: 2025-11-09T05:20:02.116Z
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data-3.csv', index_col = 0)
df.head()

sns.scatterplot(df,
               x = 'compactness_mean',
               y = 'smoothness_mean',
               hue = 'diagnosis')

plt.grid()