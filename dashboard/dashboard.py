import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load Data
data = pd.read_csv('merge_data.csv')
data['dteday'] = pd.to_datetime(data['dteday'])
data.set_index('dteday', inplace=True)

#Header dab Subheader
st.markdown("<h1 style='text-align: center; display: flex; justify-content: center;'>🚲 Bike Rental Analysis 🚲</h1>", unsafe_allow_html=True)
# st.text('by:Sabrina Sekar Ranti')
st.text('')
st.text('')
st.text('')

#Pertanyaan 1
#Sub Header dan Text
st.subheader('Trend Penyewaan Sepeda per Tahun 2011-2012')
st.write('Berikut kami tampilkan jumlah penyewaan sepeda Tahun 2011 dan Tahun 2012')

# Menghitung dan menampilkan total penyewaan untuk tahun 2011 dan 2012
total_rentals_2011 = data[data['yr'] == 0]['cnt'].sum()
total_rentals_2012 = data[data['yr'] == 1]['cnt'].sum()

# Membuat visualisasi menggunakan bar plot
year = ['2011', '2012']
total_rentals = [total_rentals_2011, total_rentals_2012]
plt.figure(figsize=(4, 4))
plt.bar(year, total_rentals, color=['pink', 'orange'])

for i in range(len(year)):
    plt.text(year[i], total_rentals[i] + 1000, str(total_rentals[i]), ha='center', va='bottom')

# Konfigurasi plot
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penyewaan')
plt.title('Perbandingan Banyak Penyewaan Sepeda per Tahun (2011-2012)')
st.pyplot(plt)

#Penjelasan
st.write('Terdapat kenaikan dalam penyewaan sepeda Tahun 2011 dan Tahun 2012')
st.text('')

#Pertanyaan 2
st.subheader('Pengaruh Cuaca dalam Penyewaan Sepeda')

# Menghitung rata-rata jumlah penyewaan sepeda untuk setiap nilai weathersit
plt.figure(figsize=(3, 3))
average_rentals_by_weather = data.groupby('weathersit')['cnt'].mean()

# Visualisasi rata-rata jumlah penyewaan berdasarkan cuaca
st.write('Berikut kami tampilkan rata-rata jumlah penyewaan sepeda di tiap cuaca:')
ax = average_rentals_by_weather.plot(kind='bar', color='skyblue', figsize=(8, 6))

for i in ax.patches:
    plt.text(i.get_x() + i.get_width() / 2, i.get_height() + 50, str(round(i.get_height(), 2)), ha='center', va='bottom')

plt.title('Rata-rata Jumlah Penyewaan Sepeda berdasarkan Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.xticks(range(4), ['1', '2', '3', '4'], rotation=0)
st.pyplot(plt)
st.text('')

# Menghitung korelasi antara cuaca dan jumlah penyewaan sepeda
correlation = data['weathersit'].corr(data['cnt'])

# Visualisasi korelasi antara cuaca dan jumlah penyewaan sepeda
st.write('Berikut kami tampilkan heatmap korelasi antara cuaca dengan penyewaan sepeda:')
plt.figure(figsize=(3, 3))
sns.heatmap(data[['weathersit', 'cnt']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korelasi antara Cuaca dan Jumlah Penyewaan Sepeda')
st.pyplot(plt)
st.markdown(
    "<h3 style='font-size: 12px;'>Keterangan:</h3>"
    "<p style='font-size: 10px;'>1 = Cerah, Sedikit awan, Sebagian berawan, Sebagian berawan</p>"
    "<p style='font-size: 10px;'>2 = Kabut + Mendung, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut</p>"
    "<p style='font-size: 10px;'>3 = Salju Ringan, Hujan Ringan + Badai Petir + Awan berserakan, Hujan Ringan + Awan berserakan</p>"
    "<p style='font-size: 10px;'>4 = Hujan Lebat + Hujan Es + Badai Petir + Kabut, Salju + Kabut</p>",
    unsafe_allow_html=True
)
st.text('')

#Penjelasan
st.write('Dari hasil korelasi, cuaca tidak memengaruhi jumlah penyewaan secara signifikan. Kemungkinan besar terdapat pengaruh dari variabel-variabel yang lain.')
st.text('')

#Pertanyaan 3
st.subheader('Trend Penyewaan Sepeda Tiap Musim')
st.write('Berikut kami tampilkan tren penyewaan sepeda pada tiap musim:')
st.text('')

spring_data = data[data['season'] == 1]
summer_data = data[data['season'] == 2]
fall_data = data[data['season'] == 3]
winter_data = data[data['season'] == 4]

# Menganalisis tren untuk setiap musim
trends = {
    'Spring': spring_data.resample('M').sum()['cnt'],
    'Summer': summer_data.resample('M').sum()['cnt'],
    'Fall': fall_data.resample('M').sum()['cnt'],
    'Winter': winter_data.resample('M').sum()['cnt']
}

# Visualisasi
for season, trend in trends.items():
    st.write(f"**Tren musim {season}:**")
    st.line_chart(trend, use_container_width=True)


st.text('')
st.caption('Sabrina Sekar Ranti - 2024')