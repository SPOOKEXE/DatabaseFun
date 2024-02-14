
from pydantic import BaseModel

class SessionInfo(BaseModel):
	userid : str
	username : str
	expiry : str
	token : str

class AccountInfo(BaseModel):
	userid : str
	username : str
	email : str
	password_hash : str
	creation_date : str
	terminated : int

class UserProfile(BaseModel):
	description : str
