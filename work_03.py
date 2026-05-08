# 심박출(ejection_fraction)로 범위를 한정하여 그래프 구현
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

# slider 범위 설정
min_ef = int(df['ejection_fraction'].min())
max_ef = int(df['ejection_fraction'].max())

st.write('심박출 범위에 따른 time 히스토그램')

selected_range = st.slider(
    '심박출(ejection_fraction) 범위 선택',
    min_value=min_ef,
    max_value=max_ef,
    value=(min_ef, max_ef)
)

# 선택 범위
low, high = selected_range

# 데이터 필터링
filtered_df = df[
    (df['ejection_fraction'] >= low) &
    (df['ejection_fraction'] <= high)
]

# histogram
g= sns.histplot( 
    data=filtered_df,
    x='time',
    bins=20,
    hue='DEATH_EVENT'
)

st.write(g.figure)
