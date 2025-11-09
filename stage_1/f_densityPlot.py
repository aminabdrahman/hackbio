#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: e_scatterplot.ipynb
Conversion Date: 2025-11-09T05:20:08.993Z
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data-3.csv', index_col = 0)
df.head()

sns.kdeplot(df,
           x = 'area_mean',
           hue = 'diagnosis',
           fill = True)