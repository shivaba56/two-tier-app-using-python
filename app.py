from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="*****",       # replace mysql server privateip
        user="***",         # Replace with your MySQL username
        password="*****",    # Replace with your MySQL password
        database="user_db"   # Replace with your database name
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Get data from form
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']  # In a real app, hash the password before storing!

    try:
        # Create database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert user data into the database
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect('/')  # Redirect to the index page after successful registration

    except Error as e:
        return f"Error: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)

