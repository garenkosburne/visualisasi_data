# -*- coding: utf-8 -*-
"""Proyek_Akhir_Analisis_Data_dengan_Pyhton.ipynb

# Proyek Analisis Data: Bike Sharing Analysis
- Nama: Ringga Setiadi
- Email: garenkosburne@gmail.com
- Id Dicoding:ringga__LobT

## Menentukan Pertanyaan Bisnis

- pertanyaan 1 : Bagaimana variasi ketersediaan sepeda berdasarkan kondisi cuaca (weathersit) pada hari tertentu? Apakah cuaca yang baik memengaruhi peningkatan penyewaan?
- pertanyaan 2 : Bagaimana hubungan antara suhu (temp) dan jumlah penyewaan sepeda harian? Apakah terdapat tren atau pola tertentu?
- pertanyaan 3 : Apakah ada perbedaan antara distribusi penyewaan sepeda antara weekend dan weekdays?
- pertanyaan 4 : Bagaimana kontribusi pengguna casual dan registered terhadap total penyewaan sepeda?

## Menyiapkan semua library yang dibuthkan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from os import path


"""## Data Wrangling

### Gathering Data
"""

#uploading dataset yang digunakan
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

"""### Assessing Data"""

#Melihat baris awal (5 baris pertama) untuk setiap dataset
print(day_df.head())
print(hour_df.head())

"""### Cleaning Data"""

#pengecekan missing value pada dataset

print(day_df.isnull().sum())
print(hour_df.isnull().sum())

#Menghapus 'instant' karena tidak memberikan informasi untuk pertanyaan

day_df.drop('instant', axis=1, inplace=True)
hour_df.drop('instant', axis=1, inplace=True)

"""## Exploratory Data Analysis (EDA)"""

print(day_df.describe())
print(hour_df.describe())

# Merubah kolom 'dteday' menjadi tipe data datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Menentukan tanggal terakhir dalam dataset
last_date = day_df['dteday'].max()

"""## Visualization & Explanatory Analysis

### Pertanyaan 1:Bagaimana variasi ketersediaan sepeda berdasarkan kondisi cuaca (weathersit) pada hari tertentu? Apakah cuaca yang baik memengaruhi peningkatan penyewaan?
"""

# Ketersediaan sepeda berdasarkan kondisi cuaca (weathersit)
plt.figure(figsize=(10, 5))

sns.barplot(
    y="cnt",
    x="weathersit",
    data=day_df,
    palette="viridis"
)
plt.title("Variasi Ketersediaan Sepeda Berdasarkan Kondisi Cuaca", loc="center", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("Kondisi Cuaca")
plt.tick_params(axis='x', labelsize=12)
plt.show()

"""
### Pertanyaan 2:Bagaimana hubungan antara suhu (temp) dan jumlah penyewaan sepeda harian? Apakah terdapat tren atau pola tertentu?"""

# Hubungan antara suhu dan jumlah penyewaan sepeda harian

plt.figure(figsize=(10, 5))

sns.scatterplot(
    y="cnt",
    x="temp",
    data=day_df,
    palette="viridis"
)
plt.title("Hubungan Antara Suhu dan Jumlah Penyewaan Sepeda Harian", loc="center", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("KSuhu")
plt.tick_params(axis='x', labelsize=12)
plt.show()

"""### Pertanyaan 3: Apakah ada perbedaan antara distribusi penyewaan sepeda antara weekend dan weekdays?"""

#Distribusi penyewaan sepeda pada weekend dan weekdays

plt.figure(figsize=(10, 5))

sns.barplot(
    y="cnt",
    x="holiday",
    data=day_df,
    palette="viridis"
)
plt.title("Distribusi penyewaan sepeda pada weekend daya weekdays", loc="center", fontsize=15)
plt.ylabel("Jumlah Penyewaan")
plt.xlabel("Weekend(1: Ya, 0: Tidak")
plt.tick_params(axis='x', labelsize=12)
plt.show()

"""### Pertanyaan 4: Bagaimana kontribusi pengguna casual dan registered terhadap total penyewaan sepeda?"""

# Plotting kontribusi pengguna casual dan registered per tahun

plt.figure(figsize=(10, 5))
sns.barplot(data=day_df, x='weekday', y='cnt', hue='yr', palette='viridis')
plt.title('Kontribusi Pengguna Casual dan Registered Terhadap Total Penyewaan per Tahun')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Jumlah Penyewaan')
plt.show()

"""## Conclusion

**Conclution pertanyaan 1**: Berdasarkan barplot kondisi cuaca terhadap jumlah penyewaan dapat saya simpulkan menjadi:
- weathersit 1 : pada kondisi ini cuaca baik yang berpengaruh pada tingginya penyewaan sepeda.
-weathersit 2 dan 3 : pada kondisi ini cuaca lebih buruk sehingga terjadi penurunan penyewaan sepeda

**Conclution pertanyaan 2**: berdasarkan visualisasi berdasarkan scatterplot dapat disimpulkan bahwa semakin tinggi cuaca maka semakin tinggi pula jumlah penyewaan sepeda. Hal ini sejalan dengan conlusin pertanyaan 1.

**Conclution pertanyaan 3**: berdasrakan barplot menunujukan hasil bahwa tingkat penyewaan pada *weekdays* lebih tinggi dari pada *weekend*. Hal ini terjadi karena pada saat cuaca yang baik kecenderungan dari orang-orang untuk keluar rumah untuk menikmati keindahan alam.

**Conclution pertanyaan 4**: berdasarkan barplot dapat ditarik kesimpulan bahwa:
- pada tahun 2011 dan 2012 terlihat pengguna casual dan registered terhadap penyewaan sepeda cukup seragam.
- pengguna registered memberikan kontribusi lebih tinggi dibandingkan casual dalam penyewaan sepeda.
- karena tingginya pengguna registered dalam penyewaan sepeda, maka bisnis bisa meningkatkan jumlah pengguna registerednya untuk meningkatkan volume penyewaan ini.
"""
