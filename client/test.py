import inventory_client


import sys
# Replace the path inside path.insert with absolute path of services directory
sys.path.insert(0, '/Users/aiyankapoor/IdeaProjects/API_Design/A3_GRPC/client')


client = inventory_client.Test()
result = client.run("B1")
assert result.ISBN == "B1" and result.title == "Bugs Bunny" and result.author == "Billu Sanda" and result.publishing_year == 2001
print("Test passed successfully!")
