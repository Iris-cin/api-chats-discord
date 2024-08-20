import requests

# Générer une clé API
response = requests.post("http://127.0.0.1:5000/generate-key")
api_key = response.json().get("api_key")
print(f"Generated API Key: {api_key}")

# Utiliser la clé API pour obtenir une image de chat
response = requests.get(f"http://127.0.0.1:5000/random-cat?api_key={api_key}")
cat_image_url = response.json().get("image_url")
print(f"Random Cat Image URL: {cat_image_url}")
