"""
log_in.py
a library that lets you connect to fuzer - requires a cookie.txt file and handles the session creating automatically.
"""
import requests
from http.cookiejar import MozillaCookieJar
import pathlib
    
# main
def cookied_session(filename):
    s = requests.Session()
    cookies = MozillaCookieJar(filename)
    cookies.load(ignore_discard=True, ignore_expires=True)
    s.cookies = cookies

    return s

