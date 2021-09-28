import pytest
import os
from dotenv import load_dotenv
from os.path import dirname, abspath

from faker import Faker


ROOT_DIR = dirname(abspath(__file__))
load_dotenv()


@pytest.fixture(scope='session')
def env_run(request):
    if "URL_ENV" in os.environ:
        url = os.environ["URL_ENV"]
    else:
        url = str(os.getenv("URL_ENV"))
    return url

@pytest.fixture()
def faker_fixture():
    return Faker()
