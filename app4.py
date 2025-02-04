
# 이미지, 동영상, 음악파일을 화면에 보여주는 방법

import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main() :
    # 1. 저장되어있는 이미지파일을 화면에 보여주기
    img = Image.open('./data/image_03.jpg')
    st.image(img, width= 500)
    st.image(img, use_container_width=True)

    # 2. 인터넷상에 있는 이미지를 화면에 표시하는 방법
    url = 'https://kormedi.com/wp-content/uploads/2022/11/ck-cm270027748-l-700x467.jpg'
    st.image(url, width=300)  

    # 3. 동영상을 화면에 보여주기
    video_file = open('./data/video1.mp4', 'rb')
    st.video(video_file)

    # 4. 음악파일을 화면에 보여주기
    sound_file = open('./data/song.mp3', 'rb')
    st.audio(sound_file, format='audio/mp3')


if __name__ == '__main__' :
    main()


