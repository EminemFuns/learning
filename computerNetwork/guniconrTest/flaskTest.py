from flask import Flask

app = Flask(__name__)


@app.route('/rest-api/v1/vcs/images', methods=['GET','POST'])
def hello_world():
    return '{"detail": "Given token not valid for any token type", ' \
           '"code": "token_not_valid","messages": [{'\
           '"message": "Token is invalid or expired",'\
           '"token_class": "AccessToken",' \
           '"token_type": "access"}]}', 401


if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()