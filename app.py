import streamlit as st

st.set_page_config(
  page_title="Exploring Malaysia Through Data",
  page_icon="📊",
  layout="wide"
)

st.title("Exploring Malaysia Through Data")
st.subheader("A Scientific Visualization Assignment Project")

st.markdown("""
Welcome to my data visualization application.

This project explores three imprttant aspects of Malaysia:

1.**Household Income** - Changes in mean and median household income across Malaysian states.
2.**Marriage Statistics** - Marriage trends and differences between males and females across states.
3.**Schools by District** - Distribution of schools across Malaysian states, districts and education stages.

Use the navigation menu on the left to explore each dataset and its visualizations.
""")

st.info("Select a page from the sidebar to begin exploring the visualizations.")
