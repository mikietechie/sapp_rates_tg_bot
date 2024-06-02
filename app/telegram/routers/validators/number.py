# pylint: disable=too-few-public-methods
"""
Form fields validators.
"""
import re
from typing import Tuple, Any

from aiogram_forms.errors import ValidationError


class IntValidator:
    """Int validator."""
    def __call__(self, value: str) -> None:
        try:
            assert str(int(value)) == value
        except:
            raise ValidationError(f'Value should an number i.e integer.', code='is_int')
