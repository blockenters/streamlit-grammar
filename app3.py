# UI 관련된 함수들 소개. 

import streamlit as st 
import pandas as pd

def main() :
    df = pd.read_csv('data/iris.csv')

    # 유저가 버튼을 누르면, 데이터 프레임을 웹화면에 보여준다. 
    if st.button('데이터 보기') : 
        st.dataframe( df )

    # '대문자' 버튼을 만들고,
    # 유저가 이 버튼을 누르면, species 컬럼의 데이터를 대문자로 바꿔서
    # 아래에 보여준다. 
    if st.button('대문자') :
        st.dataframe( df['species'].str.upper() )

    # 라이오버튼 : 여러개의 선택지 중에서 하나를 선택할 수 있는 버튼
    st.radio('가장 좋아하는 색상은?', ['빨강', '노랑', '파랑'])

    # 라디오버튼을 만들되
    # 오름차순 정렬, 내림차순 정렬  이 2개를 선택할 수 있게 만들어보자.
    # petal_length 컬럼을 정렬. 
    my_choice = st.radio('petal_length 정렬 방식을 선택하세요' , ['오름차순', '내림차순'])
    if my_choice == '오름차순' :
        st.dataframe( df.sort_values('petal_length') )
    else :
        st.dataframe( df.sort_values('petal_length', ascending=False) )


if __name__ == '__main__' :
    main()
