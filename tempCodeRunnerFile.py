@app.route("/caesar_e", methods=['GET', 'POST'])
# def caesar_e():
#     Encript = ""
#     if request.method == 'POST':
#         p = request.form['plain']
#         k = int(request.form['key'])
#         Encript = encrypt(p,k)
#     return render_template('caesar_e.html', name="CE_Encript", Enkripsi=Encript, menu='kriptografi_klasik', submenu='caesar')

# @app.route("/caesar_d", methods=['GET', 'POST'])
# def caesar_d():
#     Decrypt = ""
#     if request.method == 'POST':
#         c = request.form['cipher']
#         k = int(request.form['key'])
#         Decrypt = decrypt(c,k)
#     return render_template('caesar_d.html', name = "CD_Dekripsi", Dekripsi=Decrypt)
