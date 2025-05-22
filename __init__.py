from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm3

@app.route('/encrypt/<string:key>/<string:data>')
def encrypt_data(key, data):
    """Chiffre une chaîne de caractères avec une clé donnée."""
    try:
        fernet = Fernet(key.encode())
        encrypted_data = fernet.encrypt(data.encode())
        return f"Valeur chiffrée : {encrypted_data.decode()}"
    except Exception as error:
        return f"Erreur lors du chiffrement : {str(error)}"

@app.route('/decrypt/<string:key>/<string:data>')
def decrypt_data(key, data):
    """Déchiffre une chaîne chiffrée avec une clé donnée."""
    try:
        fernet = Fernet(key.encode())
        decrypted_data = fernet.decrypt(data.encode())
        return f"Valeur déchiffrée : {decrypted_data.decode()}"
    except Exception as error:
        return f"Erreur lors du déchiffrement : {str(error)}"

@app.route('/generate-key')
def generate_personal_key():
    """Génère une nouvelle clé de chiffrement."""
    new_key = Fernet.generate_key()
    return f"Voici votre clé personnelle : {new_key.decode()}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
