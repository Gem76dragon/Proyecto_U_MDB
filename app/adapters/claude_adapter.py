from anthropic import Anthropic
from app.ports.claude_port import ClaudePort

class ClaudeAdapter(ClaudePort):
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20240620"

    def generate_response(self, prompt, temperature, max_tokens):
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            raise Exception(f"Error en la llamada a la API de Claude: {str(e)}")