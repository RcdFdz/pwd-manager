import pytest
from json_manager import JSONManager

def test_delete_element():
	json = {'One': 1, 'Two': 2}
	sm = JSONManager(json)
	x = sm.delete_entry('Two')
	assert x == {'One':True}

def test_delete_last_element():
	json = {'One': 1}
	sm = JSONManager(json)
	x = sm.delete_entry('One')
	assert x == {}

def test_delete_element_does_not_exist():
	json = {'One': 1}
	sm = JSONManager(json)
	with pytest.raises(KeyError):
		x = sm.delete_entry('Two')

def test_delete_from_empty_json():
	json = {}
	sm = JSONManager(json)
	with pytest.raises(KeyError):
		x = sm.delete_entry('Two')

def test_modify_value():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	x = sm.modify_values('One', {'user': 'user3'})
	assert x == {'One': {'user':'user3','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}

def test_modify_values_does_not_exist():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	with pytest.raises(KeyError):
		x = sm.modify_values('One',{'aaaa':'user3','pass':'pass3'})

def test_modify_id():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	x = sm.modify_id('One','Three')
	assert x == {'Three': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}

def test_modify_id_does_not_exist():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	with pytest.raises(KeyError):
		x = sm.modify_id('Four','Three')

def test_add_value():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	x = sm.add('Three',{'user':'user3','pass':'pass3','url':'url3','other':'other3'})
	assert x == {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}, 'Three': {'user':'user3','pass':'pass3','url':'url3','other':'other3'}}

def test_add_value_exist():
	json = {'One': {'user':'user1','pass':'pass1','url':'url1','other':'other1'}, 'Two': {'user':'user2','pass':'pass2','url':'url2','other':'other2'}}
	sm = JSONManager(json)
	with pytest.raises(KeyError):
		x = sm.add('Two',{'user':'user3','pass':'pass3','url':'url3','other':'other3'})
