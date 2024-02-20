import openai

# OpenAI API key
openai.api_key = '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'

def detect_language(text):
    prompt = f"Text: \"{text}\" Language:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1
    )

    language = response.choices[0].text.strip()
    return language

def translate_text(text, target_language):
    prompt = f"{text} {target_language} Translation:"

    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    translated_text = response.choices[0].text.strip()
    return translated_text


input_text = input()
detected_language = detect_language(input_text)
print("Detected Language:", detected_language)

target_language = input()  
translated_text = translate_text(input_text, target_language)
print(f"Translated to {target_language}: {translated_text}")
