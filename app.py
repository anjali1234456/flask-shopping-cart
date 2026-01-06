from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Product data
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000},
]

# Cart (stores added products)
cart = []

# Helper function: check if product is already added
def is_added(pid):
    for item in cart:
        if item["id"] == pid:
            return True
    return False


@app.route("/")
def home():
    return render_template(
        "index.html",
        products=products,
        is_added=is_added
    )


@app.route("/add/<int:pid>")
def add_to_cart(pid):
    # Add product only if not already added
    for item in cart:
        if item["id"] == pid:
            return redirect(url_for("home"))

    for p in products:
        if p["id"] == pid:
            cart.append(p)
            break

    return redirect(url_for("home"))


@app.route("/cart")
def view_cart():
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)


if __name__ == "__main__":
    app.run()
