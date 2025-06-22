def test_app_creation():
    from app.main import create_app
    app = create_app()
    assert app is not None
