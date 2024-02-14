
from __future__ import annotations

import asyncio
import sqlite3
import regex
import os

from typing import Any
from enum import Enum
from databases import Database
from _models_ import AccountInfo, SessionInfo, UserProfile

NUMBERS_LETTERS_PATTERN = r'^[a-zA-Z0-9_]*$'
NUMBERS_ONLY_PATTERN = r'^[0-9]*$'
EMAIL_ADDRESS_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

DEFAULT_USER_PROFILE : UserProfile = UserProfile(description='Go to your settings to change your profile.')

os.makedirs('databases', exist_ok=True)

class SanityLambdas(Enum):
	NUMBERS : lambda value : value if regex.fullmatch(NUMBERS_ONLY_PATTERN, value) != None else None
	EMAIL_ADDRESS : lambda value : value if regex.fullmatch(EMAIL_ADDRESS_PATTERN, value) != None else None
	NUMBERS_LETTERS : lambda value : value if regex.fullmatch(NUMBERS_LETTERS_PATTERN, value) != None else None

class BaseDatabase(Database):

	CONSTRUCTOR : str = None
	_connection : sqlite3.Connection
	_cursor : sqlite3.Cursor

	async def initialize( self ) -> None:
		connection : sqlite3.Connection = await self.connect()
		self._connection = connection
		cursor : sqlite3.Cursor = connection.cursor()
		self._cursor = cursor
		await cursor.execute(self.CONSTRUCTOR)

	def __init__( self, filename : str, *args, **kwargs ) -> BaseDatabase:
		super().__init__( "sqlite+aiosqlite:///" + filename, *args, **kwargs)
		print(f'Initializing SQLITE Database: {filename}')
		asyncio.run( self.initialize() )

class TerminationsDatabase(BaseDatabase):

	CONSTRUCTOR = 'CREATE TABLE IF NOT EXISTS master (id INTEGER PRIMARY KEY, reason VARCHAR(1000))'
	connection : sqlite3.Connection

	async def initialize( self ) -> None:
		self.connection : sqlite3.Connection = await self.connect()
		cursor = self.connection.cursor()
		await cursor.execute(self.CONSTRUCTOR)

class SessionsDatabase(BaseDatabase):

	async def get_session_info( self, token : str ) -> SessionInfo | None:
		'''
		Get the session information given the session token. Used for account sessions.
		'''
		result = await SESSIONS_DATABASE.fetch_one(f'SELECT * FROM master WHERE token={token}')
		if result == None: return None
		return SessionInfo(**result)

	# async def create_new_session( userid : str ) -> SessionInfo | None:
	# 	pass

	async def initialize( self ) -> None:
		await self.connect()
		query = "CREATE TABLE IF NOT EXISTS master (id INTEGER PRIMARY KEY, username VARCHAR(16), expiry VARCHAR(24), token VARCHAR(1526))"
		await self.execute(query=query)

class ProfilesDatabase(BaseDatabase):

	async def get_username_from_userid( self, user_id : str ) -> str | None:
		return await PROFILES_DATABASE.fetch_one(f'SELECT username FROM master WHERE id={user_id}')

	async def get_profile_from_userid( self, user_id : str ) -> UserProfile | None:
		'''
		Get the account's public profile. This is for the public to see.
		'''
		result = await PROFILES_DATABASE.fetch_one(f'SELECT * FROM master WHERE id={user_id}')
		if result == None: return None
		return UserProfile(**result)

	async def set_profile_for_user_id( self, user_id : str, profile : UserProfile ) -> None:
		# await PROFILES_DATABASE.execute(f'REPLACE INTO master(id, description) VALUES ({user_id}, {profile.description}) WHERE id={user_id}')
		old_profile : UserProfile | None = await PROFILES_DATABASE.fetch_one(f'SELECT (id) FROM master WHERE id={user_id}')
		if old_profile == None:
			query : str = 'INSERT INTO master(description) VALUES (:description)'
			await PROFILES_DATABASE.execute(query, profile)
		else:
			await PROFILES_DATABASE.execute(f'UPDATE master SET description = {profile.description} WHERE id = {user_id};')

	async def initialize( self ) -> None:
		await self.connect()
		query = "CREATE TABLE IF NOT EXISTS master (id INTEGER PRIMARY KEY, description VARCHAR(1000))"
		await self.execute(query=query)

class AccountsDatabase(BaseDatabase):

	async def get_account_info( self, user_id : str ) -> AccountInfo | None:
		'''
		Get the account's information. This is for the account's owner to see.
		'''
		result = await SESSIONS_DATABASE.fetch_one(f'SELECT * FROM master WHERE id={user_id}')
		if result == None: return None
		return AccountInfo(**result)

	async def get_id_from_username( self, username : str ) -> str | None:
		try:
			user_id : str = await self.fetch_one('SELECT id FROM master WHERE username=?', (username,))
			return user_id
		except:
			return None

	async def create_account( self, username : str, email : str, password_hash : str ) -> str:
		command : str = 'INSERT INTO master(username, email, password_hash, creation_date, terminated) VALUES (:username, :email, :password_hash, :creation_date, :terminated)'
		data : dict = {
			"username" : username,
			"email" : email,
			"password_hash" : password_hash,
			"creation_date" : "0000000",
			"terminated" : "0"
		}
		await self.execute( command, data )
		user_id : str = await self.get_id_from_username(username)
		print(user_id)
		await PROFILES_DATABASE.set_profile_for_user_id(user_id, DEFAULT_USER_PROFILE)

	async def initialize( self ) -> None:
		await self.connect()
		query = "CREATE TABLE IF NOT EXISTS master (id INTEGER PRIMARY KEY, username VARCHAR(16), email VARCHAR(64), password_hash VARCHAR(128), creation_date VARCHAR(24), terminated INTEGER)"
		await self.execute(query=query)

SESSIONS_DATABASE = SessionsDatabase('databases\\sessions.db')
TERMINATION_DATABASE = TerminationsDatabase('databases\\terminations.db')
PROFILES_DATABASE = ProfilesDatabase('databases\\profiles.db')
ACCOUNT_DATABASE = AccountsDatabase('databases\\accounts.db')

async def debug_run() -> None:
	user_id : str = await ACCOUNT_DATABASE.get_id_from_username('spook')
	print(user_id == None and 'Account does not exist.' or 'Account exists.')
	if user_id == None:
		user_id = await ACCOUNT_DATABASE.create_account('spook', 'a@gmail.com', 'BLURRED')
	print( user_id )
	# profile : UserProfile = await PROFILES_DATABASE.get_profile_from_userid( user_id )
	# print( profile )

asyncio.run( debug_run() )
