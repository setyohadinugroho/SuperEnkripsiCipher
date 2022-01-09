from flask import Flask, request, render_template
from caesar import encrypt, decrypt
from transposisi import entrans, detrans
from superenkripsi import senkripsi, sdekripsi

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


# Kriptografi Klasik

@app.route("/caesar_e", methods=['GET', 'POST'])
def caesar_e():
    Encript = ""
    if request.method == 'POST':
        p = request.form['plain']
        k = int(request.form['key'])
        Encript = encrypt(p,k)
    return render_template('caesar_e.html', name="CE_Encript", Enkripsi=Encript, menu='kriptografi_klasik', submenu='caesar')

@app.route("/caesar_d", methods=['GET', 'POST'])
def caesar_d():
    Decrypt = ""
    if request.method == 'POST':
        c = request.form['cipher']
        k = int(request.form['key'])
        Decrypt = decrypt(c,k)
    return render_template('caesar_d.html', name = "CD_Dekripsi", Dekripsi=Decrypt, menu='kriptografi_klasik', submenu='caesar')

@app.route("/rot13")
def rot13():
    return render_template('rot13.html',menu='kriptografi_klasik', submenu='rot13')

@app.route("/tidakTeratur")
def tidakTeratur():
    return render_template('tidakTeratur.html',menu='kriptografi_klasik', submenu='tidakTeratur')

@app.route("/kalimatBermakna")
def kalimatBermakna():
    return render_template('kalimatBermakna.html',menu='kriptografi_klasik', submenu='kalimatBermakna')

@app.route("/affine")
def affine():
    return render_template('affine.html',menu='kriptografi_klasik', submenu='affine')

@app.route("/otp")
def otp():
    return render_template('otp.html',menu='kriptografi_klasik', submenu='otp')

@app.route("/kunciBerulang")
def kunciBerulang():
    return render_template('kunciBerulang.html',menu='kriptografi_klasik', submenu='kunciBerulang')


@app.route("/transposisi_e", methods=['GET', 'POST'])
def transposisi_e():
    TEEncript = ""
    if request.method == 'POST':
        p = request.form['t_plain']
        k = int(request.form['t_key'])
        TEEncript = entrans(p,k)
    return render_template('transposisi_e.html', name="TEEncript", TE_Enkripsi=TEEncript, menu='kriptografi_klasik', submenu='transposisi_e')

@app.route("/transposisi_d", methods=['GET', 'POST'])
def transposisi_d():
    TDDecript = ""
    if request.method == 'POST':
        c = request.form['t_cipher']
        k = int(request.form['t_key'])
        TDDecript = detrans(c,k)
    return render_template('transposisi_d.html', name="TDDecript", TD_Dekripsi=TDDecript, menu='kriptografi_klasik', submenu='transposisi_e')


@app.route("/superenkripsi_e", methods=['GET', 'POST'])
def superenkripsi_e():
    SEEncript = ""
    if request.method == 'POST':
        p = request.form['SE_plain']
        kc = int(request.form['SE_key_kc'])
        kt = int(request.form['SE_key_kt'])
        SEEncript = senkripsi(p,kc,kt)
    return render_template('superenkripsi_e.html', name="SEEncript", SE_Enkripsi=SEEncript, menu='kriptografi_klasik', submenu='superenkripsi_e')

@app.route("/superenkripsi_d", methods=['GET', 'POST'])
def superenkripsi_d():
    SEDecript = ""
    if request.method == 'POST':
        c = request.form['SE_cipher']
        kc = int(request.form['SE_key_kc'])
        kt = int(request.form['SE_key_kt'])
        SEDecript = sdekripsi (c,kc,kt)
    return render_template('superenkripsi_d.html', name="SEDecript", SE_Dekripsi=SEDecript, menu='kriptografi_klasik', submenu='superenkripsi_e')

@app.route("/superEnkripsi")
def superEnkripsi():
    return render_template('superEnkripsi.html',menu='kriptografi_klasik', submenu='superEnkripsi')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html',menu='kriptografi_klasik', submenu='vigenere')

@app.route("/homofonik")
def homofonik():
    return render_template('homofonik.html',menu='kriptografi_klasik', submenu='homofonik')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html',menu='kriptografi_klasik', submenu='playfair')

@app.route("/enigma")
def enigma():
    return render_template('enigma.html',menu='kriptografi_klasik', submenu='enigma')





# Kriptografi Modern
@app.route("/stream")
def stream():
    return render_template('stream.html',menu='kriptografi_modern', submenu='stream')

@app.route("/block")
def block():
    return render_template('block.html',menu='kriptografi_modern', submenu='block')

@app.route("/diffieHelman")
def diffieHelman():
    return render_template('diffieHelman.html',menu='kriptografi_modern', submenu='diffieHelman')

@app.route("/elgamal")
def elgamal():
    return render_template('elgamal.html',menu='kriptografi_modern', submenu='elgamal')

@app.route("/knapsack")
def knapsack():
    return render_template('knapsack.html',menu='kriptografi_modern', submenu='knapsack')

@app.route("/modulo")
def modulo():
    return render_template('modulo.html',menu='kriptografi_modern', submenu='modulo')



if __name__ == "__main__":
    app.run(debug = True)