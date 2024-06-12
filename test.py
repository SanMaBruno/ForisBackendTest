import requests

BASE_URL = "http://mini-challenge.foris.ai"
USERNAME = "foris_challenge"
PASSWORD = "ForisChallenge"

def authenticate(username, password):
    url = f"{BASE_URL}/login"
    credentials = {"username": username, "password": password}
    response = requests.post(url, json=credentials)
    response.raise_for_status()
    response_json = response.json()
    print("Respuesta de autenticación:", response_json)  # Añadido para depuración
    if 'access_token' not in response_json:
        raise KeyError("No se encontró el token en la respuesta de autenticación.")
    return response_json["access_token"]

def fetch_challenge(token):
    url = f"{BASE_URL}/challenge"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Respuesta de fetch_challenge:", response.text)  # Añadido para depuración
    response.raise_for_status()
    return response.json()

def fetch_dumps(dump_type, token):
    url = f"{BASE_URL}/dumps/{dump_type}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Respuesta de fetch_dumps:", response.text)  # Añadido para depuración
    response.raise_for_status()
    return response.json()

def validate_answer(token, number_of_groups, answer):
    url = f"{BASE_URL}/validate"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"number_of_groups": number_of_groups, "answer": answer}
    response = requests.post(url, json=body, headers=headers)
    print("Respuesta de validate_answer:", response.text)  # Añadido para depuración
    response.raise_for_status()
    return response.json()

def calculate_number_of_groups(dumps):
    # Implementa la lógica para calcular el número de grupos
    groups = dumps.get("groups", [])
    return len(groups)

def solve_challenge(dumps):
    # Implementa la lógica para resolver el desafío
    # Esto depende de la estructura de los datos proporcionados en el dump
    # Por ahora, devuelve una respuesta simulada
    return "simulated_answer"

def main():
    try:
        token = authenticate(USERNAME, PASSWORD)
        print(f"Token obtenido: {token}")
        
        challenge = fetch_challenge(token)
        dump_type = challenge.get("dump_type")
        print(f"Tipo de dump obtenido: {dump_type}")
        
        dumps = fetch_dumps(dump_type, token)
        number_of_groups = calculate_number_of_groups(dumps)
        print(f"Número de grupos calculado: {number_of_groups}")
        
        answer = solve_challenge(dumps)
        print(f"Respuesta del desafío: {answer}")
        
        validation_response = validate_answer(token, number_of_groups, answer)
        print(f"Respuesta de validación: {validation_response}")
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except KeyError as e:
        print(f"Error de clave: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
