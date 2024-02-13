from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_bmi.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    if request.method == 'POST':
        tinggi = float(request.form['tinggi'])
        berat = float(request.form['berat'])
        bmi = calculate_bmi_value(tinggi, berat)
        category = get_bmi_category(bmi)
        return render_template('result_bmi.html', tinggi=tinggi, berat=berat, bmi=bmi, category=category)

def calculate_bmi_value(tinggi, berat):
    return round(berat / ((tinggi / 100) ** 2), 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Kurus'
    elif 18.5 <= bmi < 24.9:
        return 'Ideal'
    elif 25 <= bmi < 29.9:
        return 'Kelebihan Berat Badan'
    else:
        return 'Obesitas'

if __name__ == '__main__':
    app.run(debug=True)
