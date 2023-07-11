# test_my_class.py
import pytest
from .my_class import MyClass

@pytest.fixture
def my_class(event_loop):
    return MyClass()


@pytest.mark.asyncio
async def test_hello(my_class):
    assert await my_class.hello() == "Hello, World!"
