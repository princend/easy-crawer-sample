from flask import Flask
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template_string
from fetch_data import fetch_data  # 引入之前编写的爬虫函数

app = Flask(__name__)

@app.route('/')
def index():
    data = fetch_data()
    html = get_html()
    return render_template_string(html, data=data)



def get_html():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>爬虫数据展示</title>
    <!-- 引入 Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { font-family: Arial, sans-serif; }
        .item { margin-bottom: 20px; }
        .item img { max-width: 100%; height: auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">爬虫数据展示</h1>
        <div class="row">
            {% for item in data %}
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{{ item.img }}" class="card-img-top" alt="{{ item.title }}">
                        <div class="card-body">
                            <h5 class="card-title">
                                <a href="{{ item.link }}" class="text-dark">{{ item.title }}</a>
                            </h5>
                            <p class="card-text">评分: {{ item.score }}</p>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>

    <!-- 引入 Bootstrap JS 和 jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

'''

if __name__ == '__main__':
    app.run(debug=True)