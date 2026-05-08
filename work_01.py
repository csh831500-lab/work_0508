import pandas as pd
import seaborn as sns
import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

path_a = os.path.join(BASE_DIR, 'data', 'heart_failure_a.json')
path_b = os.path.join(BASE_DIR, 'data', 'heart_failure_b.json')

# df 생성
df_a = pd.read_json(path_a)
df_b = pd.read_json(path_b)
df = pd.merge(df_a, df_b, on='person_id', how='inner')

st.write('박출계수와 나이의 상관관계를 위해 jointplot 그래프')

g = sns.jointplot(df, x='ejection_fraction', y='age', hue='DEATH_EVENT')

st.write(g.figure)