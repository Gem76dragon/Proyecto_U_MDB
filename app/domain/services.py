class ConfigurationService:
    def __init__(self, file_adapter, claude_adapter):
        self.file_adapter = file_adapter
        self.claude_adapter = claude_adapter

    def generate_prompt(self, file_contents):
        system_prompt = """Eres un ingeniero de desarrollo de software especializado en configuración. 
Tu tarea es generar un archivo de configuración para la Plataforma A. Este archivo será descargable a través de una interfaz web. 
Sigue estas instrucciones cuidadosamente:"""

        user_prompt  = f"""1. Utiliza el contenido del archivo 'plantilla.txt' como base para la estructura del archivo de configuración.
2. Asigna los valores a cada campo según las reglas definidas en el archivo 'reglas.txt'.
3. El archivo de salida debe estar en formato [plantilla.txt]
4. Si encuentras campos en la plantilla que no tienen reglas correspondientes, déjalos en blanco y añade un comentario indicando 'Regla no encontrada'.
5. Si una regla no se puede aplicar (por ejemplo, datos faltantes o inconsistentes), utiliza un valor predeterminado y añade un comentario explicativo.
6. Al finalizar, valida que el archivo generado cumple con todas las reglas aplicables.


Contenido de entrada.txt:
{file_contents.get('entrada.txt', 'Archivo no encontrado')}

Contenido de plantilla.txt:
{file_contents.get('plantilla.txt', 'Archivo no encontrado')}

Contenido de reglas.txt:
{file_contents.get('reglas.txt', 'Archivo no encontrado')}

Por favor, genera el archivo de configuración siguiendo estas instrucciones."""
        
        formatted_prompt = f"{system_prompt}\n\nHuman: {user_prompt}\n\nAssistant: Entendido. Procederé a generar el archivo de configuración para la Plataforma A siguiendo las instrucciones proporcionadas.\n\nHuman: Excelente, por favor procede con la generación del archivo de configuración.\n\nAssistant:"

        return formatted_prompt       
        
    def generate_configuration(self, prompt, temperature, max_tokens):
        return self.claude_adapter.generate_response(prompt, temperature, max_tokens)
