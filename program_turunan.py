import numpy as np

def f(x):
    # Definisi fungsi
    return x**2

def selisih_maju(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def selisih_mundur(f, x, h=1e-5):
    return (f(x) - f(x - h)) / h

def selisih_nilai_tengah(f, x, h=1e-5):
    return (f(x + h/2) - f(x - h/2)) / h

# Contoh penggunaan
x_titik = 2.0

sel_maju = selisih_maju(f, x_titik)
sel_mundur = selisih_mundur(f, x_titik)
sel_n_tengah = selisih_nilai_tengah(f, x_titik)

print(f'Turunan maju dari f({x_titik}) adalah {sel_maju}')
print(f'Turunan mundur dari f({x_titik}) adalah {sel_mundur}')
print(f'Turunan nilai tengah dari f({x_titik}) adalah {sel_n_tengah}')
