
from typing import Any

# from shared.constants import
# from shared.utility import ()
from shared.structs import (
	PostBanData, PreBanData,
	RegisterAccountModel,
	SessionClientInfo, SessionData,
	AccountProfile
)

class ActionsAPI:
	'''API for doing any sort of action with the database.'''

	class Moderation:
		'''API for moderation actions.'''

		@staticmethod
		async def ban_user_id( user_id : str, ban_data : PreBanData ) -> None:
			raise NotImplementedError

		@staticmethod
		async def is_user_id_banned( user_id : str ) -> bool:
			raise NotImplementedError

		@staticmethod
		async def get_user_ban_info( user_id : str ) -> PostBanData | None:
			raise NotImplementedError

	class Account:
		'''API for account actions.'''

		@staticmethod
		async def register( register_data : RegisterAccountModel ) -> Any | None:
			raise NotImplementedError

		@staticmethod
		async def logout( token : str ) -> Any | None:
			raise NotImplementedError

	class Session:
		'''API for account session actions.'''

		@staticmethod
		async def get_session_info( session_data : SessionData ) -> SessionClientInfo | None:
			pass

		@staticmethod
		async def login( username : str, password_hashed : str ) -> SessionClientInfo | None:
			raise NotImplementedError

	class User:
		'''API for user actions.'''

		@staticmethod
		async def get_username_from_id( user_id : str ) -> str:
			raise NotImplementedError

		@staticmethod
		async def get_id_from_username( username : str ) -> str:
			raise NotImplementedError

		@staticmethod
		async def get_profile_from_id( user_id : str ) -> AccountProfile:
			raise NotImplementedError

		@staticmethod
		async def get_profile_from_username( username : str ) -> AccountProfile:
			raise NotImplementedError

class BaseDataStore:
	pass

class BansDataStore(BaseDataStore):
	pass

class InventoryDataStore(BaseDataStore):
	pass

class AccountsDataStore(BaseDataStore):
	pass

class ProfilesDataStore(BaseDataStore):
	pass

class SessionsDataStore(BaseDataStore):
	pass
