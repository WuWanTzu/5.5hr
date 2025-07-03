
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

# 設定 API 金鑰
genai.configure(api_key="YOUR_API_KEY")  # 請記得換成你自己的 API 金鑰

# 初始化模型
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_answer(prompt, temperature, max_tokens):
    """
    產生回答的函數，支援溫度和最大 token 數。

    參數：
    - prompt (str): 問題或提示
    - temperature (float): 模型生成的隨機程度
    - max_tokens (int): 限制回答的最大長度

    回傳：
    - str: 模型生成的回答
    """

    # 建立 GenerationConfig
    config = GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_tokens
    )

    # 使用設定生成回答
    response = model.generate_content(
        prompt,
        generation_config=config
    )

    return response.text

# 測試用範例（提交後可以刪掉）
if __name__ == "__main__":
    prompt = "What is the capital of France?"
    temperature = 0.7
    max_tokens = 100

    answer = generate_answer(prompt, temperature, max_tokens)
    print("Generated Answer:", answer)
