import pandas as pd
import streamlit as st

def run_eda():
    # iris.csv 파일 읽어서
    # 여러 컬럼들을 선택할 수 있도록 화면에 보여주고
    # 유저가 선택한 컬럼들만 화면에 보여주는 기능 개발
    st.subheader('EDA 화면입니다.')
    st.text('아이리스 데이터를 분석합니다.')

    df = pd.read_csv('data/iris.csv')
    st.text('데이터 프레임을 보여줍니다.')
    st.dataframe(df)

    # 컬럼이름을 가져온다.
    print( df.columns )

    selected_columns = st.multiselect('컬럼을 선택하세요.', df.columns)
    print(selected_columns)

    if len(selected_columns) != 0 :
        st.dataframe( df[ selected_columns ] )
        # 상관계수를 보여준다.
        st.text('상관계수는~ ')
        st.dataframe( df.corr(numeric_only= True) )
    else :
        st.text('선택한 컬럼이 없습니다.')

    


