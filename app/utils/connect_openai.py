import openai

from app.core.config import Settings

def send_msg_to_openai(prompt):
    errors = "超时错误，请重试！"
    try:
        # 使用自定义HTTP客户端
        openai.api_key = Settings.Openai["secret"]
        client = openai.Client(
            api_key=Settings.Openai["secret"],
            base_url=Settings.Openai["openai_host"]  # 使用自定义的API端点
        )
        
        response = client.Completion.create(
            model=Settings.Openai["model"],
            prompt=prompt,
            max_tokens=150
        )
        
        # 正确处理响应
        if response.choices:
            return response.choices[0].text.strip()
        else:
            return errors
    except Exception as e:
        return f"{errors} 异常信息: {str(e)}"