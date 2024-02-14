
import asyncio
import sys
import uvicorn

from fastapi import FastAPI
from uvicorn import Server, Config

from public import account, users, session
from shared import resources

URL_MAPPING : list[tuple[str, int, FastAPI]] = [
	( "127.0.0.1", 5000, account.account_api ),
	( "127.0.0.1", 5001, users.users_api ),
	( "127.0.0.1", 5002, session.session_api ),
]

async def host_fastapp( app : FastAPI, host : str, port : int ) -> None:
	await uvicorn.Server(uvicorn.Config(app, host=host, port=port, log_level='info')).serve()

async def start_apis():
	'''Start all the APIs asynchronously.'''
	await asyncio.wait(
		[
			host_fastapp(account.account_api, '127.0.0.1', 5000),
			host_fastapp(users.users_api, '127.0.0.1', 5001),
			host_fastapp(session.session_api, '127.0.0.1', 5002),
		],
		return_when=asyncio.ALL_COMPLETED,
	)

if __name__ == "__main__":
	try:
		asyncio.run(start_apis())
	except Exception as e:
		print(e)
		sys.exit(0)
