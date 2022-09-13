import yaml


class FileUtils:

    @staticmethod
    def get_yaml_data(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            file = yaml.load(f, Loader=yaml.FullLoader)
        return file
