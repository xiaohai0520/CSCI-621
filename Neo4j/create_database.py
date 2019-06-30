
from process_data import read_data
from neo4j import GraphDatabase
from py2neo import Graph,Node,Relationship

file = 'movie.csv'
username = 'neo4j'
password = 'neo4j'
address = 'bolt://localhost:7687'
uri = 'http://localhost:7474'
cols = ['movie_title', 'genres','title_year', 'imdb_score', 'budget','director_name','actor_1_name','actor_2_name']

actors = {}
directors = {}
genres = {}


def create_movie_node(row,movie_db):
    print(row.movie_title.strip())
    # create movie node   include name year score budget
    movie_node = Node('Movie', name=row.movie_title.strip(), year=row.title_year, score=row.imdb_score, budget=row.budget)

    # insert into graph
    movie_db.create(movie_node)

    return movie_node

def add_director(name,movie_db,movie_node):
    if name in directors:
        director_node = directors[name]
        #create relationship
    else:
        director_node = Node('Director',name=name)
        directors[name] = director_node
        movie_db.create(director_node)

    r1 = Relationship(movie_node,'directBy',director_node)
    r2 = Relationship(director_node,'direct',movie_node)

    movie_db.create(r1)
    movie_db.create(r2)

def add_actor(name,movie_db,movie_node):
    if name in actors:
        actor_node = actors[name]
        #create relationship
    else:
        actor_node = Node('Actor',name=name)
        actors[name] = actor_node
        movie_db.create(actor_node)

    r1 = Relationship(movie_node,'actBy',actor_node)
    r2 = Relationship(actor_node,'act',movie_node)

    movie_db.create(r1)
    movie_db.create(r2)

def add_genre(name,movie_db,movie_node):
    if name in genres:
        genre_node = genres[name]

    #create relationship
    else:
        genre_node = Node('Genre',genre=name)
        genres[name] = genre_node
        movie_db.create(genre_node)

    r1 = Relationship(movie_node,'gen',genre_node)
    r2 = Relationship(genre_node,'gen',movie_node)

    movie_db.create(r1)
    movie_db.create(r2)




def connectdb():
    # connect to database
    movie_db = Graph(uri, auth=(username, password))


    #return
    return movie_db

def create_database(movie_db,movie_data):

    for i, row in movie_data.iterrows():

        # movie
        movie_node = create_movie_node(row,movie_db)

        # director
        director_name = row.director_name
        add_director(director_name,movie_db,movie_node)

        # actor
        actor_name = row.actor_1_name
        add_actor(actor_name,movie_db,movie_node)
        actor_name = row.actor_2_name
        add_actor(actor_name,movie_db,movie_node)

        # genre
        cur_genres = row.genres.split('|')
        for genre in cur_genres:
            add_genre(genre,movie_db,movie_node)


def main():
    # read data
    print(1)
    movie_data = read_data(file, cols)

    #connect to db
    movie_db = connectdb()

    # delete previous data
    movie_db.delete_all()
    # create db
    create_database(movie_db,movie_data)

if __name__ == "__main__":
    main()





