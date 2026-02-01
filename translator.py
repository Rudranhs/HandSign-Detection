from googletrans import Translator

# Function to translate text from English to Gujarati or vice versa
def translate_text(input_text, target_language='gu'):
    translator = Translator()
    
    try:
        # Detect the source language automatically
        detected_lang = translator.detect(input_text).lang
        
        # Translate to the target language
        print(f"Detected language: {detected_lang}, translating to {target_language}...")
        translation = translator.translate(input_text, dest=target_language)
        
        # Return the translated text
        return translation.text
    
    except Exception as e:
        return f"Error in translation: {e}"





