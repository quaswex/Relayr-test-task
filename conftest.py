# -*- coding: utf-8 -*-

import pytest
from actions import Actions


@pytest.fixture
def action(request):
    fixture = Actions()
    request.addfinalizer(fixture.destroy)
    return fixture
