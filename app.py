# from flask import Flask

# app = Flask(__name__) #creates app

# @app.route("/") # URL endpoint

# #def home() -> function runs when URL is opened
# def home():
#     return "My first Devops project"

# if __name__ == "__main__":
#     app.run(debug=True)
    
# @app.route("/about")
# def about():
#     return "This is DevOps Project"

# @app.route("/user/<name>")
# def user(name):
#     return f"Hello {name}"


#-----------------SQL------------------------

from flask import Flask, render_template, request
import pymysql
import time
time.sleep(20)

app = Flask(__name__)

# DB connection
db = pymysql.connect(
    host="db",
    user="root",
    password="root",
    database="devops_db"
)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

db.commit()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    
    print("Received:", name, age)
    
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    db.commit()

    return f"User {name} added successfully!"

@app.route("/users")
def users():
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")
    db.commit()
    data = cursor.fetchall()

    return str(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    