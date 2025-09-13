import streamlit as st
from PIL import Image
import pytesseract

# Dummy AI model for product suggestions
eco_tips = {
    'plastic bag': 'Switch to cloth bags for a lower carbon footprint.',
    'bottle water': 'Opt for reusable bottles over single-use plastic.',
    'meat': 'Try plant-based protein once a week for reduced emissions.',
    'chips': 'Choose snacks with recyclable packaging.',
    'milk': 'Consider locally sourced dairy or plant milk.'
}

st.title("Green Consumption Advisor 🛒🌱")
st.markdown("**Upload your grocery bill/food receipt, get AI-powered sustainability tips!**")

uploaded_file = st.file_uploader("Upload an image of your bill/ticket", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Bill/Receipt", use_column_width=True)
    st.markdown("---")

    bill_text = pytesseract.image_to_string(image)
    st.markdown("#### Detected Items from Bill:")
    st.code(bill_text)

    found_items = []
    tips_shown = False
    for item, tip in eco_tips.items():
        if item in bill_text.lower():
            found_items.append((item, tip))
            st.success(f"**{item.capitalize()}** found! Tip: {tip}")
            tips_shown = True

    if not tips_shown:
        st.info("No eco-related items detected. Try a clearer image or add more items to your bill!")

    st.markdown("#### General Green Tips")
    st.markdown("- Prefer reusable over single-use items.\n- Buy local to reduce transportation emissions.\n- Always check for recyclable packaging.")

st.markdown("---")
st.caption("Powered by Streamlit, OCR, and AI for a sustainable lifestyle.")

# Requirements: pip install streamlit pillow pytesseract
# For deployment on Streamlit Cloud: Just upload this script and dependencies in requirements.txt
