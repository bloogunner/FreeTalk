from models.translation_model import TranslationModel

def main():
    
    translator = TranslationModel()
    
    
    result = translator.translate(
        text="Hello, How are you?",
        source_language="en",
        target_language="es"
    )
    
    print(result)
    
    
    
if __name__ == "__main__":
    main()