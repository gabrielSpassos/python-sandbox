from googletrans import Translator

# Create a Translator object
translator = Translator()

# Translate text from English to Spanish
translated_text = translator.translate('Hello world', dest='es').text
print(f"Translated text (English to Spanish): {translated_text}")

# Translate text with automatic source language detection
translated_text_auto = translator.translate('Bonjour le monde', dest='en').text
print(f"Translated text (Auto-detect to English): {translated_text_auto}")
