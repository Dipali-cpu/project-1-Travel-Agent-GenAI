#  GENRARATIVE AI PLANNER DETAILS
"""
Create a streamlit python website with following parts
1 - a textbox for user to put the destination
2 - date picker
3 - submit button
4 - textbox to put number of adults and children
5 - put a textbox for user expectations 
6 - put a textbox for budget in dollars

when user clicks submit button call gemini ai model 
and display results on screen




"""

import streamlit as st
from datetime import date
import google.generativeai as genai
import os 

# Set your Gemini API Key here
GEMINI_API_KEY = "AIzaSyAjBNwH4dLwCvarj9b1Bg303pHlhEprhGk"


genai.configure(api_key=GEMINI_API_KEY)

# models = genai.list_models()
# for m in models:
    # print(m.name, m.supported_generation_methods)


# Replace with your actual API key
genai.configure(api_key="AIzaSyAjBNwH4dLwCvarj9b1Bg303pHlhEprhGk")


# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit UI
st.title("✈️ Travel Planner with Gemini AI")

destination = st.text_input("🌍 Enter your destination")
travel_date = st.date_input("📅 Pick your travel date", min_value=date.today())
num_people = st.text_input("👨‍👩‍👧‍👦 Number of adults and children (e.g., 2 adults, 1 child)")
expectations = st.text_area("🎯 What are your travel expectations? (e.g., adventure, relaxation, culture)")
budget = st.text_input("💰 Budget (in USD)")

if st.button("🚀 Submit"):
    with st.spinner("Talking to Gemini AI..."):

        prompt = f"""
        I want to travel to {destination} on {travel_date}.
        I will be traveling with {num_people}.
        My expectations are: {expectations}.
        My total budget is {budget} USD.
        Please suggest a travel plan with itinerary ideas, things to do, and travel tips.
        """

        try:
            response = model.generate_content(prompt)
            st.success("Here's what Gemini suggests:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error fetching response from Gemini: {e}")
