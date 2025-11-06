import pytest
from utils import define_csv_columns

@pytest.mark.parametrize("line, expected",[
    ("name,telephone,address",["name", "telephone", "address"]),
    ("first_name,last_name, age",["first_name","last_name","age"]),
    (" ,int,  email   ", ["UNDEFINED","int","email"]),
    ("",None)
])
def test_define_csv_columns(line, expected):
    output = define_csv_columns(line)
    assert output == expected