import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="📊",
    layout="centered"
)

# Application title
st.title("📊 Customer Information App")

st.write("Welcome! This is my first Streamlit application.")

st.divider()

# User input
st.header("Customer Details")

name = st.text_input("Customer Name")

age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100,
    value=25
)

monthly_charges = st.number_input(
    "Monthly Charges (KES)",
    min_value=0.0,
    value=1500.0,
    step=100.0
)

# Button
if st.button("Submit Information"):

    if name.strip():

        st.success("Information submitted successfully!")

        st.subheader("Customer Summary")

        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Monthly Charges:** KES {monthly_charges:,.2f}")

        if monthly_charges > 3000:
            st.warning("This customer has relatively high monthly charges.")
        else:
            st.info("This customer has moderate monthly charges.")

    else:
        st.error("Please enter the customer's name.")

st.divider()

st.caption("Built with Python and Streamlit")
