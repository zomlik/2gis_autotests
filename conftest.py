import pytest
from api.get_regions import GetRegions


@pytest.fixture(scope="function")
def regions() -> GetRegions:
    return GetRegions()
