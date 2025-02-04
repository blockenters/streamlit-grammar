
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb

import platform

if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

def main():
    st.title('차트 그리기 1')
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    st.text('스케터 플롯')
    
    fig1 = plt.figure()
    plt.scatter(data= df, x='petal_length', y='petal_width')
    plt.title('꽃잎 길이 대 꽃잎 너비')
    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    st.pyplot(fig1)

    fig2 = plt.figure()
    sb.regplot(data=df, x='petal_length', y='petal_width')
    st.pyplot(fig2)


    # 히스토그램. 
    st.text('꽃잎 길이에 대한 히스토그램')
    fig3 = plt.figure()
    plt.hist(data= df, x='petal_length', rwidth=0.8)
    st.pyplot(fig3)    

    fig4 = plt.figure()
    plt.hist(data= df, x='petal_length', rwidth=0.8, bins=20)
    st.pyplot(fig4)  

    # 위의 2개 차트를 한 화면에 그리기.
    fig5 = plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(data= df, x='petal_length', rwidth=0.8)

    plt.subplot(1, 2, 2)
    plt.hist(data= df, x='petal_length', rwidth=0.8, bins=20)

    st.pyplot(fig5)

    # 판다스의 데이터프레임도 차트로 나타낼수 있다. 
    # species 컬럼의 데이터는 각각 몇개씩 있나? 차트로 나타내자.

    fig6 = plt.figure()
    sb.countplot(data= df, x= 'species')
    st.pyplot(fig6)

    fig7 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig7)


    st.dataframe(df.corr(numeric_only=True))

    fig8 = plt.figure()
    sb.heatmap(data= df.corr(numeric_only=True), annot=True, vmin= -1, vmax=1, cmap='coolwarm')
    st.pyplot(fig8)



if __name__ == '__main__':
    main()


