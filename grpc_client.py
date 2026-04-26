import grpc
import user_service_pb2

from user_service_pb2_grpc import UserServiceStub

channel = grpc.insecure_channel("localhost:50051")
stub = UserServiceStub(channel)

request = user_service_pb2.GetUserRequest(username="Alice")
response = stub.GetUser(request)
print(response.message)
