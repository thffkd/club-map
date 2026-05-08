# main.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산", layout="wide")

st.title("⛰️2026 학교 등산 행사 안내 지도⛰️")
st.markdown("컴퓨터 동아리가 집적 만든 코스 가이드입니다.")
st.markdown("코스를 선택하고 행사에 참여해 보세요.")
st.markdown("# 큰 제목")
st.markdown("## 작은 제목")
st.markdown("**굵은 글씨**")
st.markdown("*이탤릭체*")

st.header("헤더입니다")
st.subheader("서브헤더입니다")
st.caption("캡션입니다")
st.code("a=3")

st.text("집 가고 싶다")
