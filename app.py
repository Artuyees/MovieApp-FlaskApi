
from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)

api = Api(app)

class HomePage(Resource):
    def get(self):
        return {"movies": [ {
          "Title": "Nightmare Alley",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
          
        },
        {
          "Title": "Spider-Man",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SX300.jpg",
          
        },
        {
          "Title": "Avatar",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
          
        },
        {
          "Title": "Titanic",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
          
        },
        {
          "Title": "Pierwszy Polak na Marsie",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BYTRkOWY1MDktZWM5YS00OTM4LWIxYmUtZDUyMTJiZWQxOTAzXkEyXkFqcGdeQXVyMTEwMTY3NDI@._V1_SX300.jpg",
          
        }]}

api.add_resource(HomePage, '/homepage')
class Popular(Resource):
    def get(self):
      return {"movies": [
        {
          "Title": "Mafia",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BNTA1MzA2MWQtMTFkYi00ZDFjLTgwNDgtNDU4ZmM4OTlkZGUwXkEyXkFqcGdeQXVyMTIwNzMxNTU2._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Top Gun",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BZjQxYTA3ODItNzgxMy00N2Y2LWJlZGMtMTRlM2JkZjI1ZDhhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Okay",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMjEwOTQ4NjUwNV5BMl5BanBnXkFtZTcwOTkzNDUyMQ@@._V1_SX300.jpg",
        
          
        },
        {
          "Title": "Filip",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BY2MzODIzMDctNWY4NS00ZWM0LWFiY2QtNzI1YjU0NzEzYWQxXkEyXkFqcGdeQXVyMjI3MDQ5NDY@._V1_SX300.jpg",
        
          
        },
        {
          "Title": "Home Alone",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMzFkM2YwOTQtYzk2Mi00N2VlLWE3NTItN2YwNDg1YmY0ZDNmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
        
        
          
        },
      ]}

api.add_resource(Popular, '/popular')

class New(Resource):
    def get(self):
      return {"movies": [
      {
        "Title": "Nightmare Alley",
        "Poster":
          "https://m.media-amazon.com/images/M/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
      
        
      },
      {
        "Title": "Mafia",
        "Poster":
          "https://m.media-amazon.com/images/M/MV5BNTA1MzA2MWQtMTFkYi00ZDFjLTgwNDgtNDU4ZmM4OTlkZGUwXkEyXkFqcGdeQXVyMTIwNzMxNTU2._V1_SX300.jpg",
        
      },
      {
        "Title": "Marry Me",
        "Poster":
          "https://m.media-amazon.com/images/M/MV5BMjczZjI2M2UtOGMwOS00YWFhLTg0OTYtZDY5ZWIwNjhlOWI2XkEyXkFqcGdeQXVyMTQzNTA5MzYz._V1_SX300.jpg",
        
        
      },
      {
        "Title": "Moonfall",
        "Poster":
          "https://m.media-amazon.com/images/M/MV5BZjk0OWZiN2ItNmQ2YS00NTJmLTg0MjItNzM4NzBkMWM1ZTRlXkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_SX300.jpg",
        
        
      },
      {
        "Title": "Blacklight",
        "Poster":
          "https://m.media-amazon.com/images/M/MV5BY2ViYmNhNzEtZDJhNS00YzM4LTkzZWItZDJiNzc5ZDExOWZmXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SX300.jpg",
        
        
      },
    ]}

api.add_resource(New, '/new')

class All(Resource):
    def get(self):
      return {"movies": [
        {
          "Title": "Nightmare Alley",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BOTI4NDhhNGEtZjQxZC00ZTRmLThmZTctOGJmY2ZlOTc0ZGY0XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Spider-Man",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BZDEyN2NhMjgtMjdhNi00MmNlLWE5YTgtZGE4MzNjMTRlMGEwXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Avatar",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
        
          
        },
        {
          "Title": "Titanic",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Pierwszy Polak na Marsie",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BYTRkOWY1MDktZWM5YS00OTM4LWIxYmUtZDUyMTJiZWQxOTAzXkEyXkFqcGdeQXVyMTEwMTY3NDI@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Mission: Impossible",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMTc3NjI2MjU0Nl5BMl5BanBnXkFtZTgwNDk3ODYxMTE@._V1_SX300.jpg",
        
          
        },
        {
          "Title": "The Godfather",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Toy Story",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Mafia",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BNTA1MzA2MWQtMTFkYi00ZDFjLTgwNDgtNDU4ZmM4OTlkZGUwXkEyXkFqcGdeQXVyMTIwNzMxNTU2._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Top Gun",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BZjQxYTA3ODItNzgxMy00N2Y2LWJlZGMtMTRlM2JkZjI1ZDhhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Okay",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMjEwOTQ4NjUwNV5BMl5BanBnXkFtZTcwOTkzNDUyMQ@@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Filip",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BY2MzODIzMDctNWY4NS00ZWM0LWFiY2QtNzI1YjU0NzEzYWQxXkEyXkFqcGdeQXVyMjI3MDQ5NDY@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Home Alone",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BMzFkM2YwOTQtYzk2Mi00N2VlLWE3NTItN2YwNDg1YmY0ZDNmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
          
          
        },
        {
          "Title": "Welcome",
          "Poster":
            "https://m.media-amazon.com/images/M/MV5BZjcyOTViMzUtOWQ5Yy00ZTVmLWJmYzctN2U2OGVlN2ZjNTA0XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg",
          
        },
      ]
      }

api.add_resource(All, '/all')

if __name__ == '__main__':
    app.run()
