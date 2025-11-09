#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: b_volcano.ipynb
Conversion Date: 2025-11-09T05:19:27.916Z
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data-3.csv', index_col = 0)
df.head()

plt.figure(figsize=(8, 6))

sns.scatterplot(df,
               y = 'texture_mean',
               x = 'radius_mean',
               hue = 'diagnosis')