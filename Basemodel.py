from pydantic import BaseModel,constr

#creation if basemodel
class create_user(BaseModel):
    username:str
    password: constr(
        min_length=8,
        max_length=20
    )
