import pathlib
import shutil

import pytest


@pytest.fixture(scope="class")
def _manage_dir():
    p = pathlib.Path("./.tmp")

    if p.exists():
        shutil.rmtree("./.tmp")

    p.mkdir()
    yield
    shutil.rmtree("./.tmp")
