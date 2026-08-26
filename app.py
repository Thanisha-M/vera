import streamlit as st

st.title("Vera — Psychometric Analysis Tool")
st.subheader("Automated Assessment ^& Dimension Scoring")

st.write("Rate the following statements from 1 ^(Strongly Disagree^) to 5 ^(Strongly Agree^):")

q1 = st.slider("I enjoy solving complex analytical problems.", 1, 5, 3)
q2 = st.slider("I feel energized when working in fast-paced teams.", 1, 5, 3)
q3 = st.slider("I pay close attention to small operational details.", 1, 5, 3)

if st.button("Generate Assessment Report"):
    analytical_score = (q1 / 5) * 100
    collaboration_score = (q2 / 5) * 100
    detail_score = (q3 / 5) * 100
    st.success("Report Generated Successfully!")
    st.metric("Analytical Thinking", f"{analytical_score:.0f}%%")
    st.metric("Team Collaboration", f"{collaboration_score:.0f}%%")
    st.metric("Attention to Detail", f"{detail_score:.0f}%%")
