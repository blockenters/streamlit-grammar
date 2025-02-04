
import streamlit as st 
import pandas as pd

def main() :
    # 판다스 데이터프레임 읽어와서
    # 웹 화면에 표시 
    df = pd.read_csv('data/iris.csv')

    st.title('Iris 데이터 분석')

    st.dataframe( df )

    # species 컬럼의 유니크한 값들을 출력 
    st.text('species 컬럼의 유니크한 값들')

    st.dataframe( df['species'].unique() )

    # 전체 데이터의 갯수를 화면에 표시 
    print( df.shape )

    st.info(f'전체 데이터의 개수는 {df.shape[0]}개 입니다.')

if __name__ == '__main__' :
    main()
