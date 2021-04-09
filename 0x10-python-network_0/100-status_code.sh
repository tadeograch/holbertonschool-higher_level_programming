#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -so /dev/null -Iw "%{http_code}" "$1"