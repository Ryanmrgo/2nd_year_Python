
import abc 
from abc import ABC, abstractmethod

class Table(ABC):
    @abstractmethod
    def set_size(self, length, breadth):
        pass

    @abstractmethod
    def set_color(self, color):
        pass

    @abstractmethod
    def set_type(self, table_type):
        pass

class OfficeTable(Table):
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.color = ""
        self.table_type = ""

    def set_size(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def set_color(self, color):
        self.color = color

    def set_type(self, table_type):
        self.table_type = table_type

    def __str__(self):
        return f"Office Table - Size: {self.length}x{self.breadth}, Color: {self.color}, Type: {self.table_type}"

class TableContainer:
    def __init__(self):
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def __len__(self):
        return len(self.tables)

    def __contains__(self, item):
        return item in self.tables

    def __iter__(self):
        return iter(self.tables)

# Example usage
office_table1 = OfficeTable()
office_table1.set_size(120, 80)
office_table1.set_color("Brown")
office_table1.set_type("Wood")

office_table2 = OfficeTable()
office_table2.set_size(100, 60)
office_table2.set_color("Black")
office_table2.set_type("Steel")

container = TableContainer()
container.add_table(office_table1)
container.add_table(office_table2)

print("Number of tables in container:", len(container))

for table in container:
    print(table)