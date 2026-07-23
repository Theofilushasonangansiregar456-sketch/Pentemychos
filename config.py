import os

class Config:
    # Secret key utama untuk enkripsi data session login
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pente_mychos_secret_quantum_key_2026'
    
    # Jika nanti kamu mau pakai database (misal SQLite/MySQL), taruh konfigurasinya di sini
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Mode Debug (Otomatis restart server Flask tiap ada perubahan kode)
    DEBUG = True