import pytest

from utilities.file_utils import FileUtils


@pytest.fixture
def test_data():
    return FileUtils.get_yaml_data('../data_test/data_signup.yaml')


@pytest.fixture
def dataset(request, test_data):
    test_name = request.node.name.split('[')[0]
    return test_data[test_name]
