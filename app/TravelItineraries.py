import streamlit as st
import google.generativeai as genai

# Configure API key
api_key = ""
genai.configure(api_key=api_key)

# Function to generate a travel itinerary based on user input
def generate_itinerary(destination, days, nights):
   
    model_name = "gemini-2.5-flash" 
    
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
    )

    prompt = f"Create a high-quality travel itinerary for {days} days and {nights} nights in {destination}."
    
    response = model.generate_content(prompt)
    return response.text


# Streamlit app
def main():
    st.title("Travel Itinerary Generator")

    destination = st.text_input("Enter your desired destination:")
    days = st.number_input("Enter the number of days:", min_value=1)
    nights = st.number_input("Enter the number of nights:", min_value=0)

    if st.button("Generate Itinerary"):
        if destination.strip() and days > 0 and nights >= 0:
            try:
                itinerary = generate_itinerary(destination, days, nights)
                st.text_area("Generated Itinerary:", value=itinerary, height=300)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please make sure all inputs are provided and valid.")


if __name__ == "__main__":
    main()
