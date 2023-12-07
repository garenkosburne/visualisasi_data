# Proyek Analisis Data Penyewaan Sepeda

## Informasi Umum

**Nama**: Ringga Setiadi  
**Email**: garenkosburne@gmail.com
**Id Dicoding**: ringga__LobT

## Deskripsi Projek

Projek ini berfokus pada analisis data penyewaan sepeda untuk mendapatkan wawasan mengenai pola dan tren penyewaan sepeda berdasarkan cuaca, weekend dan weekdays serta pengguna casual dan registered. Dua dataset utama yang digunakan adalah `day.csv` dan `hour.csv`, yang berisi data harian, kondisi dan waktu penyewaan sepeda.

## Pertanyaan Bisnis

1. Apakah peran cuaca dapat memengaruhi peningkatan penyewaan?
2. Bagaimana kondisi yang tampak ketika sepeda digunakan pada workingday, holiday, dan weekday?
3. Bagaimana tren penggunaan sepeda dalam setahun? ditahun manakah tren yang lebih tinggi?
4. Bagaimana variabel seperti temp dan atemp serta humidity dapat mempengaruhi jumlah total penyewa sepeda (baik Casual ataupun Registered)?
5. Apakah ada pengaruh musim terhadap penyewa sepeda 

## Analisis Data

Analisis data dilakukan dengan menggunakan Python dan berbagai library seperti pandas, matplotlib, dan seaborn. Proses analisis meliputi eksplorasi data, visualisasi, dan interpretasi hasil untuk menjawab pertanyaan bisnis.


## Dashboard

Dashboard interaktif dibuat dengan menggunakan Streamlit untuk memvisualisasikan hasil analisis data secara interaktif. Dashboard dapat diakses [di sini](https://visualisasidata-4tarnsnq32aqja2ppyqlah.streamlit.app/)

## Setup Environment
Anda perlu membuat environment khusus menggunakan Conda dan menginstall dependensi yang diperlukan. Ikuti langkah-langkah berikut:
```sh
conda create --name main-ds python=3.11
conda activate main-ds
pip install streamlit pandas numpy matplotlib seaborn
```
## Run steamlit app
```
streamlit run dashboard_tugas_akhir.py
```
