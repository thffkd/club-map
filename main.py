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

# 2-1. 코스별 세부 정보 사전 설정 (소요시간, 주의사항 등)
course_info = {
    "A코스": {
        "color": "blue",
        "time": "4~5분",
        "desc": "학교 출발",
        "notice": "경사가 완만하여 초보자에게 추천합니다.",
        "caution": "편안한 운동화를 착용하세요."
    },
    "B코스": {
        "color": "green",
        "time": "8~9분",
        "desc": "가온어린이공원 경유",
        "notice": "탁 트인 조망과 아름다운 자연 경관을 즐길 수 있습니다.",
        "caution": "낙엽 및 미끄럼 주의, 등산화 권장."
    },
    "C코스": {
        "color": "orange",
        "time": "10~11분",
        "desc": "서해랑길 94코스 출발",
        "notice": "접근성이 뛰어난 완주 코스입니다.",
        "caution": "수분 보충을 위해 물을 챙기세요."
    },
    "D코스": {
        "color": "red",
        "time": "13~14분",
        "desc": "세븐일레븐 코스",
        "notice": "편의점이 있어 간식 및 음료 구매가 편리합니다.",
        "caution": "쓰레기는 반드시 되가지고 내려오세요."
    },
    "E코스": {
        "color": "purple",
        "time": "12~13분",
        "desc": "논현주공1단지 코스",
        "notice": "입구를 잘 찾아가야하는 코스입니다.",
        "caution": "벌레에 물리지 않도록 벌레기피제 사용을 권장합니다."
    }
}

# 3. 사이드 바 - 코스 선택
st.sidebar.header("📝코스선택")

# Excel 데이터 내에 존재하는 실제 코스 목록 추출
unique_courses = list(df['코스'].unique()) if '코스' in df.columns else []
course_options = ["전체 코스 보기"] + unique_courses

selected_course = st.sidebar.selectbox("가고 싶은 코스를 선택하세요", course_options)

# 선택한 코스에 맞게 데이터 필터링
if selected_course == "전체 코스 보기":
    filtered_df = df.copy()
else:
    filtered_df = df[df['코스'] == selected_course].copy()

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
