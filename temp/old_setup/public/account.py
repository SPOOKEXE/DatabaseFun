
from typing import Any, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response

from shared.resources import PresetResponses, StatusCodes, catch_unknown, run_uvicorn_locally
from shared.structs import SessionInfo
from old_setup.public.database_apis import Databases, AsyncHttp

## STRUCTS ##
class RegisterRequest(BaseModel):
	username : str
	email : str
	password_hash : str
	dateofbirth : str
	gender : int

class SessionResponse(BaseModel):
	success : bool
	data : Optional[SessionInfo]

## API ##
account_api : FastAPI = FastAPI()
account_api.get('/')(catch_unknown)

@account_api.post('/register/', response_model=SessionResponse)
async def register( request : Request, response: Response, info : RegisterRequest ) -> dict:
	print( info.model_dump_json() )
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

@account_api.post('/info/{token}')
async def info(request : Request, response: Response) -> dict:
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

@account_api.post('/login/')
async def login(request : Request, response: Response) -> dict:
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

@account_api.post('/logout/')
async def logout(request : Request, response: Response) -> dict:
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

## MAIN ##
if __name__ == '__main__':
	run_uvicorn_locally(account_api)
