import os
import google.generativeai as genai

# Conectamos con la IA usando tu llave secreta
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-3.8-flash')

# Le damos la instrucción de actuar como un experto en cultura pop
prompt = """
Identifica las 3 series o películas que son mayor tendencia mundial esta semana en redes sociales.
Genera una lista de 30 palabras clave en español para bloquear spoilers de esas tendencias (nombres de personajes principales, villanos, actores, y términos como 'muerte', 'final', 'post-créditos').
Devuelve ÚNICAMENTE un archivo JSON válido con esta estructura exacta, sin texto adicional:
{
  "tendencias_semana": ["palabra1", "palabra2", "palabra3"]
}
"""

response = model.generate_content(prompt)
texto_json = response.text.replace('```json', '').replace('```', '').strip()

# El bot crea o sobreescribe el archivo público
with open('tendencias.json', 'w', encoding='utf-8') as f:
    f.write(texto_json)

print("Archivo tendencias.json actualizado con éxito con los spoilers de esta semana.")
