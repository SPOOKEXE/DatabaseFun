
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response

from shared.resources import PresetResponses, StatusCodes, catch_unknown, run_uvicorn_locally
from shared.structs import UserProfile
from old_setup.public.database_apis import Databases, AsyncHttp

## STRUCTS ##
class WriteUserProfile:
	description : str

class ProfileResponse(BaseModel):
	success : bool
	profile : UserProfile | None

## API ##
users_api : FastAPI = FastAPI()
users_api.get('/')(catch_unknown)

@users_api.get('/profile/{userid}', response_model=ProfileResponse)
async def profile( request : Request, response : Response, userid : str ) -> dict:
	# profile : UserProfile = await ProfilesDatabase.get_profile_from_userid( userid )
	# if profile == None:
	# 	response.status_code = StatusCodes.NOT_FOUND
	# 	return ProfileResponse(success=False, profile=None)
	# return ProfileResponse(success=True, profile=profile)
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

@users_api.post('/profile/description')
async def profile( request : Request, response : Response, userid : str ) -> dict:
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

@users_api.post('/profile/alias')
async def profile( request : Request, response : Response, userid : str ) -> dict:
	response.status_code = StatusCodes.NOT_IMPLEMENTED
	return PresetResponses.UNIMPLEMENTED_ROUTE

## MAIN ##
if __name__ == '__main__':
	run_uvicorn_locally(users_api)
