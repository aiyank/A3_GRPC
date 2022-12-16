import grpc
import InventoryProto_pb2
import InventoryProto_pb2_grpc
from concurrent import futures

books = {}


class InventoryServicer(InventoryProto_pb2_grpc.InventoryServiceServicer):
    def create_book(self, request, context):
        book = InventoryProto_pb2.Book()
        book.ISBN = request.ISBN
        book.title = request.title
        book.author = request.author
        book.genre = InventoryProto_pb2.Book.COMEDY
        book.publishing_year = request.publishing_year

        books[book.ISBN] = book

        return InventoryProto_pb2.CreateBookResponse(response="Book created successfully!")

    def get_book(self, request, context):
        book = books[request.ISBN]
        return InventoryProto_pb2.Book(ISBN=book.ISBN, title=book.title, author=book.author, genre=book.genre, publishing_year=book.publishing_year)


def main():
    add_sample_books()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    InventoryProto_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryServicer(), server)
    print("The server has successfully started!")
    server.add_insecure_port('[::]:1234')
    server.start()
    server.wait_for_termination()


def add_sample_books():
    print("Adding sample data to books!")
    book1 = InventoryProto_pb2.Book()
    book1.ISBN = "B1"
    book1.title = "Bugs Bunny"
    book1.author = "Billu Sanda"
    book1.genre = InventoryProto_pb2.Book.COMEDY
    book1.publishing_year = 2001

    book2 = InventoryProto_pb2.Book()
    book2.ISBN = "B2"
    book2.title = "Lola Bunny"
    book2.author = "Khalnayak"
    book2.genre = InventoryProto_pb2.Book.COMEDY
    book2.publishing_year = 2002

    book3 = InventoryProto_pb2.Book()
    book3.ISBN = "B3"
    book3.title = "Road Runner"
    book3.author = "Mohseen Khan"
    book3.genre = InventoryProto_pb2.Book.COMEDY
    book3.publishing_year = 2003

    book4 = InventoryProto_pb2.Book()
    book4.ISBN = "B4"
    book4.title = "Daffy Duck"
    book4.author = "Arpit Bhagat"
    book4.genre = InventoryProto_pb2.Book.COMEDY
    book4.publishing_year = 2004

    books[book1.ISBN] = book1
    books[book2.ISBN] = book2
    books[book3.ISBN] = book3
    books[book4.ISBN] = book4


main()
