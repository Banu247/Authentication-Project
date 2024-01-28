from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from connectdb import Usermaster,get_db
from Basemodel import create_user
from password_encrypt_decrypt import encrypt_password,decrypt_password

app =FastAPI()


@app.get('/fetch-users')
async def fetch_users(db:Session = Depends(get_db)):
    """API to fetch all the users """
    users  = db.query(Usermaster.id,Usermaster.username,Usermaster.password).all()
    response_list =[]
    if users:
        for user in users:
            response_list.append({"id":user.id,"username":user.username,"password":user.password})
        return response_list
    else:
        return{"message":"No details found"}
    
@app.post("/user-creation")
async def user_creation(userdata:create_user,db:Session = Depends(get_db)):
    """API to create users"""
    encrypted_password = encrypt_password(userdata.password)
    user_details = Usermaster(username = userdata.username,password= encrypted_password)
    users =db.query(Usermaster.username).all()
    if not userdata.username or not userdata.password:
        raise HTTPException(status_code=404,detail="username or password connot be empty")
    elif users !=[]:
        for username in users:
            if username[0] == userdata.username:
                raise HTTPException(status_code=422,detail="Username already exists!")

    db.add(user_details)
    db.commit()
    db.refresh(user_details)

    return{"message":"User created successfully"}


@app.delete('/delete-user')
async def delete_data(user:str = Query(description="To delete all the users specify all or Specify a username to delete a specific user.") ,db: Session = Depends(get_db)):
    """API to delete the users"""
    if user =="all":
        db.query(Usermaster).delete()
    else:
        db.query(Usermaster).filter(Usermaster.username ==user).delete()

    db.commit()
    return{"message":"Details deleted successfully"}


@app.post('/login')
async def login(login:create_user,db: Session = Depends(get_db)):
    """API to login"""
    if not login.username or not login.password:
        raise HTTPException(status_code=404,detail="username or password connot be empty")
    else:
        retrive_user = db.query(Usermaster.password).filter(Usermaster.username == login.username).first()
        decrypted_password =decrypt_password(retrive_user.password)
        if  decrypted_password!= login.password:
            raise HTTPException(status_code=404,detail = "Password is inncorrect")
        else:
            return {"message":"logged in successfuly","status_code":200}


