from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
# Key untuk enkripsi session login
app.secret_key = 'pente_mychos_secret_quantum_key_2026' 

# Data akun dummy untuk login kelompok kamu
USER_DATA = {
    "pente@gmail.com": "jamal123"
}

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email in USER_DATA and USER_DATA[email] == password:
            session['user'] = email
            return jsonify({"status": "success", "redirect": url_for('dashboard')})
        else:
            return jsonify({"status": "error", "message": "Email atau Password salah!"}), 401
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)