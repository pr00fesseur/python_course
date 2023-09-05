filename = "names.txt"

with open(filename, mode="r") as file:
    lines = file.readlines()


class FileBase:
    def __init__(self, file: str) -> None:
        self.file: str = file

    def close(self):
        print(f"Closing file {self.file}")


class FileReader(FileBase):
    def readlines(self):
        print("Reading all lines from the file")

    def write(self):
        print("Readonly!!!")


class FileWriter(FileBase):
    def readlines(self):
        print("Only for writing")

    def write(self, data: str):
        print(f"Writing the {data}")


class open:
    def __init__(self, filename: str, mode: str) -> None:
        self._filename: str = filename
        self._mode: str = mode

    def __enter__(self):
        if self._mode == "r":
            self._file_mode_instance = FileReader(self._filename)
        elif self._mode == "w":
            self._file_mode_instance = FileWriter(self._filename)
        else:
            raise NotImplementedError

        return self._file_mode_instance

    def __exit__(self, *args, **kwargs):
        self._file_mode_instance.close()
