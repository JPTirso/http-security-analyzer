from http_security_analyzer.analyzer import make_request
from http_security_analyzer.checks import analyze_headers

url = input("Digite a URL desejada: ")

response = make_request(url)
if response:
    print("Status:", response.status_code)
    print("URL:", response.url)

    results = analyze_headers(response.headers)

    print("\nAnálise de segurança:")
    for header, present in results.items():
        if present:
            print(f"[+] {header}: {present} \n")
        else:
            print(f"[-] {header}: Ausente")

else:
    print("Não foi possível analisar o site.")