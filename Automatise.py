import requests
import os

base_url = "http://editorial.htb"
endpoints = [
    "/api/latest/metadata/messages/promos",
    "/api/latest/metadata/messages/coupons",
    "/api/latest/metadata/messages/authors",
    "/api/latest/metadata/messages/how_to_use_platform",
    "/api/latest/metadata/changelog"
]

def make_request(endpoint):
    url = f"{base_url}{endpoint}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(f'response_{endpoint.replace("/", "_")}.html', 'w') as file:
            file.write(response.text)
        print(f'Response from {endpoint} saved to response_{endpoint.replace("/", "_")}.html')
    except requests.RequestException as e:
        print(f"Request failed for {endpoint}: {e}")

if __name__ == "__main__":
    if not os.path.exists('responses'):
        os.makedirs('responses')
    os.chdir('responses')
    for endpoint in endpoints:
        make_request(endpoint)
