import asyncio
from googletrans import Translator

async def translate_text():
    async with Translator() as translator:
        result = await translator.translate('안녕하세요.')
        print(result)
        result = await translator.translate('안녕하세요.', dest='pt')
        print(result)
        result = await translator.translate('Hello', src='en', dest='pt')
        print(result)

        # Translate list
        translations = await translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='pt')
        for translation in translations:
            print(translation.origin, ' -> ', translation.text)

asyncio.run(translate_text())
