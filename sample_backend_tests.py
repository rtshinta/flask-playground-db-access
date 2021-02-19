import pytest
import app 

def test_find_users_by_name_success():  
    expected = [
        {
            'id' : 'abc123',            
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',            
            'name': 'Mac',
            'job': 'Professor',
        },        
    ]
    assert app.find_users_by_name("Mac") == expected

def test_find_users_by_name_fail():  
    expected = [] 
    assert app.find_users_by_name("Jeff") == expected
