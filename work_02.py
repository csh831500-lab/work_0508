# - 스모킹 여부를 한꺼번에 표시하지 말고 라디오로 선택하여 다른 그래프를 볼 수 있도록 구현
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


st.write('스모킹 여부에 따른 죽음과 당뇨, 흡연의 상관관계 그래프')

result = st.radio('흡연 여부 체크', ['흡연', '비흡연'])

if result =='흡연':
    filtered_df = df[df['smoking'] == 1]
else:
    filtered_df = df[df['smoking'] == 0]

g = sns.violinplot(data=filtered_df,
                x='DEATH_EVENT',
                y='platelets')

st.write(g.figure)

