from wsgiref import simple_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    start_response(status, headers)

    html = b'<h1>Hello From WSGI.</h1>'
    return [html]


if __name__ == '__main__':
    # WSGIサーバーを起動
    host = '0.0.0.0'
    port = 8880
    server = simple_server.make_server(host, port, application)

    print("Start server: http://{}:{}".format(host, port))
    server.serve_forever()
