# app.py : 홈 화면
import streamlit as st
from utils import load_a, load_b, nat_rate, OLD_A

st.set_page_config(page_title="고혈압 현황 분석", page_icon="🩺", layout="wide")
a, b = load_a(), load_b()

st.title("🩺 대한민국 고혈압 현황과 혈압관리의 중요성")
st.write("국민건강보험공단 공공데이터로 고혈압 진료 현황과 의료이용 현황을 살펴보고, "
         "어느 연령대와 지역에서 혈압관리가 필요한지 알아보는 데이터 분석 웹앱입니다.")

tot = a.groupby("year")["patients"].sum()
old = a[a.age.isin(OLD_A)].groupby("year")["patients"].sum() / tot * 100
c1, c2, c3, c4 = st.columns(4)
c1.metric("전국 고혈압·당뇨병 의료이용률(2024)", f"{nat_rate(b):.1f}%")
c2.metric("고혈압 진료인원(2022)", f"{tot[2022] / 1e4:,.0f}만 명")
c3.metric("2017년 대비 증가율", f"{(tot[2022] / tot[2017] - 1) * 100:.1f}%")
c4.metric("65세 이상 비중(2022)", f"{old[2022]:.1f}%")

st.subheader("사용한 데이터 (출처: 국민건강보험공단)")
st.markdown("""
- **데이터 A**: 본태성(원발성) 고혈압 진료인원 (2017~2022년, 성별·5세 단위 연령)
- **데이터 B**: 고혈압·당뇨병 의료이용률 (2024년, 시도·시군구·성별·10세 단위 연령)
""")

st.subheader("페이지 안내")
st.markdown("""
1. **trend** : 고혈압 진료인원의 연도별 추이
2. **age** : 연령별 진료인원과 연도 비교
3. **national** : 전국 의료이용률 (성별·연령대)
4. **regions** : 시도·시군구별 비교
5. **standardization** : 연령 구조를 보정한 지역 비교
6. **conclusion** : 종합 결론
""")

st.info("**해석할 때 주의하세요**\n\n"
        "① 데이터 A는 '사람 수'이며 인구 대비 비율이 아닙니다.\n\n"
        "② 데이터 B는 고혈압과 당뇨병을 합친 의료이용률입니다.\n\n"
        "③ 두 데이터는 기간과 연령 구간이 달라 합치지 않고 따로 분석했습니다.")
st.sidebar.success("위쪽 메뉴에서 페이지를 선택하세요.")
