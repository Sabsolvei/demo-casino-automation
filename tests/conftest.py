import pytest

from utilities.file_utils import FileUtils


@pytest.fixture
def data_test(request, config_location):
    test_filename = request.cls.__name__.lower()
    return FileUtils.get_yaml_data(f"{config_location}/data_test/data_{test_filename}.yaml")

@pytest.fixture
def name_test(request):
    return request.node.name.split('[')[0]

@pytest.fixture
def dataset(name_test, data_test):
    return data_test[name_test]['data']

@pytest.fixture
def expected_result(name_test, data_test):
    return data_test[name_test]['expected_result']
