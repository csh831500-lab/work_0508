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

page = st.sidebar.radio(
    '페이지 선택',
    ['work_01', 'work_02', 'work_03']
    )

if page == 'work_01':
    st.write('박출계수와 나이의 상관관계를 위해 jointplot 그래프')
    g = sns.jointplot(df, x='ejection_fraction', y='age', hue='DEATH_EVENT')
    st.write(g.figure)

elif page == 'work_02':
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

elif page == 'work_03':
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