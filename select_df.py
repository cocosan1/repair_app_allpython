import streamlit as st
import pandas as pd
import openpyxl

def select_dataframe(index):
    df = pd.read_excel('chair_all.xlsx', sheet_name='Sheet1', index_col=0)
    df_selected = df.loc[index]
    st.write(df_selected)
