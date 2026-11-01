import requests

def make_request(url):
    try:
        response = requests.get(
            url,
            timeout=10
        )

        return response

    except requests.exceptions.Timeout:
        print("Erro: tempo limite da requisição excedido.")

    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")

    except requests.exceptions.MissingSchema:
        print("Erro: URL sem protocolo HTTP ou HTTPS.")

    except requests.exceptions.RequestException as error:
        print(f"Erro na requisição: {error}")

    return None