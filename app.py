{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7f8a0d4d-8c4c-48ea-bc81-6793be0dda8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-09-17 11:26:30.261 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.262 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.264 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.264 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.296 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.298 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.301 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.302 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.302 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.306 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.482 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.490 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.494 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:30.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:37.507 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:37.507 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-09-17 11:26:37.507 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Judul Aplikasi\n",
    "st.title(\"📊 Web Mining Berita detik.com\")\n",
    "st.write(\"Aplikasi visualisasi data berita Sport dan Finance.\")\n",
    "\n",
    "# Read Data\n",
    "df_berita = pd.read_csv(\"berita_detik_sport_finance.csv\")\n",
    "df_pca = pd.read_csv(\"hasil_pca_berita.csv\")\n",
    "\n",
    "# Tab Tampilan\n",
    "tab1, tab2 = st.tabs([\"📰 Data Berita\", \"📉 Hasil PCA\"])\n",
    "\n",
    "with tab1:\n",
    "  st.subheader(\"Data Hasil Crawling\")\n",
    "  st.dataframe(df_berita)\n",
    "\n",
    "with tab2:\n",
    "  st.subheader(\"Visualisasi Reduksi Dimensi PCA\")\n",
    "  st.dataframe(df_pca)\n",
    "  st.scatter_chart(\n",
    "      data=df_pca, x=\"PCA_Component_1\", y=\"PCA_Component_2\", color=\"kategori\"\n",
    "  )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "294d37e5-b946-4655-a7a6-568800895aec",
   "metadata": {},
   "outputs": [],
   "source": []
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
