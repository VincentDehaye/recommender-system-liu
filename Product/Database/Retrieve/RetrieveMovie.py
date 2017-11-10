from Product.Database.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Movie

'''
Author: John Andree Lidquist, Marten Bolin
Date: 9/11/2017
Last update: 10/11/2017
Purpose: Supposed to Retrieve data from movie table in database
'''


class RetrieveMovie(Retrieve):

    def retrieve_movie(self, movie_id=None):
        if movie_id:
            movie=self.session.query(Movie).filter_by(id=movie_id).first()
        else:
            movie=self.session.query(Movie).all()
        self.session.close()
        return movie
