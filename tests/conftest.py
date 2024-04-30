import pytest
from selene import browser
from selene.support.shared import config


@pytest.fixture(autouse=True)
def browser():
    config.timeout = 10