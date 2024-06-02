from flask import Flask, request
from taylormade import desktop
from taylormade import mobile
from werkzeug.user_agent import UserAgent


def run(host="127.0.0.1", debug=False, port=5000, ssl_context=None):
    app = Flask(__name__)
    # return app


    @app.route('/')
    def root():
        user_agent = UserAgent(request.headers.get('User-Agent'))
        if user_agent.platform in ['android', 'iphone', 'ipad']:
            return mobile.home_page.site()
        else:
            return desktop.home_page.site()
    
    
    app.run(host=host, debug=debug, port=port, ssl_context=ssl_context)


if __name__ == '__main__':
    run()
