{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "294d37e5-b946-4655-a7a6-568800895aec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Judul Utama\n",
    "st.title(\"📊 Web Mining Berita detik.com\")\n",
    "st.write(\"Visualisasi Hasil Crawling, Preprocessing, dan PCA (Sport & Finance)\")\n",
    "\n",
    "# Load Data CSV\n",
    "try:\n",
    "  df_berita = pd.read_csv(\"berita_detik_sport_finance.csv\")\n",
    "  df_pca = pd.read_csv(\"hasil_pca_berita.csv\")\n",
    "\n",
    "  # Tampilan Tab\n",
    "  tab1, tab2 = st.tabs([\"📰 Data Berita\", \"📉 Visualisasi PCA\"])\n",
    "\n",
    "  with tab1:\n",
    "    st.subheader(\"Data Hasil Crawling Berita\")\n",
    "    st.dataframe(df_berita)\n",
    "\n",
    "  with tab2:\n",
    "    st.subheader(\"Scatter Plot Reduksi Dimensi PCA\")\n",
    "    st.dataframe(df_pca)\n",
    "    st.scatter_chart(\n",
    "        data=df_pca, x=\"PCA_Component_1\", y=\"PCA_Component_2\", color=\"kategori\"\n",
    "    )\n",
    "\n",
    "except Exception as e:\n",
    "  st.error(f\"Gagal memuat data: {e}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "envWebmining (Py 3.9)",
   "language": "python",
   "name": "envwebmining39"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
