import json
from typing import List, Dict, Any


class CsvFileHandler:

    def __init__(self, filepath: str, delimiter: str = ';', encoding: str = 'windows-1251'):
        self.data = None
        self.filepath = filepath
        self.delimiter = delimiter
        self.encoding = encoding

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:

        with open(self.filepath, 'r', encoding=self.encoding) as file:
            self.data = file.readlines()
            if as_dict:
                return [dict(zip(self.data[0].split(self.delimiter), line.split(self.delimiter))) for line in
                        self.data[1:]]
            else:
                return [line.split(self.delimiter) for line in self.data]

    def write_file(self, data: List[Dict] | List[List], as_dict=False) -> None:

        with open(self.filepath, 'w', encoding=self.encoding) as file:
            if as_dict:
                file.writelines([self.delimiter.join(data[0].keys()) + '\n'])
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])

    def append_file(self, data: List[Dict] | List[List], as_dict=False) -> None:

        with open(self.filepath, 'a', encoding=self.encoding) as file:
            if as_dict:
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])


class JsonAppendError(Exception):
    pass


class JsonFileHandler:

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data: List[Dict] | List[List]) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data: Any) -> None:
        raise JsonAppendError('Данный тип файла не поддерживает операцию дописывания')


class TxtFileHandler:

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self) -> List[str]:
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = file.readlines()
            return self.data

    def write_file(self, data: List[str]) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def append_file(self, data: List[str]) -> None:
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.writelines(data)
