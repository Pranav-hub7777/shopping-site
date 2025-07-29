from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_products():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    items = c.fetchall()
    conn.close()
    return items

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id = ?", (id,))
    item = c.fetchone()
    conn.close()
    return render_template('product.html', product=item)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    cart = session.get('cart', [])
    cart.append(id)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    items = []
    for id in cart:
        c.execute("SELECT * FROM products WHERE id = ?", (id,))
        items.append(c.fetchone())
    conn.close()
    return render_template('cart.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
