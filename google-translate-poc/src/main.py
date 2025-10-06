import asyncio
from googletrans import Translator

# # Create a Translator object
# translator = Translator()

# # Translate text from English to Spanish
# translated_text = translator.translate('Hello world', dest='es').text
# print(f"Translated text (English to Spanish): {translated_text}")

# # Translate text with automatic source language detection
# translated_text_auto = translator.translate('Bonjour le monde', dest='en').text
# print(f"Translated text (Auto-detect to English): {translated_text_auto}")

async def translate_text():
    async with Translator() as translator:
        result = await translator.translate('안녕하세요.')
        print(result)
        result = await translator.translate('안녕하세요.', dest='pt')
        print(result)
        result = await translator.translate('Hello', src='en', dest='pt')
        print(result)

asyncio.run(translate_text())
