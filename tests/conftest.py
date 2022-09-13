import pytest

from utilities.file_utils import FileUtils


@pytest.fixture
def data_test(request):
    test_filename = request.config.args[0].split('::')[0].split('.')[0]
    return FileUtils.get_yaml_data(f"../data_test/data_{test_filename}.yaml")

@pytest.fixture
def name_test(request):
    return request.node.name.split('[')[0]

@pytest.fixture
def dataset(name_test, data_test):
    return data_test[name_test]['data']

@pytest.fixture
def expected_result(name_test, data_test):
    return data_test[name_test]['expected_result']
