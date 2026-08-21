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

# 2. 데이터 읽어보기
#df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv',encoding='cp949')
df = pd.read_csv('등산경로.csv',encoding='UTF-8') #cp949
#코스의 위치에 해당하는 사진 이미지 이름 : "images/A입구.jpg"
df['이미지'] = 'images/' + df['코스'] + df['위치명'] + '.jpg'

df_latlon = df[['위도','경도']]
df_latlon = df_latlon.rename(columns={'위도':'lat','경도':'lon'})
#st.map(df_latlon)

# 3. 지도 생성 및 마커 표시(지도 시각화 단계)
m = folium.Map(
    location = [37.40583317, 126.7214872],
    zoom_start = 16
)

for i in range(len(df)):
    folium.Marker(
      location = [df.iloc[i]['위도'], df.iloc[i]['경도']],
      popup = f'<div style="width:200px"> <strong>{df.iloc[i]['위치명']}</strong></div>',
      tooltip = "클릭해보세요",
      icon = folium.Icon(color='cadetblue', icon='info-sign')
    ).add_to(m)

# 4. 화면 출력
col1, col2 = st.columns([3,1])

with col1:
    st_folium(m, width=700, height=500)

with col2:
    st.subheader("정보") #코스별 정보 넣기
    st.info("길이 미끄럽습니다. 주의하세요") #코스별 정보 넣기
    st.metric(label="소요시간", value="10분") #소요시간, 정보 코스별로 넣기
    st.write("주의사항 : 👟등산화를 착용하세요.")
