from flask import Flask, render_template, request, redirect, url_for, session
import main  # This includes your Jarvis logic (speak, processcommand)

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for session

PASSWORD = "jarvis123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if pwd == PASSWORD:
            session['username'] = user
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid password")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    response = None
    if request.method == 'POST':
        command = request.form['command']
        response = main.processcommand(command)
        main.speak(response)

    return render_template('dashboard.html', user=session['username'], response=response)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
