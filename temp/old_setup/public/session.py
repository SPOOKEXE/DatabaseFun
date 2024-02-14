
from typing import Any, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response

from shared.resources import PresetResponses, StatusCodes, catch_unknown, run_uvicorn_locally
from shared.structs import SessionInfo
from old_setup.public.database_apis import Databases, AsyncHttp

## STRUCTS ##
class ReducedSessionInfo(BaseModel):
	userid : str
	username : str
	expiry : str

class SessionResponse(BaseModel):
	success : bool
	data : Optional[ReducedSessionInfo]

## API ##
session_api : FastAPI = FastAPI()
session_api.get('/')(catch_unknown)

@session_api.get('/info/{token}', response_model=SessionResponse)
async def session_info( request : Request, response: Response, token : str ) -> dict[str, Any]:
	# session : SessionInfo | None = await SessionsDatabase.get_session_info( token )
	# if session == None:
	# 	response.status_code = StatusCodes.UNAUTHORIZED
	# 	return SessionResponse(success=False, data=None)
	# reduced : ReducedSessionInfo = ReducedSessionInfo(userid=session.userid, username=session.username, expiry=session.expiry)
	# return SessionResponse(success=True, data=reduced)
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

## MAIN ##
if __name__ == '__main__':
	run_uvicorn_locally(session_api)
