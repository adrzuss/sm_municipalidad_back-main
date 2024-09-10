from app import create_app, reset_db

app = create_app()

if __name__ == "__main__":
    # reset_db(app)
    app.run(debug=True)
