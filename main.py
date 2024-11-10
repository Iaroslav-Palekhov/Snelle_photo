from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Путь к файлу JSON
JSON_FILE = 'data.json'

# Функция для загрузки услуг и фотографий из JSON-файла
def load_data():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump({'services': [], 'photos': []}, f, ensure_ascii=False, indent=4)
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Функция для сохранения услуг и фотографий в JSON-файл
def save_data(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('oper.html')

@app.route('/m')
def indexm():
    data = load_data()  # Загружаем данные из JSON
    return render_template('indexm.html', services=data['services'], photos=data['photos'])


@app.route('/pc')
def indexpc():
    data = load_data()  # Загружаем данные из JSON
    return render_template('indexpc.html', services=data['services'], photos=data['photos'])

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    data = load_data()
    if request.method == 'POST':
        service_name = request.form.get('service_name')
        price = request.form.get('price')
        if service_name and price:
            data['services'].append({'name': service_name, 'price': price})
            save_data(data)
        return redirect(url_for('admin'))

    return render_template('admin.html', services=data['services'])

@app.route('/manage_photos', methods=['GET', 'POST'])
def manage_photos():
    data = load_data()
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        if image_url:
            data['photos'].append(image_url)  # Добавляем изображение в отдельный список
            save_data(data)
        return redirect(url_for('manage_photos'))

    return render_template('ph.html', photos=data['photos'])

@app.route('/delete_service/<int:index>')
def delete_service(index):
    data = load_data()
    if 0 <= index < len(data['services']):
        data['services'].pop(index)
        save_data(data)
    return redirect(url_for('admin'))

@app.route('/delete_photo/<int:index>')
def delete_photo(index):
    data = load_data()
    if 0 <= index < len(data['photos']):
        data['photos'].pop(index)  # Удаляем фотографию из списка
        save_data(data)
    return redirect(url_for('manage_photos'))

if __name__ == '__main__':
    app.run(debug=True)