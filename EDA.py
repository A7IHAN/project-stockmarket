###########################################################
# IMPORT'LAR VE BAZI AYARLAR #
###########################################################

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from veri_seti import all_dfs

warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)


###########################################################
# İLK HİSSE İÇİN KEŞİFÇİ VERİ ANALİZİ #
###########################################################

first_df = all_dfs[0]


first_df.describe().T
first_df.info()

# DEĞİŞKENLERİN KORELASYONLARI #

df_corr = first_df.corr()
mask = np.triu(np.ones_like(df_corr, dtype=bool))

plt.figure(figsize=(50, 50))
sns.heatmap(df_corr, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Değişkenler Arasındaki Korelasyon Matrisi")
plt.show()

# YÜKSEK KORELASYONU OLAN DEİŞKENLERİN GÖRSELİ #

threshold = 0.75
high_corr = df_corr[(df_corr > threshold) | (df_corr < -threshold)]

plt.figure(figsize=(50, 50))
sns.heatmap(high_corr, annot=True, mask=mask, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Değişkenler Arasındaki Yüksek Korelasyonlar\n(Eşik Değeri = ±{})".format(threshold))
plt.show()