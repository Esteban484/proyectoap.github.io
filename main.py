from flask import Flask,render_template,request
import funciones

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/result',methods=['POST',"GET"] )
def result ():
  output= request.form.to_dict()
  texto=output["abc"]
  archivo=output["archivo"]
  
  if(texto!=""):
    norm=funciones.discriminatorio1(texto)
    norm2=funciones.discriminatorio2(texto)
    return render_template("index.html",norm=norm,norm2=norm2,texto=texto)
  elif(archivo!=""):
    norm=funciones.discriminatorio1(archivo)
    norm2=funciones.discriminatorio2(archivo)
    return render_template("index.html",norm=norm,norm2=norm2,texto=archivo)
  #norm=funciones.normalizar(archivo)
  


  
app.run(host='0.0.0.0', port=80)
