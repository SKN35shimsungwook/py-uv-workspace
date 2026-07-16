

import streamlit as st
import pandas as pd
import os


header = ['학번','이름','전공']
students = [
    ['202601','홍길동','컴퓨터공학'],
    ['202602','이순신','데이터사이언스'],
    ['202603','유관순','인공지능학']
]


st.title("학사정보 검색")
st.write("아래 입력값을 바탕으로 학사 정보를 출력합니다.")


name = st.text_input("이름을 입력하세요")


학번 = None
전공 = None


for s in students:
    if s[1] == name:
        학번 = s[0]
        전공 = s[2]
        break


if name:
    if name == '':
        st.write(f"이름을 입력해 주세요.")
    elif name == None:
        st.write(f"해당 정보를 찾을 수 없습니다.")
    else:
        st.write(f"{name}의 학번은 {학번}, 전공은 {전공}입니다.")
        st.subheader("📷 학생증 사진 업로드")
        uploaded_file = st.file_uploader(
            "학생증 사진을 업로드하세요",
            type=["jpg", "jpeg", "png"],
            key=학번  # 학생마다 업로더를 구분하기 위한 key
        )


        if uploaded_file is not None:
            st.image(uploaded_file, caption=f"{name}의 학생증", width=300)
            st.success("사진이 업로드되었습니다.")



