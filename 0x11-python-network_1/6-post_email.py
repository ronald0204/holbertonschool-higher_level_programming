#!/usr/bin/python3
"""sends a POST request"""
import sys
import requests as rq


if __name__ == "__main__":
    r = rq.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
