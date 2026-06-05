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

# 2. 데이터 읽어보기
#df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv',encoding='cp949')
df = pd.read_csv('등산경로.csv',encoding='cp949')
df_latlon = df[['위도','경도']]
df_latlon = df_latlon.rename(columns={'위도':'lat','경도':'lon'})
#st.map(df_latlon)

# 3. 지도 생성 및 마커 표시(지도 시각화 단계)
m = folium.Map(
    location=[37.40583317, 126.7214872],
    zoom_start=12
)

folium.Marker(
  location = [37.40583317, 126.7214872],
  popup = "남동고등학교",
  tooltip = "클릭해보세요",
  icon = folium.Icon(color='cadetblue', icon='info-sign')
).add_to(m)

# 4. 화면 출력
st_folium(m, width=700, height=500)
