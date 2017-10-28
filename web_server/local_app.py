from app_factory import create_app

if __name__ == '__main__':
    app = create_app()
    app.run('localhost', 35000, debug=True)
