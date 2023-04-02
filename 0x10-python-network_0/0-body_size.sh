#!/bin/bash

# Check if the URL is provided as an argument
if [ -z "$1" ]
then
  echo "Error: No URL provided"
  exit 1
fi

# Send a request to the URL using curl and store the response in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

# Display the size of the body of the response
echo "Size of the body of the response: $response bytes"

