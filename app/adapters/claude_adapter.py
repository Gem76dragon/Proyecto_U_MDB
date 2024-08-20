from anthropic import Anthropic, APIError
from app.ports.claude_port import ClaudePort



def set_api_key(api_key):
    CLAUDE_API_KEY = api_key

class ClaudeAdapter(ClaudePort):
    def __init__(self):
        if CLAUDE_API_KEY is None:
            raise ValueError("API key no configurada. Usa set_api_key() para configurar la clave API.")
        self.client = Anthropic(api_key=CLAUDE_API_KEY)
        self.model = "claude-3-5-sonnet-20240620"

    def generate_response(self, prompt, temperature, max_tokens):
        try:
            message = self.client.completions.create(
                model=self.model,
                max_tokens_to_sample=max_tokens,
                temperature=temperature,
                prompt=f"\n\nHuman: {prompt}\n\nAssistant: ",
            )
            return message.completion
        except APIError as e:
            if e.status_code == 401:
                raise Exception(f"Error de autenticación: Clave API inválida. Por favor, verifica tu clave API.")
            else:
                raise Exception(f"Error en la llamada a la API de Claude: {str(e)}")
        except Exception as e:
            raise Exception(f"Error inesperado en la llamada a la API de Claude: {str(e)}")