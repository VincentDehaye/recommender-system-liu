from Product.Database.DBConn import create_session


class Insert:
    def __init__(self):
        self.session = create_session()

