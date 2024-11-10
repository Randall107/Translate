from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from readfile import reader
from vocabs import vocabs

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://Jeng:database42069@Jeng.mysql.pythonanywhere-services.com/Jeng$dictionary".format(
    username="Jeng",
    password="",
    hostname="Jeng.mysql.pythonanywhere-services.com",
    databasename="Jeng$dictionary",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Words(db.Model):

    __tablename__ = "words"

    word = db.Column(db.String(1000), primary_key=True)
    translations = db.Column(db.String(4096))

class WordModel():
    def ConvertToList(self):
        return self.translation_clone.split(", ")

    def __init__(self, word_clone, translation_clone):
        self.word_clone = word_clone
        self.translation_clone = translation_clone

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error_page.html')

@app.route('/', methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("home_page.html")

@app.route('/product/<name>')
def get_product(name):
    return 'The product is ' + str(name)

@app.route('/dict/<w>/<v>', methods=["GET", "POST"])
def add_word(w, v):
    if request.method == "GET":
        wd = Words(word=w,translations="หมา")
        db.session.add(wd)
        db.session.commit()
        v = Words(word=v,translations="asd")
        db.session.add(v)
        db.session.commit()
        return "word is " + str(w) + " " + str(v)

@app.route('/upload')
def add_sample():
    man = reader
    l = man.read(man, r"/home/Jeng/mysite/xml/sample2")
    converter = vocabs(l)
    dic = converter.convert(l)
    k = list(dic.keys())
    v = list(dic.values())
    i = 0
    while i < len(dic):
        en=k[i]
        translation = ''.join(map(str, v[i]))
        if Words.query.filter(Words.word == en).first():
            w = Words.query.filter(Words.word == en).first()
            w.translations = w.translations + " ," + translation
        else:
            w = Words(word=en,translations=translation)
            db.session.add(w)
            db.session.commit()
        i = i + 1
    return dic

@app.route('/addnon')
def add():
    with open(r"/home/Jeng/mysite/xml/non_existing", 'r') as file:
        lines = file.readlines()
        for line in lines:
            temp = ""
            try:
                x = line.split(":")
                en = x[0]
                temp = en
                th = x[1][1:-1]
                if Words.query.filter(Words.word == en).first():
                    w = Words.query.filter(Words.word == en).first()
                    w.translations = w.translations + ", " + request.form["upt"]
                    db.session.commit()
                else:
                    w = Words(word=en,translations=th)
                    db.session.add(w)
                    db.session.commit()
            except:
                return temp
    return "completed!"

@app.route('/download')
def download():
    entries = Words.query.all()
    with open(r"/home/Jeng/mysite/xml/db", 'a') as file:
        for entry in entries:
            file.write(f"{entry.word}\n")
    return "Completed!"

@app.route('/post', methods=["GET", "POST"])
def post():
    if request.method == "GET":
        return render_template("main_page.html", words=Words.query.all())

    w = Words(word=request.form["en"],translations=request.form["th"])
    db.session.add(w)
    db.session.commit()
    view_model = WordModel(w.word, w.translations)
    l = view_model.ConvertToList()
    return render_template("main_page.html", en_value=request.form["en"],translations=l)

@app.route('/del', methods=["GET", "POST"])
def delete():
    if request.method == "GET":
        return render_template("del_page.html")

    en = request.form["en"]
    if Words.query.filter(Words.word == en).first():
        w = Words.query.filter(Words.word == en).first()
        db.session.delete(w)
        db.session.commit()
        return redirect(url_for('delete'))
    else:
        return render_template("del_page.html",en_value=en,translations=["Word not found."])


@app.route('/update', methods=["GET", "POST"])
def update():
    if request.method == "GET":
        return render_template("update_page.html")

    en = request.form["en"]
    if Words.query.filter(Words.word == en).first():
        w = Words.query.filter(Words.word == en).first()
        w.translations = w.translations + ", " + request.form["upt"]
        db.session.commit()
        return redirect(url_for('update'))
    else:
        return render_template("update_page.html",en_value=en,translations=["Word not found."])

@app.route('/read', methods=["GET", "POST"])
def read():
    if request.method == "GET":
        return render_template("read_page.html",en_value="",translations=[])
    en=request.form["en"].lower()
    if Words.query.filter(Words.word == en).first():
        w = Words.query.filter(Words.word == en).first()
        view_model = WordModel(w.word, w.translations)
        l = view_model.ConvertToList()
        no_dupes = []
        i = 0
        while i < len(l):
            if l[i] not in no_dupes:
                no_dupes.append(l[i])
            i = i + 1
        return render_template("read_page.html",en_value=en,translations=no_dupes)
    else:
        return render_template("read_page.html",en_value=en,translations=["Word not found."])


