#!/bin/bash
#Displays the size of the body of the request
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -d " " -f2
