import grpc
import course_service_pb2

from course_service_pb2_grpc import CourseServiceStub

channel = grpc.insecure_channel("localhost:50051")
stub = CourseServiceStub(channel)

request = course_service_pb2.GetCourseRequest(course_id = "api-course")
response = stub.GetCourse(request)
print(response)
