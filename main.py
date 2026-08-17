from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    products = ["Ноутбук", "Миша", "Клавіатура"]
    # products = []  # для перевірки випадку без товарів

    return render_template("shop.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)