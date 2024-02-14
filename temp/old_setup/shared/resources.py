
from httpx._status_codes import codes as StatusCodes
from fastapi import FastAPI, Request, Response

class PresetResponses:
	UNAVAILABLE_ROUTE : dict = {'message' : 'Route does not exist.'}
	UNIMPLEMENTED_ROUTE : dict = {'message' : 'Route is not implemented.'}

async def catch_unknown( request : Request, response : Response ) -> dict:
	response.status_code = StatusCodes.NOT_FOUND
	return PresetResponses.UNAVAILABLE_ROUTE

def run_uvicorn_locally( app : FastAPI, host : str = '127.0.0.1', port : int = 8000 ) -> None:
	import uvicorn
	uvicorn.run(app, host=host, port=port)

def run_uvicorn_commandline( app : FastAPI ) -> None:
	import argparse

	parser = argparse.ArgumentParser(prog='Public API', description='Public API for the fun testing database.')
	parser.add_argument('-ar', '--addroute', type=str, nargs=2)
	parser.add_argument('-h', '--host', type=str, required=True)
	parser.add_argument('-p', '--port', type=int, required=True)

	args = parser.parse_args()
	print(args.__dict__)

	run_uvicorn_locally( app, host='127.0.0.1', port=8000 )
