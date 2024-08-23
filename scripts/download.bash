#!/bin/bash

# URL base for the API endpoint
BASE_URL="https://datos.gob.do/api/dataset"

# Number of total elements
TOTAL_ELEMENTS=959

# Interval for downloading elements in seconds
DOWNLOAD_INTERVAL=2

# Initialize the starting index
# start=0
start=904

# Loop to download the elements
while [ $start -lt $TOTAL_ELEMENTS ]; do
    # Construct the URL with the current index
    # url="${BASE_URL}?skip=${start}&limit=8"

    # Filename to save the data
    filename="data_${start}.json"

    echo "Downloading data from URL: $url"
    echo "Saving to file: $filename"

    # Download data using curl and save to a file
    # Check how to fall victime of claudefare human / user controls.
    # If not change this. When the downloads have break `grep -r -i --files-with-matches "Just a moment..."`
   curl "https://datos.gob.do/api/datasets?skip=$start" --compressed -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8' -H 'Accept-Language: es' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Connection: keep-alive' -H 'Cookie: _ga_GV77Z34G6S=GS1.1.1724344964.3.1.1724348726.0.0.0; _ga=GA1.1.602248903.1721752470; cookies_accepted=true; __cf_bm=S5mKRrEUTq0En2jGnpWGh1jSQhYPPYTdflvGFCNVwPw-1724349048-1.0.1.1-CO1AFN60Hel5oQGICUmAid5XbIcXyz6moxAliTmVAJwjo8cCUxzWRdK2D_ijhtEJpT.fdB9cPknThDXZs60Bsg; cf_clearance=5Q6ouZ.GbsCqvoO_nOzvtwe1ntImiSy3EQrSN3N7JvM-1724348692-1.2.1.1-yNLSozSSPzOtOCwYzV8TVNTqx1qi_uk4OuEZ54BaYDZl6txT6VNVJc.0.wdkevHXa8OSgxYmPH5Kq8sIQHMRzuMptNeYm8wpKHMQNeKIuvEY5Sa88udXOTqU0zttWKLLMEP46OqAed.ypxL8fGCmCj.s3Y24tms1NsxFd740moome2F9D9iRVliWSUamDiuuxxOdUykBlCRe5jINW5rH2hOB0ZxB8Qre9F5MbEuSchV4SnGVt7hfrOIsVxOlmj7BCOkVZzR4W7sJWLs7OdJNHDkDWnIc1MeRO5RVfctNio19UZG0ryLRaBGDBrv4aHdEI38bhw14Uac9nzcebVyoNLQ5oKYm9J5_K2d9RndwkB3dUTN_UsrmTHfCAiuE8mcQT_nZtfP7C1WMLNLca9VHvg' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: none' -H 'Sec-Fetch-User: ?1' -H 'Priority: u=0, i' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -o "$filename"
    
   #  curl -s "$url" -o "$filename"

    # Increment the start index by 8 (skip 8 elements)
    start=$((start + 8))
    


    # Sleep for the download interval
    echo "Waiting for $DOWNLOAD_INTERVAL seconds before the next download..."
    sleep $DOWNLOAD_INTERVAL
   
done

echo "Download process completed."

