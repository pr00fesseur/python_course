from functools import wraps


class Printer:
    def __init__(self, name: str, ip: str, port: int) -> None:
        self.name: str = name
        self.ip: str = ip
        self.port: int = port

    def __str__(self) -> str:
        return f"{self.name}@{self.ip}:{self.port}"


def open_connection(printer: Printer):
    print("Connection with Driver...")
    print(f"Connection with {printer}...")


def print_with_printer(printer: Printer, text: str):
    print(f"Printing with {printer}")
    print(f"'{text}'")


def close_connection(printer: Printer):
    print(f"Closing connection for {printer}...")


def connect(printer: Printer):
    def wrapper(func):
        @wraps(func)
        def inner(document: str):
            open_connection(printer)
            func(document)
            close_connection(printer)

        return inner

    return wrapper


# instance = connect(print_document)
# instance(printer, document)

hp_black = Printer(name="HP Black", ip="10.10.10.2", port=33145)
hp_white = Printer(name="HP White", ip="10.10.10.15", port=33145)

# print_document(hp_black, "Test one")

# open_connection(hp_black)
# print_with_printer(hp_black, "Test printing")
# close_connection(hp_black)


@connect(printer=hp_black)
def print_document(document: str):
    print(f"document: {document}")


print_document("John is on printer")
