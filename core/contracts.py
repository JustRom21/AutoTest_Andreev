USER_DATA_SCHEMA = {
    "type":"object",
    "properties":{
        'id': {'type':'number'},
        'email':{'type':'string'},
        'first_name':{'type':'string'},
        'last_name':{'type':'string'},
        'avatar':{'type':'string'},

    },
    "required": ["id","email","first_name","last_name","avatar"]
}

RESOURCE_DATA_SCHEMA = {
    "type":"object",
    "properties":{
        'id': {'type':'number'},
        'name':{'type':'string'},
        'year':{'type':'number'},
        'color':{'type':'string'},
        'pantone_value':{'type':'string'},

    },
    "required": ["id","name","year","color","pantone_value"]
}

USER_CREATE_DATA_SCHEMA = {
    "type":"object",
    "properties":{
        'id': {'type':'string'}, #не совсем понятно, почему автотест считает параметр id строкой а не числом
        'name':{'type':'string'},
        'job':{'type':'string'},
        },
    "required": ["id","name","job"]
}

REGISTER_CREATE_DATA_SCHEMA = {
    "type":"object",
    "properties":{
        'id': {'type':'number'},
        'token':{'type':'string'}
        },
    "required": ["id","token"]
}