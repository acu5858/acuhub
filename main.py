"""
ACU.HUB | Simulation Admin Panel
Türkiye simülasyonunda hayatta kalanlar için web portalı.
"""

import os
from flask import Flask, render_template, request, jsonify

import logic
from tests_data import get_all_tests, get_test_by_id, calculate_test_result

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

TOOLS = [
    {"id": "vize-final", "name": "Vize-Final Hesaplayıcı", "desc": "Finalden kaç alman lazım?", "emoji": "📊", "category": "akademik"},
    {"id": "kyk-butce", "name": "KYK / Enflasyon Bütçesi", "desc": "Ayın kaçında makarna başlar?", "emoji": "💸", "category": "finans"},
    {"id": "yalan-dedektor", "name": "Yalan Dedektörü", "desc": "Kolpa mı gerçek mi?", "emoji": "🤥", "category": "sosyal"},
    {"id": "github-readme", "name": "GitHub Readme Generator", "desc": "Havalı profil oluştur", "emoji": "💻", "category": "tech"},
    {"id": "kaos-olcer", "name": "Kaos Seviyesi Ölçer", "desc": "Bugün dışarı çıkmalı mısın?", "emoji": "🌪️", "category": "gunluk"},
    {"id": "kurumsal-cevirici", "name": "Kurumsal Çevirici", "desc": "Beyaz yaka dili", "emoji": "👔", "category": "kariyer"},
    {"id": "bahane-uretici", "name": "Bahane Üretici PRO", "desc": "Teknik bahaneler", "emoji": "🛠️", "category": "tech"},
    {"id": "yemek-carki", "name": "Yemek Çarkı", "desc": "Bugün ne yesem?", "emoji": "🎰", "category": "gunluk"},
    {"id": "pomodoro", "name": "Pomodoro Timer", "desc": "Zamanlayıcı", "emoji": "⏱️", "category": "verimlilik"},
    {"id": "sifre-guc", "name": "Şifre Güçlendirici", "desc": "Şifren ne kadar zayıf?", "emoji": "🔐", "category": "tech"},
    {"id": "doviz-duvari", "name": "Döviz Ağlama Duvarı", "desc": "Kurları gör, ağla", "emoji": "💔", "category": "finans"},
    {"id": "muhendislik-secici", "name": "Mühendislik Alanı Seçici", "desc": "Ruhun hangi mühendis?", "emoji": "⚙️", "category": "kariyer"},
    {"id": "renk-secici", "name": "Renk Seçici", "desc": "Rastgele pastel renk", "emoji": "🎨", "category": "tasarim"},
    {"id": "metin-kasa", "name": "Metin Kasa", "desc": "Base64 / ROT13 şifreleme", "emoji": "🔤", "category": "tech"},
    {"id": "gno-hesap", "name": "GNO Hesaplayıcı", "desc": "Notu ne kadar eder?", "emoji": "📈", "category": "akademik"},
]


@app.route('/')
def dashboard():
    """Ana sayfa - Dashboard"""
    tests = get_all_tests()
    return render_template('dashboard.html', tools=TOOLS, tests=tests)


@app.route('/tools/<tool_id>')
def tool_page(tool_id):
    """Araç sayfası"""
    tool = next((t for t in TOOLS if t['id'] == tool_id), None)
    if not tool:
        return render_template('404.html'), 404
    return render_template('tool.html', tool=tool)


@app.route('/tests')
def tests_list():
    """Testler listesi sayfası"""
    tests = get_all_tests()
    return render_template('tests.html', tests=tests)


@app.route('/tests/<test_id>')
def test_page(test_id):
    """Test sayfası"""
    test = get_test_by_id(test_id)
    if not test:
        return render_template('404.html'), 404
    return render_template('test_detail.html', test=test)


