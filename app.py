from flask import Flask, render_template, redirect, url_for
from scrape_menu import scrape_menu

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    menu_data = scrape_menu()
    return render_template('menu.html', menu=menu_data)

if __name__ == '__main__':
    app.run()
