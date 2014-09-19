from app import app
if __name__ == "__main__":
    from app import db
    db.create_all()
    app.run(debug = True) #We will set debug false in production 
