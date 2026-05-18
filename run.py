from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🚀 Servidor iniciando...")
    app.run(debug=app.config.get('DEBUG', False))