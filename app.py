from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- MOCK DATA (Data Palsu untuk Prototype) ---
# Dalam aplikasi nyata, ini akan diambil dari database.
lessons_data = {
    1: {
        "id": 1,
        "title": "Mengenal Huruf b dan d",
        "description": "Latihan membedakan bentuk huruf b (perut di depan) dan d (perut di belakang).",
        "content": "b", # Contoh konten visual
        "next_level": 2
    },
    2: {
        "id": 2,
        "title": "Mengenal Huruf p dan q",
        "description": "Latihan membedakan bentuk huruf p dan q.",
        "content": "p",
        "next_level": None # Akhir dari demo
    }
}

# --- ROUTES (Jalur Navigasi) ---

@app.route('/')
def login():            
    return render_template('login.html')

@app.route('/role')
def role():
    return render_template('role.html')

@app.route('/set_role', methods=['POST', 'GET'])
def set_role():
    # Mengambil data dari tombol yang ditekan (value="anak" atau value="orang_tua")
    peran = request.form.get('peran_user')
    
    if peran == 'anak':
        # Simpan status di session
        print(f"DEBUG: Pengguna memilih ANAK")
        return redirect(url_for('dashboard_child'))
        
    elif peran == 'orang_tua':
        # Simpan status di session
        print(f"DEBUG: Pengguna memilih ORANG TUA")
        return redirect(url_for('dashboard_parent'))
    
    # Jika error, kembalikan ke home
    return redirect(url_for('home'))


@app.route('/dashboard-orang-tua')
def dashboard_parent():
    """Halaman Dashboard Orang Tua (Memantau progress)"""
    return render_template('dashboard_parent.html')

@app.route('/dashboard-anak')
def dashboard_child():
    """Halaman Dashboard Anak (Menu memilih pelajaran)"""
    return render_template('dashboard_child.html')

@app.route('/lesson/<int:level_id>')
def lesson(level_id):
    """
    Halaman Pelajaran (Dinamis).
    Menerima parameter level_id untuk menentukan materi apa yang ditampilkan.
    """
    current_lesson = lessons_data.get(level_id)
    
    if not current_lesson:
        return "Pelajaran belum tersedia", 404
        
    return render_template('lesson.html', lesson=current_lesson)

@app.route('/example-lesson')
def example_lesson():            
    return render_template('sample_quiz.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)