from flask import render_template, Flask
from werkzeug.exceptions import NotFound

app = Flask(__name__)


@app.get("/", endpoint="home")
def get_home():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def get_about():
    return render_template("about.html")


@app.errorhandler(404)
def handle_404(error):
    if isinstance(error, NotFound) and error.description != NotFound.description:
        return error
    return f"<h1>eroror: {error}</h1>"


if __name__ == "__main__":
    app.run(debug=True)




"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""