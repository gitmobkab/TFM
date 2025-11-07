import pytest
from utils import * # I know a shortcut bro, trust.

@pytest.mark.parametrize("line, expected",[
    ("name,telephone,address",["name", "telephone", "address"]),
    ("first_name,last_name, age",["first_name","last_name","age"]),
    (" ,int,  email   ", ["UNDEFINED","int","email"]),
    ("",None)
])
def test_define_csv_columns(line, expected):
    output = define_csv_columns(line)
    assert output == expected
    
@pytest.mark.parametrize("file_path, expected_ext",[
    ("/home/mob/TFM/students.csv",".csv"),
    ("C://Users//richm//Desktop/Employe.xls", ".xls"),
    ("~/.config/btop",""),
    ("","")
])
def test_get_file_ext(file_path, expected_ext):
    output = get_file_ext(file_path)
    assert output == expected_ext