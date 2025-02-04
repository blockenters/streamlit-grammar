# 스트림릿 라이브러리를 사용하기 위한 임포트 
import streamlit as st 

# 스트림릿 앱을 실행하기 위한 기본 틀! 

def main() :
    # st 의 함수들은, 웹 화면에 표시하는 함수들.
    st.title("Hello Streamlit")
    st.subheader('작은 제목')
    st.text('일반 텍스트')
    st.success('무엇인가 잘 되었음을 글자로 나타낼때')
    st.info('정보를 나타낼때')
    st.warning('경고를 나타낼때')
    st.error('에러를 나타낼때')

    name = '홍길동'

    print( f'제 이름은 {name}입니다.' )

    st.text( f'제 이름은 {name}입니다.' )

    st.write('텍스트를 표시할수 있습니다.')

if __name__ == '__main__' :
    main()
