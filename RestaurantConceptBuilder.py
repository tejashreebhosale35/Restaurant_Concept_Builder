import streamlit as st
import langchain_helper 

st.set_page_config(page_title="AI Restaurant Builder", page_icon="🍔", layout="centered")
st.title("🍔 AI Restaurant Concept Builder")

cuisine = st.sidebar.selectbox("Pick a cuisine", ["Indian", "Italian", "Mexican", "American"])
pricing_tier = st.sidebar.selectbox("Pick a pricing tier", ["Budget", "Mid-range", "High-end"])
design_vibe = st.sidebar.selectbox("Pick a design vibe", ["Modern", "Rustic", "Vintage", "Cozy"])


if cuisine:
    st.spinner("Analyzing culinary databases & designing graphics...")
    response = langchain_helper.generate_restaurant_name(cuisine, pricing_tier, design_vibe)
    col1, col2 = st.columns([1, 1])
                
    with col1:
                    st.subheader("Brand Identity")
                    st.markdown(f"### **`{response["restaurant_name"].strip('"' + "'")}`**")
                    st.caption(f"Theme Concept: Modern {cuisine} Dining")
    with col2:
                    st.subheader("Curated Menu Draft")
                    
                    # Parse menu lines safely using Regex
                    parsed_items = response["menu_items"].split(",")
                    
                    if parsed_items:
                        for item_name in parsed_items:
                            st.markdown(f"**🔹 {item_name.strip()}**")
                       