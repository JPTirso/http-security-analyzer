from http_security_analyzer.analyzer import make_request

url = input("Digite a URL desejada: ")

response = make_request(url)
if response:
    print("Status:", response.status_code)
    print("URL:", response.url)
    print("Headers:", response.headers)
else:
    print("Não foi possível analisar o site.")