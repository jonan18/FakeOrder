from application import create_app
from application.auth import RsaSingleton

app = create_app()

app.app_context().push()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=13003)
