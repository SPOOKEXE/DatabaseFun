
from pydantic import BaseModel

class SocialNetworkOptions(BaseModel):
	facebook : str
	twitter : str
	youtube : str
	twitch : str
	visibility : int

class CommunicationRestrictions(BaseModel):
	private_message : int # message button on profile [SocialLevels]
	chat_message : int # on website [TightestSocialLevels]
	ingame_message : int # in-game [ExtremeSocialLevels]

class AdditionalRestrictions(BaseModel):
	vip_server_invitations : int # give perms to join vip server [SocialLevels]
	join_me_in_games : int # join the user in the game they're playing [SocialLevels]
	view_inventory : int # view my inventory [SocialLevels]

class PlatformNotifications:
	events : int # NotificationLevel
	payout_received : int # NotificationLevel

class FriendAndGroupNotifications:
	friend_request_received : int # NotificationLevel
	friend_request_accepted : int # NotificationLevel
	chat_message : int # NotificationLevel
	private_message : int # NotificationLevel
	invited_to_game : int # NotificationLevel

class NotificationSettings(BaseModel):
	platform : PlatformNotifications
	social : FriendAndGroupNotifications

class PrivacySettings(BaseModel): # PRIMARY KEY = user_id
	'''Information stored on the server for a given account.'''
	restrictions_enabled : int
	communication_restrictions : CommunicationRestrictions
	additional_restrictions : AdditionalRestrictions

class MiscSettings(BaseModel):
	theme : str
	language : str
	world_region : str # oceania / northern america / southern american / europe / africa / asia

class AccountInfo(BaseModel): # PRIMARY KEY = user_id
	'''Information stored on the server for a given account.'''
	username : str
	alias : str
	email : str
	password_hash : str
	creation_date : str

	privacy_settings : PrivacySettings
	social_options : SocialNetworkOptions
	notification_settings : NotificationSettings
	misc_settings : MiscSettings

class AccountProfile(BaseModel): # PRIMARY KEY = user_id
	'''Information stored on the server for a given account. This is the PUBLIC PROFILE of the user that CAN BE EDITED via APIs.'''
	presence_status_enum : int # C
	presence_status_value : str # C
	description : str # D
	site_badges : list[str] # E

class FriendsList(BaseModel):
	user_ids : list[int]

class CatalogItem(BaseModel):
	id : int
	total_sold : int
	available_total : int = 0 # 0 = unlimited
	name : str
	price : int
	date : str

class InventoryItem(BaseModel):
	id : int
	serial_number : int # total_sold; total_sold += 1
	name : str
	price : int
	date : str

class UserInventory(BaseModel):
	items : list[InventoryItem]
