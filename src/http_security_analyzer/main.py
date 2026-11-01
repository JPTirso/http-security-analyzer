from http_security_analyzer.analyzer import make_request

url = "https://google.com"

response = make_request(url)

print("Status:", response.status_code)
print("URL:", response.url)
print("Headers:", response.headers)