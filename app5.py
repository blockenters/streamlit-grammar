
import streamlit as st

def main():
    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요.')
    print(name)
    st.text(name)

    # 2. 입력한 글자수 제한 
    address = st.text_input('주소를 입력하세요', max_chars=20)
    st.text(address)

    # 3. 여러행 입력하는 방법 
    message = st.text_area('메세지를 입력하세요', height=200)
    st.text(message)

    # 4. 비밀번호 입력 
    password = st.text_input('비밀번호를 입력하세요', type='password')
    st.text(password)

    # 5. 정수 입력 방법
    st.number_input('나이를 입력하세요', min_value=0, max_value=150)

    # 6. 실수 입력 방법
    st.number_input('키를 입력하세요', min_value=0.0, max_value=250.0, step=0.1)

    # 7. 날짜 입력 방법
    my_date = st.date_input('생일을 입력하세요')

    print(my_date)
    print( type(my_date) )

    # 요일을 출력하기
    print( my_date.weekday() )
    print( my_date.strftime('%A') )

    st.text(my_date.strftime('%A') + "입니다")

    # 8. 시간 입력 방법
    my_time = st.time_input('시간을 입력하세요')
    print(my_time)
    print( type(my_time) )

    st.text( my_time.strftime('%I:%M %p') )

    # 9. 색깔 선택하는 방법
    my_color = st.color_picker('좋아하는 색상을 선택하세요')
    print(my_color)

if __name__ == '__main__':
    main()



