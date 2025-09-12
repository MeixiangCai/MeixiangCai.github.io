# Image Enhancement: Dehazing

## Objective
Perform **image dehazing** on a picture by sending requests to an image enhancement API.

## Process
1. Obtain `request_url`, `data`, and `headers`, then convert the image into **Base64** encoding.  
2. Call the image dehazing API, send the request, and retrieve the Base64-encoded result.  
3. Decode the Base64 output back into an image.  

- A test image is provided as a reference.  