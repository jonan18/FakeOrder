import pytest
from application import create_app

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('application.config_order.TestingConfig')
    with app.app_context():
        yield app 
