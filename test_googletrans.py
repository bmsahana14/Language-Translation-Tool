import streamlit as st
from googletrans import Translator  

# Language mapping for target languages
language_mapping = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Hindi": "hi",
    "Russian": "ru",
    "Telugu": "te",
    "Kannada": "kn"
}

# Inject custom CSS for galaxy-themed background
st.markdown(
    """
    <style>
    body {
        background-size: cover; /* Cover the entire page */
        color: #FFFFFF; /* White text */
    }
    .stTextArea label, .stSelectbox label {
        color: #FFFFFF; /* Label text color */
    }
    .translated-text {
        color: #E80606; /*  blue translated text */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.title(" Language Translation Tool ")

# Input for text to translate
text_to_translate = st.text_area("Enter text to translate")

# Dropdown to select target language
selected_language_name = st.selectbox("Select target language:", list(language_mapping.keys()))

# Translation button
if st.button("Translate"):
    if text_to_translate:
        target_language = language_mapping[selected_language_name]
        try:
            translator = Translator()
            # Translate the text
            translated_text = translator.translate(text_to_translate, dest=target_language).text
            st.markdown(f"<div class='translated-text'>{translated_text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error during translation: {e}")
    else:
        st.warning("Please enter text to translate.")
