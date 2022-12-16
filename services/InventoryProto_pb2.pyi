from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishing_year", "title"]
    class genre_enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    COMEDY: Book.genre_enum
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HORROR: Book.genre_enum
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    MYSTERY: Book.genre_enum
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    THRILLER: Book.genre_enum
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.genre_enum
    publishing_year: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.genre_enum, str]] = ..., publishing_year: _Optional[int] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class ISBN(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["ISBN", "inventory_number", "title"]
    class status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.status
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.status
    TITLE_FIELD_NUMBER: _ClassVar[int]
    inventory_number: str
    title: str
    def __init__(self, inventory_number: _Optional[str] = ..., title: _Optional[str] = ..., ISBN: _Optional[str] = ...) -> None: ...
