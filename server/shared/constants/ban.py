
class BanType:
	WARNING = 0
	TEMPORARY = 1
	TERMINATION = 2

class AbusiveContentTags:
	ASSET = 0
	SOCIAL = 1
	ACCOUNT = 2

class AbusiveContentTypes:

	PROFANITY = (
		0, 'Profane language or slurs is not allowed.',
		[ AbusiveContentTags.SOCIAL ]
	)

	HARASSMENT = (
		1, 'Bullying or harassment towards community members is not allowed.',
		[ AbusiveContentTags.SOCIAL ]
	)

	DISCRIMINATORY = (
		2, 'Discriminatory content is not allowed on the site.',
		[ AbusiveContentTags.SOCIAL ]
	)

	SPAM = (
		3, 'Spamming, including clickbait, reptitive language and large volume messanging, are not allowed.',
		[ AbusiveContentTags.SOCIAL ]
	)

	ADVERTISEMENT = (
		4, 'Advertising with offsite links and content is not allowed.',
		[ AbusiveContentTags.SOCIAL ]
	)

	SCAMMING = (
		5, 'Scamming, phishing, requests for passwords, selling of accounts, selling others\' assets for real money, and/or artificially inflating games are not allowed.',
		[ AbusiveContentTags.SOCIAL ]
	)

	EXPLICIT_CONTENT = (
		6, 'Explicit content is not allowed on the site. Includes pornography, sexual references and inuendos of such.',
		[ AbusiveContentTags.SOCIAL, AbusiveContentTags.ASSET ]
	)

	DISTURBING_CONTENT = (
		7, 'Disturbing content is not allowed on the site. Includes gore, acts of amputation, acts of beheading and the such.',
		[ AbusiveContentTags.SOCIAL, AbusiveContentTags.ASSET ]
	)

	INAPPROPRIATE_CONTENT = (
		8, 'Inappropriate content is not allowed on the site.',
		[ AbusiveContentTags.SOCIAL, AbusiveContentTags.ASSET ]
	)

	DRUGS_AND_ALCOHOL = (
		9, 'Drug and alcohol content are not allowed on the site.',
		[ AbusiveContentTags.SOCIAL, AbusiveContentTags.ASSET ]
	)

	SELF_HARM = (
		10, 'Referencing suicide and self-harm is not allowed on the site.',
		[ AbusiveContentTags.SOCIAL ]
	)

	ACCOUNT_THEFT = (
		11, 'Account theft is not permitted on the site.',
		[ AbusiveContentTags.ACCOUNT ]
	)

	EXPLOITING = (
		12, 'Exploiting on the site is not permitted.',
		[ AbusiveContentTags.ACCOUNT, AbusiveContentTags.SOCIAL ]
	)

	REAL_LIFE_TRAGEDY = (
		13, 'The site does not permit content relating to real-life tragedies. This is for only direct references to such tragedies.',
		[ AbusiveContentTags.ASSET ]
	)

	EXTORTION_BLACKMAIL = (
		14, 'Extortion/Blackmail is not permitted on the site.',
		[ AbusiveContentTags.SOCIAL ]
	)

	TERRORISM_EXTREMISM = (
		15, 'Terrorism/Extremism is not permitted on the site.',
		[ AbusiveContentTags.SOCIAL ]
	)

	REAL_LIFE_THREATS = (
		16, 'Real-life threats are not permitted on the site.',
		[ AbusiveContentTags.SOCIAL ]
	)

	THIRD_PARTY_SELLING = (
		17, 'The site does not permit third-party selling.',
		[ AbusiveContentTags.SOCIAL, AbusiveContentTags.ACCOUNT ]
	)

	CHARGEBACK = (
		18, 'You have chargedback a purchase for your account resulting in a permanent ban.',
		[ AbusiveContentTags.ACCOUNT ]
	)
