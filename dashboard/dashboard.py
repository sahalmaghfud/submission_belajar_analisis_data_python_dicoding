import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def load_data():
    all_data_df = pd.read_csv('dashboard/data.csv')
    return all_data_df  

def plot_pm25(data, selected_year):
    filtered_data = data[data['year'] == selected_year]
    result = filtered_data.groupby(by="station")['PM2.5'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#D3D3D3"] * len(result)  # Warna abu-abu untuk semua bar
    
    sns.barplot(
        x='station', 
        y='PM2.5', 
        data=result.sort_values(by="PM2.5", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title(f'Rata-rata PM2.5 per Stasiun di Tahun {selected_year}', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def plot_rain(data, selected_year):
    filtered_data = data[data['year'] == selected_year]
    rain_data = filtered_data.groupby(["month", "station"])['RAIN'].sum().unstack().reset_index()
    rain_data = rain_data.melt(id_vars='month', var_name='station', value_name='total_rain')

    fig, ax = plt.subplots(figsize=(20, 10))
    colors = sns.color_palette("Set2", n_colors=len(rain_data['station'].unique())) 
    
    sns.barplot(
        x='month', 
        y='total_rain', 
        hue='station', 
        data=rain_data,
        palette=colors,
        ax=ax
    )
    ax.set_title(f'Total Curah Hujan per Stasiun di Tahun {selected_year}', loc='center', fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    plt.xticks(rotation=0)
    ax.legend(title='Stasiun', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot(fig)

st.title("Visualisasi Data Kualitas Udara dan Curah Hujan")

all_data_df = load_data()

years = all_data_df['year'].unique()
selected_year = st.selectbox("Pilih Tahun", sorted(years))

st.subheader("Rata-rata PM2.5 per Stasiun")
plot_pm25(all_data_df, selected_year)

st.subheader("Total Curah Hujan per Stasiun per Bulan")
plot_rain(all_data_df, selected_year)
