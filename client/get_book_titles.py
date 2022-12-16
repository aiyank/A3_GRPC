import inventory_client
import sys
# Replace the path inside path.insert with absolute path of services directory
sys.path.insert(0, '/Users/aiyankapoor/IdeaProjects/API_Design/A3_GRPC/client')


def test_client(client, isbn):
    return client.run(isbn)


def main():
    client = inventory_client.Test()
    list_ISBN = ["B1", "B2"]
    result = []

    for isbn in list_ISBN:
        result.append(test_client(client, isbn))


main()
