from flask import current_app

class Control:
    class Input:
        @staticmethod
        def book(values):
            err_message = None
            # Invalid input control
            if len(values["explanation"]) >= 1000:
                err_message = "Explanation cannot be more than 1000 character"
            elif not values["released_year"].isdigit():
                err_message = "Released year must be digit"
            elif len(values["book_name"]) >= 100:
                err_message = "Book name cannot be more than 100 character"
            return err_message

        @staticmethod
        def book_edition(values, edition_number=None, book_id=None):
            err_message = None
            db = current_app.config["db"]       # AHMED EKLEDI
            # Invalid input control
            if not db.book.get_row(values['book_id']):  # AHMED EDITLEDI
                err_message = "There is not this book id"
            elif book_id and book_id != int(values['book_id']):
                err_message = "This is editing page. Book cannot be change"
            elif int(values['edition_number']) <= 0:
                err_message = "Edition number cannot be less than 1"
            elif not values['edition_number'].isdigit():
                err_message = "Edition number must be digit"
            elif not edition_number and Database().book_edition.get_row(values['book_id'], values['edition_number']):
                err_message = "There is this edition number"
            elif edition_number and edition_number != int(values['edition_number']):
                err_message = "This is editing page. Edition number cannot be change"
            elif len(values["isbn"]) >= 20:
                err_message = "ISBN cannot be more than 20 character"
            elif not values["isbn"].isdigit():
                err_message = "ISBN must be digit"
            elif len(values["publisher"]) >= 100:
                err_message = "Publisher cannot be more than 100 character"
            elif not values["publish_year"].isdigit():
                err_message = "Publish year must be digit"
            elif not values["number_of_pages"].isdigit():
                err_message = "Number of page must be digit"
            elif len(values["language"]) >= 50:
                err_message = "Language cannot be more than 50 character"

            return err_message
