import streamlit as st
import time

st.title("3분 타이머")

# 세션 상태로 타이머 시작 시간 관리
if "start_time" not in st.session_state:
    st.session_state.start_time = None

if st.button("타이머 시작"):
    st.session_state.start_time = time.time()

if st.session_state.start_time is not None:
    elapsed = time.time() - st.session_state.start_time
    remaining = 180 - elapsed  # 3분 = 180초

    if remaining > 0:
        mins, secs = divmod(int(remaining), 60)
        st.markdown(f"<h1 style='font-size:72px;'>{mins:02d}:{secs:02d}</h1>", unsafe_allow_html=True)
        st.experimental_rerun()  # 화면 갱신
        time.sleep(1)
    else:
        st.markdown("<h1 style='font-size:100px; color: red;'>시간 종료</h1>", unsafe_allow_html=True)
