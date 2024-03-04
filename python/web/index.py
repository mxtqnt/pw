import cgi
from wsgiref import simple_server

def app(environ, start_response):
    path = environ["PATH_INFO"]
    method = environ["REQUEST_METHOD"]
    data=b""
    if path == "/app":
        data = b"Hello, Web!\n"
    if path == "/app/feedback":
        if method == "POST":
            body = cgi.FieldStorage(fp=environ["wsgi.input"], environ=environ)
            message = body.getvalue('name') + " " + body.getvalue('email') + " " + body.getvalue('feedback')
            data = message.encode('utf-8')
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]

if __name__ == '__main__':
    w_s = simple_server.make_server(
        host="",
        port=8000,
        app=app
    )
    w_s.serve_forever()