@app.route('/api/vize-final', methods=['POST'])
def api_vize_final():
    """Vize-Final hesaplayıcı API"""
    data = request.get_json()
    vize = float(data.get('vize', 0))
    vize_weight = int(data.get('vize_weight', 40))
    result = logic.calculate_grade(vize, vize_weight)
    return jsonify(result)


@app.route('/api/kyk-butce', methods=['POST'])
def api_kyk_budget():
    """KYK bütçe hesaplayıcı API"""
    data = request.get_json()
    income = float(data.get('income', 0))
    result = logic.calculate_kyk_budget(income)
    return jsonify(result)


@app.route('/api/yalan-dedektor', methods=['POST'])
def api_bullshit():
    """Yalan dedektörü API"""
    data = request.get_json()
    text = data.get('text', '')
    result = logic.detect_bullshit(text)
    return jsonify(result)


@app.route('/api/github-readme', methods=['POST'])
def api_github_readme():
    """GitHub README generator API"""
    data = request.get_json()
    name = data.get('name', '')
    username = data.get('username', '')
    result = logic.generate_github_readme(name, username)
    return jsonify(result)


@app.route('/api/kaos-olcer', methods=['POST'])
def api_chaos():
    """Kaos seviyesi ölçer API"""
    data = request.get_json()
    factors = data.get('factors', [])
    result = logic.calculate_chaos_level(factors)
    return jsonify(result)


@app.route('/api/kurumsal-cevirici', methods=['POST'])
def api_corporate():
    """Kurumsal çevirici API"""
    data = request.get_json()
    text = data.get('text', '')
    result = logic.translate_to_corporate(text)
    return jsonify(result)


@app.route('/api/bahane-uretici', methods=['POST'])
def api_excuse():
    """Bahane üretici API"""
    result = logic.generate_tech_excuse()
    return jsonify(result)


@app.route('/api/yemek-carki', methods=['POST'])
def api_food():
    """Yemek çarkı API"""
    result = logic.spin_food_wheel()
    return jsonify(result)


@app.route('/api/pomodoro', methods=['POST'])
def api_pomodoro():
    """Pomodoro timer API"""
    data = request.get_json()
    mode = data.get('mode', 'work')
    result = logic.get_pomodoro_settings(mode)
    return jsonify(result)


@app.route('/api/sifre-guc', methods=['POST'])
def api_password():
    """Şifre güçlendirici API"""
    data = request.get_json()
    password = data.get('password', '')
    result = logic.analyze_and_strengthen_password(password)
    return jsonify(result)


@app.route('/api/doviz-duvari', methods=['POST'])
def api_currency():
    """Döviz ağlama duvarı API"""
    result = logic.get_currency_wall()
    return jsonify(result)


@app.route('/api/muhendislik-secici', methods=['POST'])
def api_engineering():
    """Mühendislik alanı seçici API"""
    result = logic.select_engineering_field()
    return jsonify(result)


@app.route('/api/renk-secici', methods=['POST'])
def api_color():
    """Renk seçici API"""
    result = logic.generate_random_color()
    return jsonify(result)


@app.route('/api/metin-kasa', methods=['POST'])
def api_text_encode():
    """Metin şifreleme API"""
    data = request.get_json()
    text = data.get('text', '')
    method = data.get('method', 'base64')
    result = logic.encode_text(text, method)
    return jsonify(result)


@app.route('/api/gno-hesap', methods=['POST'])
def api_gno():
    """GNO hesaplayıcı API"""
    data = request.get_json()
    current_gno = float(data.get('current_gno', 3.0))
    new_grade = float(data.get('new_grade', 3.0))
    result = logic.calculate_gno(current_gno, new_grade)
    return jsonify(result)


@app.route('/api/test-result', methods=['POST'])
def api_test_result():
    """Test sonucu hesaplama API"""
    data = request.get_json()
    test_id = data.get('test_id', '')
    answers = data.get('answers', [])
    result = calculate_test_result(test_id, answers)
    return jsonify(result)


@app.after_request
def after_request(response):
    """Cache-Control header'ı ekle."""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
