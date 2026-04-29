from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password='str',
    last_name='str',
    first_name='str',
    middle_name='str'
)

create_user_response = public_users_client.create_user(create_user_request)

auth_data = AuthenticationUserSchema(email=create_user_request['email'], password=create_user_request['password'])
files_client = get_files_client(auth_data)
course_client = get_courses_client(auth_data)
exercise_client = get_exercises_client(auth_data)

create_file_request = CreateFileRequestSchema(
    filename='cat.jpg',
    directory='files',
    upload_file='./testdata/files/cat.jpg')

create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

create_course_request = CreateCourseRequestDict(
    title="Math",
    maxcore=100,
    minScore=10,
    description="Math course",
    estimatedTime='1 month',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print(f'Create course data: {create_course_response}')

create_exercise_request = CreateExerciseRequestDict(
    title="abs",
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=10,
    orderIndex=12121,
    description="some descr",
    estimatedTime="1 month"
)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print(f"Create exercise data: {create_exercise_response}")
