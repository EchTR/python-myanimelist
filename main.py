# github.com/echtr

from re import search
from mal import Anime, AnimeSearch
from flask import Flask, render_template, url_for, request

# 35507 => classroom of the elite

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/get_anime", methods = ["POST"])
def get_anime():
    anime_name = request.form["anime_name"]
    search = AnimeSearch(anime_name)
    f_anime = search.results[0]

    # def variables
    title = f_anime.title
    url_ = f_anime.url
    

    vl_1 = 0
    char_ = 0
    anime_id = ""
    checkp1 = 0
    checkp2 = 0
    print(url_)
    for i in url_:
        if i == "/":
            vl_1 += 1
            if vl_1 == 4:
                checkp1 = char_
            if vl_1 == 5:
                checkp2 = char_
        
        char_ += 1
    anime_id = url_[checkp1+1:checkp2]

    new_anime = Anime(anime_id)
    #buraya kadar, önce aranan isim ile ilgili animeyi açtım. 
    #sonra o animenin url adresinden anime id'i aldım. sonra da o anime id'e bağlanıp 
    #modülün her özelliğinden faydalandım.
    image_url = new_anime.image_url
    type_ = new_anime.type
    score = new_anime.score
    synopsis = new_anime.synopsis
    episodes = new_anime.episodes
    scored_by = new_anime.scored_by
    title_eng = new_anime.title_english
    characters = new_anime.characters
    len_ = len(characters)
    aired = new_anime.aired

    if request.method == "POST":
        return render_template("anime.html",
        title = title,
        url_ = url_,
        image_url = image_url,
        type_ = type_,
        score = score,
        synopsis = synopsis,
        episodes = episodes,
        scored_by = scored_by,
        title_eng = title_eng,
        len_ = len_,
        characters = characters,
        aired = aired
        )
    else:
        return "wrong usage!"
    
app.run()