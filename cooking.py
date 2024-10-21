

# OpenAI API 키 설정 (본인의 API 키로 교체하세요)
openai.api_key = "YOUR_API_KEY"

# 앱 제목
st.title("비즈니스 의사결정 지원 앱")

# 앱 개발 동기
st.subheader("앱 개발 동기")
st.write("경영학과를 희망하며, 데이터 분석 및 의사결정의 중요성을 바탕으로 사용자들이 더 나은 비즈니스 결정을 내릴 수 있도록 돕는 앱을 개발합니다.")

# API 연동 기능
st.subheader("API 연동")
api_url = st.text_input("데이터를 수집할 API URL을 입력하세요:")
if st.button("API 데이터 가져오기"):
    if not api_url.startswith(("http://", "https://")):
        st.warning("유효한 API URL을 입력하세요.")
    else:
        with st.spinner("데이터를 가져오는 중..."):
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    st.success("데이터를 성공적으로 가져왔습니다.")

                    # JSON 데이터 처리 예
                    if isinstance(data, list):
                        # 리스트 형태의 데이터 처리
                        df = pd.DataFrame(data)
                        st.dataframe(df)  # DataFrame으로 변환하여 표시
                    elif isinstance(data, dict):
                        # 딕셔너리 형태의 데이터를 처리한 후 표시
                        st.write(pd.DataFrame([data]))
                    else:
                        st.warning("지원하지 않는 데이터 형식입니다.")
                else:
                    st.error(f"API 호출 실패: {response.status_code}")
            except Exception as e:
                st.error(f"오류 발생: {e}")

# 실시간 피드백 기능
st.subheader("실시간 피드백")
user_decision = st.text_area("현재 결정이나 전략에 대해 입력하세요:")
if st.button("AI 피드백 받기"):
    if user_decision:
        # OpenAI API에 요청하기
        with st.spinner("AI 피드백을 가져오는 중..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_decision}]
                )
                feedback = response["choices"][0]["message"]["content"]
                st.success(f"AI 피드백: {feedback}")
            e

# 고객 세분화 기능
st.subheader("고객 세분화")
st.write("고객 데이터를 기반으로 세분화를 진행합니다.")
customer_data = st.text_area("고객 데이터를 입력하세요 (콤마로 구분된 값):")
if st.button("세분화하기"):
    if customer_data:
        customers = customer_data.split(",")
        segmentation = pd.DataFrame(customers, columns=["고객"])

        # 예시 세분화 (임의로 생성된 데이터)
        segmentation["세그먼트"] = [
            "고급" if "VIP" in customer else "일반" for customer in customers
        ]

        st.succ
