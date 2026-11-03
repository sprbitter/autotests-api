from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Провверяет, соответствует ли JSON-объект (instance) заданой JSON-схеме (schema)

    :param instance: JSON-данные, которые нужн проверить.
    :param schema: Ожидаемая JSON-схема.
    :raises jsonschema.exeptions.ValidationError: Если instance не соттвествует schema.
    """

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
