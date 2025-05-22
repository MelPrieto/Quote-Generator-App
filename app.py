import streamlit as st
from fpdf import FPDF 

st.set_page_config(page_title="Quote Generator", layout="centered")

st.title("📄 Quote Generator App")

project = st.text_input("Enter the Project Description: ")
estimated_hours = st.number_input("Enter the stimated hours: ", min_value=0)
hourly_rate = st.number_input("Enter the hourly rate: ", min_value=0)
delivery_time = st.text_input("Enter the delivery time: ")

if st.button("Generate Quote PDF"):
    if project and estimated_hours and hourly_rate and delivery_time:
        total = estimated_hours * hourly_rate

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.image("Template.png", x=0, y=0, w=210, h=297)
        pdf.text(120, 155, project)
        pdf.text(120, 175, str(estimated_hours))
        pdf.text(120, 198, str(hourly_rate))
        pdf.text(120, 222, delivery_time)
        pdf.set_font("Arial", style="B", size=18)
        pdf.text(120, 245, str(total))
        pdf.output("Quote.pdf")

        with open("Quote.pdf", "rb") as file:
            st.download_button(
                label="📥 Download PDF Quote",
                data=file,
                file_name="Quote.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Please fill in all fields.")