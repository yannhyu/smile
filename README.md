# smile
SDC
"Good thing you found us, and we found you."

# Setup
(venv) >:~/Documents/dev/smile$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 04, 2019 - 03:04:51
Django version 2.0.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

# Check endpoint with httpie
(venv) >:~/Documents/dev/smile$ http GET http://127.0.0.1:8000/testcommentview/
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 89
Content-Type: application/json
Date: Thu, 04 Jul 2019 03:01:35 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "content": "foo bar",
    "created": "2019-07-04T03:01:35.800708Z",
    "email": "leila@example.com"
}
