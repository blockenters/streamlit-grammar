
# 스트림릿의 내장 차트 함수와, 웹용 차트인 plotly 

import streamlit as st
import plotly.express as px
import pandas as pd

def main():
    df = pd.read_csv('data/lang_data.csv')

    st.text('언어별 인기도')
    selected_columns = st.multiselect('언어를 선택하세요.', df.columns)
    print(selected_columns)

    if len(selected_columns) != 0:
        df_selected = df[selected_columns]

        # st 내장 라인 차트 
        st.line_chart(df_selected)

        # st 내장 area 차트 
        st.area_chart(df_selected)

    df2 = pd.read_csv('data/location.csv', index_col=0)
    st.dataframe(df2)

    # st 내장 지도 그리는 함수 
    st.map(df2)

    df3 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df3)

    # plotly express 의 pie 차트 
    fig1 = px.pie(data_frame=df3, names='lang', values='Sum')
    st.plotly_chart(fig1)

    # plotly express 의 bar 차트
    df3.sort_values('Sum', ascending=False, inplace=True)
    fig2 = px.bar(data_frame= df3, x='lang', y='Sum')
    st.plotly_chart(fig2)

    


if __name__ == '__main__':
    main()




