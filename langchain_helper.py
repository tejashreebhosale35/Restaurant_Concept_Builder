from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv("SecretKey.env")

if "GROQ_API_KEY" not in os.environ or "OPENAI_API_KEY" not in os.environ:
    st.error("🔑 Missing Credentials! Please check your .env file layout.")
    st.stop()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.0, max_retries=2)

def generate_restaurant_name(cuisine, pricing_tier, design_vibe):
    prompt_template_name = PromptTemplate.from_template(
        "Generate a creative restaurant name for a {cuisine} restaurant with a {pricing_tier} pricing tier and a {design_vibe} design vibe. Only one name please return just the restaurant name in plain text without any formatting or punctuation."
    )
    chain1 = prompt_template_name | llm | StrOutputParser()
    prompt_template_menuitems = PromptTemplate.from_template(
        "Generate a list of creative menu items for a {cuisine} restaurant. The restaurant price point is {pricing_tier} and the ambiance vibe is {design_vibe}. Return ONLY the 10 items separated by commas. Do not use bullet points, numbering, or introductory text."
    )

    chain2 = prompt_template_menuitems | llm | StrOutputParser()

    return {
        "restaurant_name": chain1.invoke({"cuisine": cuisine, "pricing_tier": pricing_tier, "design_vibe": design_vibe}),
        "menu_items": chain2.invoke({"cuisine": cuisine, "pricing_tier": pricing_tier, "design_vibe": design_vibe}),
    }