import pandas as pd
import streamlit as st

st.title("📊 Web Mining Berita detik.com")
st.write("Visualisasi Hasil Crawling, Preprocessing, dan PCA (Sport & Finance)")

try:
  df_berita = pd.read_csv("berita_detik_sport_finance.csv")
  df_pca = pd.read_csv("hasil_pca_berita.csv")

  tab1, tab2 = st.tabs(["📰 Data Berita", "📉 Visualisasi PCA"])

  with tab1:
    st.subheader("Data Hasil Crawling Berita")
    st.dataframe(df_berita)

  with tab2:
    st.subheader("Scatter Plot Reduksi Dimensi PCA")
    st.dataframe(df_pca)
    st.scatter_chart(
        data=df_pca, x="PCA_Component_1", y="PCA_Component_2", color="kategori"
    )

except Exception as e:
  st.error(f"Gagal memuat data: {e}")
