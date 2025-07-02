
from google.ai import generativelanguage_v1beta as generativelanguage
from google.ai.generativelanguage_v1beta.types import generation_config

# 初始化模型客戶端
client = generativelanguage.GenerativeLanguageServiceClient()
model_name = "models/gemini-1.5-pro-latest"

def generate_answer(prompt, temperature, max_tokens):
    generation_cfg = generation_config.GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
    )
    request = generativelanguage.GenerateTextRequest(
        model=model_name,
        prompt=generativelanguage.TextPrompt(text=prompt),
        generation_config=generation_cfg,
    )
    response = client.generate_text(request=request)
    return response.candidates[0].output

if __name__ == "__main__":
    question = "What is the capital of France?"
    answer = generate_answer(question, temperature=0.7, max_tokens=50)
    print("Q:", question)
    print("A:", answer)
