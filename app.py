import streamlit as st

st.set_page_config(
    page_title="StudySpace",
    page_icon="🎀",
    layout="wide"
)

# Pastel design
st.markdown("""
<style>
.stApp {
    background-color: #FAF7FF;
}
h1, h2, h3 {
    color: #7653A6;
}
div.stButton > button {
    background-color: #DCC9FF;
    color: #382653;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
}
div.stButton > button:hover {
    background-color: #C6AEF8;
    color: #382653;
}
div[data-testid="stTextInput"] input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎀 StudySpace")
st.sidebar.write("Your little study corner")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📚 My Subjects", "✅ My Goals"]
)

st.sidebar.divider()
st.sidebar.caption("Small steps, big dreams ✨")

# Home page
if page == "🏠 Home":

    st.title("🎓 Welcome to StudySpace!")
    st.write("A little progress every day adds up 💗")

    name = st.text_input("What should we call you?")

    if name:
        st.success(f"Welcome back, {name}! ✨")

    st.subheader("🌷 Your Study Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📚 YOUR SUBJECTS")
        st.metric("Available", 4)

    with col2:
        st.info("🌸 YOUR MOTIVATION")
        st.write("Keep learning!")

    with col3:
        st.info("✨ YOUR DAILY GOAL")
        st.write("One step at a time")

    st.subheader("💜 Quick Study")

    subject = st.selectbox(
        "What would you like to study?",
        ["Python", "Physics", "Mathematics", "English"]
    )

    if st.button("🚀 Let's Start Studying"):
        st.balloons()
        st.success(f"Let's study {subject}!")

# Subjects page
elif page == "📚 My Subjects":

    st.title("📚 My Study Subjects")

    st.write("Choose a subject and get started!")

    st.markdown("""
    - 🐍 Python
    - ⚡ Physics
    - ➗ Mathematics
    - 📝 English
    """)

# Goals page
# Goals page
elif page == "✅ My Goals":

    st.title("✅ My Study Goals")
    st.write("Small steps, big dreams! 🌷")

    # Remember goals while the website is running
    if "goals" not in st.session_state:
        st.session_state.goals = []

    # Add a new goal
    with st.form("goal_form"):
        goal = st.text_input("What do you want to accomplish?")
        submitted = st.form_submit_button("➕ Add Goal")

        if submitted:
            if goal.strip():
                st.session_state.goals.append({
                    "task": goal.strip(),
                    "done": False
                })
                st.rerun()
            else:
                st.warning("Please enter a goal first!")

    st.divider()
    st.subheader("🌸 My To-Do List")

    # Display goals
    if not st.session_state.goals:
        st.info("No goals yet. Add your first goal above! 💗")

    for i, item in enumerate(st.session_state.goals):
        item["done"] = st.checkbox(
            item["task"],
            value=item["done"],
            key=f"goal_{i}"
        )

    completed = sum(
        item["done"] for item in st.session_state.goals
    )

    total = len(st.session_state.goals)

    st.progress(completed / total if total else 0)
    st.write(f"✨ Completed: {completed} out of {total} goals")