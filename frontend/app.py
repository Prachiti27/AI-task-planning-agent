import streamlit as st
import requests

st.set_page_config(
    page_title="AI Task Planner",
    layout="centered"
)

if "plan_data" not in st.session_state:
    st.session_state.plan_data = None

st.title("AI Task Planner")
st.caption("Convert a goal and timeline into a clear execution plan")

st.divider()

goal = st.text_input(
    "Goal",
    placeholder="Prepare for placements"
)

days = st.number_input(
    "Total days available",
    min_value=1,
    step=1
)

generate = st.button("Generate plan")

if generate:
    if not goal.strip():
        st.warning("Please enter a goal.")
    else:
        with st.spinner("Planning…"):
            res = requests.post(
                "http://127.0.0.1:8000/generate-plan",
                json={"goal": goal, "days": days},
                timeout=60
            )
            st.session_state.plan_data = res.json()

if st.session_state.plan_data:
    data = st.session_state.plan_data

    st.divider()
    st.subheader("Your plan")

    for idx, item in enumerate(data["plan"], start=1):
        st.markdown(
            f"""
            **{idx}. {item['task']}**  
            _{item['estimated_days']} days · {item['priority']} priority_
            """
        )

    st.divider()

    st.download_button(
        "Download as Notion checklist",
        data=data["markdown"],
        file_name="task_plan.md",
        mime="text/markdown",
        key="download_markdown_single"
    )

st.divider()
st.caption("AI Task Planning Agent")
