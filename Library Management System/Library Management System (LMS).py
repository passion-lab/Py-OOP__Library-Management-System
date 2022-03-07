# ! BE AWARE !
# Module section for Library Management System (LMS)
# Don't change anything if not known what is going to do.

class Library:
    # Instances
    library_instances = []

    # some pre-defined books in this Library for future use
    # library_catalog = {
    #     "Adventure": "Chander Pahar",
    #     "Comics": ["Batul The Great", "Handa Bhonda", "Gopal Bhar", "Nonte Phonte", "Chander Buri Magic Man",
    #                "Thakumar Jhuli"]
    # }

    # object constructor
    def __init__(self, library_name: str, list_of_books: list):
        """

        :param library_name: Library names
        :param list_of_books: Must have to be a list of book names
        """
        self.__class__.library_instances.append(library_name)  # adds each names to class instance list

        self.name = library_name
        self.catalog = list_of_books
        self.checks = {}  # stores records of books and lender username; deletes while return

        self.book_options = []  # stores books index to lend/return
        for time, val in enumerate(self.catalog):
            self.book_options.append(str(time + 1))  # adds each book index

    # add books
    def add_books(self, book_name):
        """

        :param book_name: Name(s) of book and use comma separated list within [] for multiple books
        :return: Adds book names to existing instance's catalog
        """
        if type(book_name) == tuple or type(book_name) == list:  # if books name are tuple or list
            for item in book_name:
                self.catalog.append(item)  # append to existing book catalog
        else:  # if name(s) is/are string
            self.catalog.append(book_name)  # append to existing book catalog
        return 'Your book(s) are successfully added to our library.\nThanks, for contributing us!\n'

    # list books
    def list_books(self, index: bool = False):
        """

        :param index: Take boolean value to show the index the books or not
        :return: List of all books in the library
        """
        print("\nList of all books in this library...")
        for time, items in enumerate(self.catalog):
            print(f" - {items}") if index is False else print(f" - [{time + 1}] {items}")  # shows index if true
        return "\n"

    # check-out/rent books
    def check_out(self, nth_book: int):
        """

        :param nth_book: Index of the book
        :return: Check out the indexed book for the user
        """
        if nth_book == 0:
            pass  # if user input 0, the check out process will be escaped and return to the main menu
        else:
            nth_book = nth_book - 1  # to access actual list index from user input
            search_book = str(self.catalog[nth_book])  # preparing for search string
            # search for existing lending
            if str(self.checks).find(search_book) != -1:
                self.book_options.remove("0")  # remove no longer using entry
                print(f'\nSORRY, Your requested book "{search_book}" is unavailable in the library right now!')
                print(f'It is now belonging to the user named {self.checks[search_book]} for a week. Please try after '
                      f'few days or for another book.\nSorry for the inconvenience!\n')
            else:
                print("\n")
                user_name = input(f'To lend the book, enter your full name: ').strip()  # user input for name to lend
                if user_name:
                    self.book_options.remove("0")  # remove no longer using entry
                    print(f'Processing for checking out "{self.catalog[nth_book]}"...')
                    self.checks.update({self.catalog[nth_book]: user_name})  # update checked out book dict
                    print(f"Thank you, {user_name}! Your requested book has checked out successfully.\n")
                else:
                    print("Without your identity, checking out is not possible. Please enter your name once again "
                          "to proceed!")
                    self.check_out(nth_book + 1)  # return to the method again if no user name input detected

    # check-in/return books
    def check_in(self, nth_book: int):
        """

        :param nth_book: Index of the book
        :return: Check in the indexed book for the user
        """
        self.book_options.remove("0")  # remove no longer using entry
        if nth_book == 0:
            pass  # if user input 0, the check out process will be escaped and return to the main menu
        else:
            nth_book = nth_book - 1  # to access actual list index from user input
            search_book = str(self.catalog[nth_book])  # preparing for search string
            # search for existing lending
            if str(self.checks).find(search_book) == -1:
                print(f'\nSORRY, Your requested book "{search_book}" is not issued yet!')
                print("You may had a typing error. Go back and try again if you do.\n")
            else:
                print("\nProcessing your request for returning...")
                del self.checks[search_book]  # delete checked out entry while return
                print(f'Your book "{search_book}" has checked in successfully!\n')


if __name__ == "__main__":

    # variables ------------------------
    story = ["Batul The Great", "Handa Bhonda", "Gopal Bhar", "Nonte Phonte", "Chander Buri Magic Man",
             "Thakumar Jhuli"]
    story_lib = Library("Story", story)

    want_quit = False

    # functions -------------------------
    def user_response(message: str, check_list: list):
        user_input = input(message).strip()
        if user_input in check_list:
            return user_input
        else:
            print("SORRY! You entered a wrong input. Try again with a right one.\n")
            user_response(message, check_list)

    # main program --------------------------
    # welcome title
    title = "Mini Project 1 - Library Management System (LMS)"
    subtitle = "[Note: User can see, borrow, return and add books here]"
    underline = int(len(subtitle)) * "-"
    print("\n{}\n{}\n{}\n".format(title, underline, subtitle))

    print("WELCOME TO VIRTUAL LIBRARY")

    while True:
        if want_quit:
            break
        else:
            # have to keep under a function
            print("\nOptions:\n  [1] List of all books in the library.\n  [2] Check-out book(s).\n  [3] Check-in"
                  " book(s).\n  [4] Add book(s) to library.\n\n  [0] Exit.\n")

            user_chose = user_response("Choose an option to continue: ", ["1", "2", "3", "4", "0"])
            if user_chose == "0":
                want_quit = True
            elif user_chose == "1":
                print(story_lib.list_books())
            elif user_chose == "2":
                print(story_lib.list_books(index=True))
                print("WARNING! You have to return in the same day on the next week after you rent the book.")
                story_lib.book_options.append("0")
                story_lib.check_out(
                    int(user_response("Select a book by corresponding number for checking out (or, [0] to Escape): ",
                                      story_lib.book_options)))
            elif user_chose == "3":
                print(story_lib.list_books(index=True))
                story_lib.book_options.append("0")
                story_lib.check_in(
                    int(user_response("Which book do you want to check in (or, [0] to Escape): ",
                                      story_lib.book_options)))
            else:
                story_lib.add_books(input("Type the name of book or use a list separated by comma for multiple books "
                                          "to add to this library: ").strip())

    print("Thanks for using our library! Come again to give your knowledge and wisdom a deeper dive.")
    quit()
