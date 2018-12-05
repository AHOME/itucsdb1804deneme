from table_operations.baseClass import baseClass

class Comment(baseClass):
    def __init__(self):
        super()

    def add(self, comment):
        query = "INSERT INTO COMMENT (CUSTOMER_ID, BOOK_ID, COMMENT_TITLE, COMMENT_STATEMENT, ADDED_TIME, UPDATED_TIME, RATING) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        fill = (comment.customer_id, comment.book_id, comment.comment_title, comment.comment_statement, comment.added_time, comment.updated_time, comment.rating)

        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def update(self, comment_key, comment):
        query = "UPDATE COMMENT SET CUSTOMER_ID = %s, BOOK_ID = %s, COMMENT_TITLE = %s, COMMENT_STATEMENT = %s, ADDED_TIME = %s, UPDATED_TIME = %s, RATING = %s WHERE COMMENT_ID = %s"
        fill = (comment.customer_id, comment.book_id, comment.comment_title, comment.comment_statement, comment.added_time, comment.updated_time, comment.rating, comment_key)

        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def delete(self, comment_key):
        query = "DELETE FROM COMMENT WHERE COMMENT_ID = %s"
        fill = (comment_key)

        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            cursor.close()

    def get_row(self, comment_key):
        _comment = None

        query = "SELECT * FROM COMMENT WHERE COMMENT_ID = %s"
        fill = (comment_key)

        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(query, fill)
            comment = cursor.fetchone()
            if comment is not None:
                _comment = Comment(comment[1], comment[2], comment[3], comment[4], comment[5], comment[6], comment[7])

        return _comment

    def get_table(self):
        comments = []

        query = "SELECT * FROM COMMENT;"

        with dbapi2.connect(url) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            for comment in cursor:
                comment_ = Comment(comment[1], comment[2], comment[3], comment[4], comment[5], comment[6], comment[7])
                comments.append((comment[0], comment_))
            cursor.close()

        return comments
