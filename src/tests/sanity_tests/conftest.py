import asyncio
import pytest
import json

import pytest_asyncio

def pytest_addoption(parser):
    parser.addoption("--datafile", action="store", help="Path to the JSON data file")

@pytest.fixture(scope='session')
def datafile(request):
    filename = request.config.getoption("--datafile")
    if not filename:
        pytest.fail('Datafile not specified. Use --datafile to specify the path to the data file.')
    with open(filename, 'r') as f:
        data = json.load(f)
    return data



@pytest_asyncio.fixture(scope='session')
def event_loop():  # https://pytest-asyncio.readthedocs.io/en/latest/reference/fixtures.html#fixtures
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()