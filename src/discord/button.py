from requests import post

def interact_button(channel_id, token, custom_id, latest_message, session_id):
	data = {
		"application_id": 270904126974590976,
		"channel_id": channel_id,
		"type": 3,
		"data": {
			"component_type": 2,
			"custom_id": custom_id
		},
		"guild_id": latest_message["message_reference"]["guild_id"],
		"message_flags": 0,
		"message_id": latest_message["id"],
		"session_id": session_id
	}

	request = post("https://discord.com/api/v10/interactions", headers={"authorization": token}, json=data)

	if request.status_code in [200, 204]:
		return True
	else:
		return False