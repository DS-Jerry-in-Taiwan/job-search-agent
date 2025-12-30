import streamlit as st
import requests

st.set_page_config(page_title="智能職缺搜尋 Agent", page_icon="🤖")

st.title("🤖 智能職缺搜尋 Agent")
st.caption("AI 驅動的職缺搜尋、薪資分析與面試準備助手")

# 側邊欄配置
with st.sidebar:
    st.header("⚙️ 使用者配置")
    skills = st.multiselect("技能", ["Python", "Java", "JavaScript", "FastAPI", "Django"])
    experience = st.slider("經驗年資", 0, 10, 3)
    location = st.selectbox("期望地點", ["台北", "新竹", "台中", "高雄"])

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 對話歷史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 輸入框
if prompt := st.chat_input("輸入您的問題..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # API 調用
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = requests.post(
                "http://localhost:8000/api/chat",
                json={
                    "message": prompt,
                    "user_profile": {
                        "skills": skills,
                        "experience_years": experience,
                        "location": location
                    }
                }
            )
            result = response.json()["response"]
            st.markdown(result)

    st.session_state.messages.append({"role": "assistant", "content": result})
