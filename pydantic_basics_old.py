"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string",
  }
}
"""
import uuid

from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title:str = "Playwright"
    max_score:int = Field(alias="maxScore", default=1000)
    min_score:int = Field(alias="minScore", default=100)
    description:str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time:str = Field(alias="estimatedTime", default="2 week")
    created_by_user: UserSchema = Field(alias="createdByUser")

try:
    course_default_model= CourseSchema(
        id="course-id",
        title="Playwright",
        maxScore=100,
        minScore=10,
        description="Playwright course",
        previewFile=FileSchema(
            id="file-id",
            url="http://localhost:8000",
            filename="file.png",
            directory="courses",
        ),
        estimatedTime="1 week",
        createdByUser=UserSchema(
            id="user-id",
            email="user@gmail.com",
            lastName="Bond",
            firstName="Zara",
            middleName="Alise"
        )
    )
except ValidationError as error:
    print(error)
    print(error.errors())

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print(course_dict_model.model_dump())
print(course_dict_model.model_dump(by_alias=True))

print("Course default model:", course_default_model)

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)

