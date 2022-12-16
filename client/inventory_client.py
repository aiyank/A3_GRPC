
import grpc

import sys
# Replace the path inside path.insert with absolute path of services directory
sys.path.insert(
    0, '/Users/aiyankapoor/IdeaProjects/API_Design/A3_GRPC/services')

import InventoryProto_pb2_grpc
import InventoryProto_pb2


class Test:
    def run(self, ISBN):
        with grpc.insecure_channel('0.0.0.0:1234') as ch:
            stub = InventoryProto_pb2_grpc.InventoryServiceStub(ch)
            response = stub.get_book(
                InventoryProto_pb2.CreateBookResponse(response=ISBN))
            print(response)
            return response
