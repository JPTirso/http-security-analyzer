import requests
from urllib.parse import urlparse

def validate_url(url):
    if not url:
        raise ValueError("URL não preenchida")

    parsed_url = urlparse(url)

    if not parsed_url.scheme:
        print("URL informada sem protocolo HTTP/HTTPS")

        scheme = input("Você deseja colocar https ou http? ").strip().lower()

        if scheme not in ["https", "http"]:
            raise ValueError("Nome do protocolo inválido")

        url = f"{scheme}://{url}"
        parsed_url = urlparse(url)

    elif parsed_url.scheme not in ["http", "https"]:
        raise ValueError("Protocolo inválido. Utilize HTTP ou HTTPS.")

    if not parsed_url.hostname:
        raise ValueError("Domínio do site inválido")

    return url

def make_request(url):
    try:
        newURL = validate_url(url)
        response = requests.get( newURL, timeout=10 )

        return response

    except requests.exceptions.Timeout:
        print("Erro: tempo limite da requisição excedido.")

    except requests.exceptions.ConnectionError:
        print("Erro: não foi possível conectar ao servidor.")

    except requests.exceptions.MissingSchema:
        print("Erro: URL sem protocolo HTTP ou HTTPS.")

    except requests.exceptions.RequestException as error:
        print(f"Erro na requisição: {error}")

    except ValueError as e:
        print(e)

    return None