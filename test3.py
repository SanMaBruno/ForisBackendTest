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
    print("Respuesta de autenticación:", response_json)
    if 'access_token' not in response_json:
        raise KeyError("No se encontró el token en la respuesta de autenticación.")
    return response_json["access_token"]

def fetch_challenge(token):
    url = f"{BASE_URL}/challenge"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Respuesta de fetch_challenge:", response.text)
    response.raise_for_status()
    return response.text

def fetch_dumps(dump_type, token):
    url = f"{BASE_URL}/dumps/{dump_type}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Respuesta de fetch_dumps:", response.text)
    response.raise_for_status()
    return response.content

def validate_answer(token, number_of_groups, answer):
    url = f"{BASE_URL}/validate"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"number_of_groups": number_of_groups, "answer": answer}
    response = requests.post(url, json=body, headers=headers)
    print("Respuesta de validate_answer:", response.text)
    response.raise_for_status()
    return response.json()

def main():
    try:
        token = authenticate(USERNAME, PASSWORD)
        print(f"Token obtenido: {token}")
        
        challenge_instructions = fetch_challenge(token)
        print(f"Instrucciones del desafío: {challenge_instructions}")
        
        dump_type = "mysql"  # Puede ser 'mysql', 'psql' o 'onlinepsql'
        
        dump_data = fetch_dumps(dump_type, token)
        with open(f"dump_{dump_type}.sql", "wb") as file:
            file.write(dump_data)
        print(f"Dump {dump_type} guardado en dump_{dump_type}.sql")
        
        # Resultados obtenidos de las consultas SQL
        number_of_groups = 168  # Reemplaza con el resultado de la consulta
        answer = 28  # Reemplaza con el resultado de la consulta
        
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
