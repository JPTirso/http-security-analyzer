def check_header(headers, header_name):
    if header_name in headers:
        return headers[f"{header_name}"]

    return False

def analyze_headers(headers):
    security_headers = {
        "Strict-Transport-Security": check_header(
            headers,
            "Strict-Transport-Security"
        ),
        "Content-Security-Policy": check_header(
            headers,
            "Content-Security-Policy"
        ),
        "X-Content-Type-Options": check_header(
            headers,
            "X-Content-Type-Options"
        )
    }

    return security_headers