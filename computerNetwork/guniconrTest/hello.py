def application(environ, start_response):
    start_response('401 OK', [('Content-Type', 'application/json')])
    return '{\'wang\': \'wang\'}'
