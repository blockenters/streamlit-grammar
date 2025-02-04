# 파일업로드 + 사이드바

from datetime import datetime
import pandas as pd
import streamlit as st

def save_uploaded_file(directory, file):
    # 1. 디렉토리가 없으면, 만들어준다.
    import os 
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 이 디렉토리에 파일을 저장한다.
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    # 3. 저장완료 되었으니, 유저한테 알려준다.
    st.success(f'저장완료: {directory}에 {file.name} 저장되었습니다.')


def main() :
    st.title('파일 업로드 예제')

    st.sidebar.title('사이드바')
    menu = ['이미지 파일 업로드', 'CSV 파일 업로드', 'pdf 파일 업로드' ]
    choice = st.sidebar.selectbox('메뉴를 선택하세요', menu )
    print(choice)

    if choice == menu[0]:
        st.subheader('이미지 파일 업로드')
        # 이미지 파일 업로드
        file = st.file_uploader('이미지 파일 업로드', type=['jpg','png','jpeg', 'webp'])

        if file is not None:
            # 1. 파일 이름을 유니크하게 만든다
            new_filename = datetime.now().isoformat().replace(':','_') + '.jpg'
            file.name = new_filename
            # 2. 파일 저장한다.
            save_uploaded_file('images', file)
            # 3. 화면에 이미지를 보여준다. 
            st.image(file, use_container_width=True)

    elif choice == menu[1]:
        st.subheader('CSV 파일 업로드')

        file = st.file_uploader('CSV 파일 업로드', type=['csv'])

        if file is not None:
            # 1. 파일을 저장하고,
            save_uploaded_file('csv', file)
            # 2. 데이터 프레임을 화면에 보여준다. 
            df = pd.read_csv(file)
            st.dataframe(df)

    elif choice == menu[2]:
        st.subheader('pdf 파일 업로드')

        file = st.file_uploader('pdf 파일 업로드', type=['pdf'])

        if file is not None:
            # 1. 파일을 저장하고, 
            save_uploaded_file('pdf', file)

            # 2. pdf 파일을 화면에 보여준다.
            st.write(file)

if __name__ == '__main__' :
    main()




