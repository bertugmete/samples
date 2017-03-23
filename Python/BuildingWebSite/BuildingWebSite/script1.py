from flask import Flask , render_template
#html file'lar icin render_template ekledik.Klasor acarken templates olayina dikkat etmek gerekli. 
app = Flask(__name__)

@app.route("/")
def home():
    #render template ile olusturdugumuz html sayfalarina yonlendirme yapiyoruz.
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)

