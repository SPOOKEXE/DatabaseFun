
from pydantic import BaseModel

class BanContentEvidence(BaseModel):
	abuse_type : int
	content : str

class PreBanData(BaseModel):
	ban_type : int
	evidence : list[BanContentEvidence]
	expiration : str | None

class PostBanData(BaseModel): # PRIMARY KEY = user_id
	ban_type : int
	evidence : list[BanContentEvidence]
	expiration : str | None
	date : str
