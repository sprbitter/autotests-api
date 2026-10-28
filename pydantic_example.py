# from pydantic import BaseModel, Field
#
#
# class Address(BaseModel):
#     city: str
#     zip_code: str
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     is_active: bool = Field(alias="isActive")
#
# user_data = {
#     'id':1,
#     'name': 'Alice',
#     'email': 'alice@example.com',
#     'isActive': True
# }
#
#
# user = User(**user_data)
# print(user.model_dump())
#

# from pydantic import BaseModel, ConfigDict
# from pydantic.alias_generators import to_camel
#
# class CourseSchema(BaseModel):
#     model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
#
#     id: str
#     title: str
#     max_score: int
#     min_score: int
#     description: str
#     estimated_time: str
#
# course_data = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
#
# course_model = CourseSchema(**course_data)
# print(course_model.model_dump(by_alias=True))


