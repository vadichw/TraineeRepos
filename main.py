import requests

def check_security_headers(url):
    response = requests.get(url)
    security_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-XSS-Protection"
    ]
    
    missing_headers = []
    for header in security_headers:
        if header not in response.headers:
            missing_headers.append(header)
    
    if missing_headers:
        print(f"Отсутствуют заголовки безопасности: {', '.join(missing_headers)}")
    else:
        print("Все основные заголовки безопасности присутствуют.")

# Использование
url = "https://www.github.com/"
check_security_headers(url)

