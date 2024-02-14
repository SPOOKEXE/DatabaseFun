
from pydantic import BaseModel

class RegisterAccountModel(BaseModel):
	'''Information sent to the server when creating a new account.'''
	username : str
	email : str
	password_hashed : str
	date_of_birth : str
	gender : str

class SessionData(BaseModel):
	'''Information the client sends the server to check if account session is still valid.'''
	token : str

class SessionServerInfo(BaseModel): # PRIMARY KEY = token
	'''Information stored on the server for all active sessions under an account. If NULL is sent, go to login page.'''
	user_id : str
	username : str
	login_date : str
	expiry_date : str
	token : str

class SessionClientInfo(BaseModel):
	'''Information sent back to client when session is CREATED.'''
	token : str
	login_date : str
	expiry_date : str
