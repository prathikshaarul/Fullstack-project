from flask import Flask, render_template, request, redirect, url_for, flash, session

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "timely_secret_key"

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        class_name = request.form.get('class')
        section = request.form.get('section')
        year = request.form.get('year')
        phone = request.form.get('phone')

        # Simple demo authentication
        if username == 'admin' and password == '1234':
            session['user'] = username
            flash(f'Welcome {username}! Login successful 🎉', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials 😢 Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out 👋', 'info')
    return redirect(url_for('home'))

# Run app (for local development)
if __name__ == '__main__':
    app.run(debug=True)
