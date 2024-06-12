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
    return response.text  # Cambiado a texto

def fetch_dumps(dump_type, token):
    url = f"{BASE_URL}/dumps/{dump_type}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print("Respuesta de fetch_dumps:", response.text)  # Añadido para depuración
    response.raise_for_status()
    return response.content  # Cambiado a contenido binario para manejar archivos

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
        
        challenge_instructions = fetch_challenge(token)
        print(f"Instrucciones del desafío: {challenge_instructions}")
        
        # Basado en las instrucciones del desafío, el usuario debe elegir el tipo de dump
        # Aquí elige uno de los tipos de dump especificados en las instrucciones
        dump_type = "mysql"  # Puede ser 'mysql', 'psql' o 'onlinepsql'
        
        dump_data = fetch_dumps(dump_type, token)
        # Guardar el dump en un archivo para ser importado en la base de datos local
        with open(f"dump_{dump_type}.sql", "wb") as file:
            file.write(dump_data)
        print(f"Dump {dump_type} guardado en dump_{dump_type}.sql")
        
        # Aquí debes importar manualmente el dump en tu base de datos local según las instrucciones

        # Una vez importado, puedes continuar con la inspección y el desafío

        # Se asume que tienes acceso al dump y puedes cargarlo para su inspección
        # dumps = cargar_datos_desde_base_de_datos_local()
        # number_of_groups = calculate_number_of_groups(dumps)
        # answer = solve_challenge(dumps)
        
        # validation_response = validate_answer(token, number_of_groups, answer)
        # print(f"Respuesta de validación: {validation_response}")
        
    except requests.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except KeyError as e:
        print(f"Error de clave: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
