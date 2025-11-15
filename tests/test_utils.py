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
    
@pytest.mark.parametrize("length, expected",[
    (1,"?"),
    (10, "?,?,?,?,?,?,?,?,?,?"),
    (0,""),
    (-1,"")
])
def test_gen_query_placeholder(length, expected):
    output_str = gen_query_placeholder(length)
    assert output_str == expected
    
@pytest.mark.parametrize("columns, expected_string",[
    (["first_name","last_name","age"], "first_name,last_name,age"),
    (["name ", "address"], "name ,address"),
    (["name", "age", ""], "name,age,"),
    ([], ""),
])
def test_make_column_str(columns, expected_string):
    output = make_columns_str(columns)
    assert output == expected_string
    
@pytest.mark.parametrize("content, query_data",[
    (["Hello,World", "World"],
     
     [
         ("Hello", "World"), ("World",)
      ]
    ),
    
    (["Speudo, age, job", "Mob, 20, crying and complaining", "LIX,36,handle all the marasses"],
     [
         ("Speudo", " age", " job"),
         ("Mob", " 20", " crying and complaining"),
         ("LIX", "36", "handle all the marasses")
     ]
     ),
    ([""], [
        ("",)
    ])
])
def test_convert_to_query_data(content,query_data):
    output = convert_to_query_data(content)
    assert output == query_data