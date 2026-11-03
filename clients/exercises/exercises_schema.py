from pydantic import BaseModel

class ExerciseSchema(BaseModel):
    """
    Описание структуры задания
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение заданий
    """
    courseId: str

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения заданий.
    """
    exercises: list[ExerciseSchema]

class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение задания
    """
    exercise_id: str

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения задания.
    """
    exercise: ExerciseSchema

class CreateExerciseSchema(BaseModel):
    """
    Описание структры запроса создания задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса обновления задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema