import grpc
import InventoryProto_pb2
import InventoryProto_pb2_grpc

def run():
  with grpc.insecure_channel('') as channel:
    stub = InventoryProto_pb2_grpc.InventoryServiceStub(channel)
    response = stub.CreateBook(InventoryProto_pb2)