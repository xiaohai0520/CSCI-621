
from create_database import *

def test():
    db = connectdb()

    # Drama movies directed by Steven Spielberg.

    cypher = "MATCH (m:Movie) -[:directBy]- (d:Director)\n"\
            "WHERE d.name = 'Steven Spielberg'\n"\
            "WITH m\n"\
            "MATCH (m:Movie) -[:gen] -(g:Genre)\n"\
            "WHERE g.genre = 'Drama'\n"\
            "RETURN m.name\n"


    find = db.run(cypher)

    for i in find:
        print(i)

test()
