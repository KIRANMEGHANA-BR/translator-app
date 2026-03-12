from deep_translator import GoogleTranslator

def get_supported_languages():
    """Returns a dictionary of supported languages {name: code}"""
    try:
        return GoogleTranslator().get_supported_languages(as_dict=True)
    except Exception:
        # Fallback to a basic list if API fails for some reason
        return {'english': 'en', 'spanish': 'es', 'french': 'fr', 'german': 'de', 'chinese (simplified)': 'zh-CN', 'hindi': 'hi', 'arabic': 'ar', 'russian': 'ru'}

def translate_text(text, source='auto', target='en'):
    """Translates text from source to target language"""
    if not text or not text.strip():
        return ""
    try:
        translator = GoogleTranslator(source=source, target=target)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Error translating text: {str(e)}"
