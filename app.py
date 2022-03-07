# data comes from http://www.omdbapi.com made by Brian Fritz. All content licensed under CC BY-NC 4.0.

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/homepage", methods=["GET"])
def hello_world():
    return {"movies": [ {
    "Title": "Nightmare Alley",

    "Released": "17 Dec 2021",
    "Runtime": "150 min",
    "Genre": "Crime, Drama, Thriller",
    "Director": "Guillermo del Toro",
    "Writer": "Guillermo del Toro, Kim Morgan, William Lindsay Gresham",
    "Actors": "Bradley Cooper, Cate Blanchett, Toni Collette",
    "Plot": "An ambitious carny with a talent for manipulating people with a few well-chosen words hooks up with a female psychiatrist who is even more dangerous than he is.",
    "Language": "English",
    "Country": "United States, Mexico, Canada",
    "Awards": "Nominated for 4 Oscars. 14 wins & 89 nominations total",
    "Poster":
      "https://m.media-amazon.com/images/M/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
    "Response": "True",
  },
   {
    "Title": "Spider-Man",

    "Released": "03 May 2002",
    "Runtime": "121 min",
    "Genre": "Action, Adventure, Sci-Fi",
    "Director": "Sam Raimi",
    "Actors": "Tobey Maguire, Kirsten Dunst, Willem Dafoe",
    "Plot": "When bitten by a genetically modified spider, a nerdy, shy, and awkward high school student gains spider-like abilities that he eventually must use to fight evil as a superhero after tragedy befalls his family.",
    "Country": "United States",
    "Poster":
      "https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SX300.jpg",
    "Response": "True",
  },
  {
    "Title": "Avatar",

    "Released": "18 Dec 2009",
    "Runtime": "162 min",
    "Genre": "Action, Adventure, Fantasy",
    "Director": "James Cameron",
    "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver",
    "Plot": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "Country": "United States",
   "Awards": "Won 3 Oscars. 89 wins & 131 nominations total",
    "Poster":
      "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
    "Response": "True",
  },
  {
    "Title": "Titanic",
    "Released": "19 Dec 1997",
    "Runtime": "194 min",
    "Genre": "Drama, Romance",
    "Director": "James Cameron",
    "Actors": "Leonardo DiCaprio, Kate Winslet, Billy Zane",
    "Plot": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
    "Country": "United States, Mexico",
    "Poster":
      "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
    "Response": "True",
  },
   {
    "Title": "Pierwszy Polak na Marsie",

    "Released": "23 Jun 2017",
    "Runtime": "37 min",
    "Genre": "Documentary, Short, Drama",
    "Director": "Agnieszka Elbanowska",
    "Actors": "N/A",
    "Plot": "N/A",
    "Country": "Poland",
    "Awards": "1 win & 1 nomination.",
    "Poster":
      "https://m.media-amazon.com/images/M/MV5BYTRkOWY1MDktZWM5YS00OTM4LWIxYmUtZDUyMTJiZWQxOTAzXkEyXkFqcGdeQXVyMTEwMTY3NDI@._V1_SX300.jpg",
    "Response": "True",
  }]}
