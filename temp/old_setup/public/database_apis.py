
import httpx

class Databases:

	SESSIONS_DATABASE = '127.0.0.1:5010'
	TERMINATION_DATABASE = '127.0.0.1:5011'
	PROFILES_DATABASE = '127.0.0.1:5012'
	ACCOUNT_DATABASE = '127.0.0.1:5013'

class AsyncHttp:

	async def get( database : str, path : str, *args, **kwargs ) -> httpx.Response:
		url : str = f'http://{database}/{path}'
		return await httpx.get( url, *args, **kwargs )

	async def post( database : str, path : str, *args, **kwargs ) -> httpx.Response:
		url : str = f'http://{database}/{path}'
		return await httpx.post( url, *args, **kwargs )

class DatabaseAPI:

	class Session:

		async def info( token : str ) -> dict:
			response : httpx.Response = await AsyncHttp.get(Databases.SESSIONS_DATABASE, f'info/{token}')
			return response.json()

	class Account:

		async def register( username : str, email : str, password_hash : str, date_of_birth : str, gender : int ) -> dict:
			response : httpx.Response = await AsyncHttp.post(Databases.ACCOUNT_DATABASE, 'register', json={
				'username' : username,
				'email' : email,
				'password' : password_hash,
				'date_of_birth' : date_of_birth,
				'gender' : gender
			})
			return response.json()

		async def info( token : str ) -> dict:
			response : httpx.Response = await AsyncHttp.get(Databases.ACCOUNT_DATABASE, f'register/{token}')
			return response.json()

		async def login( username : str, password_hash : str ) -> dict:
			response : httpx.Response = await AsyncHttp.post(Databases.ACCOUNT_DATABASE, f'register', json={
				'username' : username,
				'password' : password_hash
			})
			return response.json()

		async def logout( token : str ) -> None:
			response : httpx.Response = await AsyncHttp.post(Databases.ACCOUNT_DATABASE, f'logout', json={
				'token' : token
			})
			return response.json()

	class Profile:

		async def profile( user_id : str ) -> None:
			response : httpx.Response = await AsyncHttp.get(Databases.PROFILES_DATABASE, f'profile/{user_id}')
			return response.json()

		async def description( description : str ) -> dict:
			response : httpx.Response = await AsyncHttp.get(Databases.PROFILES_DATABASE, f'profile/description')
			return response.json()

	class Termination:
		pass
