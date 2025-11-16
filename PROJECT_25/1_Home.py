import streamlit as st

st.set_page_config(
    page_title="Network Toolkit",
    page_icon="🛠️",
)

st.title("🛠️ GCEK IT3501: Network Project Toolkit")
st.subheader("Welcome to your combined network utility application.")

st.info("Please select a tool from the sidebar on the left to begin.")

st.markdown("""
This application combines all the Streamlit projects for your Computer Networks course:

* **Subnet Calculator:** (Unit 4) Analyze IPv4 networks, classes, and visualize subnets.
* **Port Scanner:** (Unit 5) Check for open TCP ports on a target host.

""")