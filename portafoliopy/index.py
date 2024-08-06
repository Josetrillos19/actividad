from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/respuesta', methods=['POST'])
def respuesta():
    if request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        suma = n1 + n2
        return render_template('formulario.html', res=suma)

@app.route('/formulario1')
def formulario1():
    return render_template('formulario1.html')

@app.route('/promedio', methods=['POST'])
def promedio():
    if request.method == 'POST':
        m1 = int(request.form['m1'])
        m2 = int(request.form['m2'])
        m3 = int(request.form['m3'])
        Promedio = m1+m2+m3/3
        return render_template('formulario1.html', pro=Promedio)
    

@app.route('/formulario3')
def formulario3():
    return render_template('formulario3.html')

@app.route('/notas', methods=['POST'])
def notas():
    if request.method == 'POST':
        nota = int(request.form['nota'])
        if nota >= 19 and nota <=20:
            mensaje="A"
        elif nota>16 and nota <=18:
            mensaje="B"
        elif nota > 13 and nota <=15:
            mensaje="C"
        elif nota>10 and nota <=12:
            mensaje="D"
        elif nota > 1 and nota <=9:
            mensaje="E"
        elif nota >=20:
            mensaje="demasiado digitos"
        return render_template('formulario3.html', men=mensaje)

   
@app.route('/formulario4')
def formulario4():
    return render_template('formulario4.html')
@app.route('/camisas', methods=['POST'])
def camisas(): 
     if request.method == 'POST':
        total1 = int(request.form['total1'])
        total2 = int(request.form['total2'])
        total3 = int(request.form['total3'])
        total4 = int(request.form['total4'])
        total5 = int(request.form['total5'])
        dolar= total1 + total2 + total3+total4+total5
        peso=dolar*4000
        return render_template('mayor.html', pesos=peso)

@app.route('/doble', methods=['GET', 'POST'])
def doble():
    resultado = None 
    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])
            doble = numero * 2
            triple = numero * 3
            resultado = {'doble': doble,'triple': triple}
        except ValueError:
            resultado = "Error"
    return render_template('doble.html', resultado=resultado)

@app.route('/area', methods=['GET', 'POST'])
def are():
    figura = None
    area_calculada = None
    error = None

    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area_calculada = 3.14159 * (radio ** 2)
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area_calculada = lado ** 2
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                area_calculada = largo * ancho
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area_calculada = 0.5 * base * altura
            else:
                error = "Figura no válida."
        except ValueError:
            error = "ingrese valores válidos."

    return render_template('area.html', figura=figura, area=area_calculada, error=error)


@app.route('/mayormenor', methods=['GET', 'POST'])
def mayormenor():
    mayor = None
    menor = None
    error = None

    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])

            if len({a, b, c}) != 3:
                error = "Los valores deben ser distintos."
            else:
                mayor = max(a, b, c)
                menor = min(a, b, c)

        except ValueError:
            error = "ingrese solo números enteros."

    return render_template('mayormenor.html', mayor=mayor, menor=menor, error=error)

            

              
if __name__ == '__main__':
    app.run()

   