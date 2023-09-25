meeting_notes = '''hello'''
from slack_sdk import WebClient
import re
import json

# Slack API configuration
SLACK_TOKEN = ''  # Replace with your Slack bot token
SLACK_CHANNEL = '#slack-bot-test-channel'  # Replace with the channel name or ID where you want to send the message

client = WebClient(token=SLACK_TOKEN)

result = client.users_list()
members = result.data['members']
# # print(members[0])

# for m in members:
#     if m['name'] == 'gbaringer':
#         print(m)

split_notes = meeting_notes.split("\n\n")

# Initialize an empty list to store the dictionaries
ticket_dicts = []

# Define the keys to extract from each section
keys_to_extract = [
    'user',
    'jira_ticket_number',
    'ticket_description',
    'action_item',
    'previous_release_version',
    'suggested_release_version',
    'previous_story_points',
    'suggested_story_points',
    'reasoning'
]

# Loop through each ticket section and extract the values
for section in split_notes:
    ticket_dict = {}
    for key in keys_to_extract:
        # Use regular expressions to extract the values
        match = re.search(fr'{key}: (.+)', section)
        if match:
            ticket_dict[key] = match.group(1)
    # Add the extracted dictionary to the list
    ticket_dicts.append(ticket_dict)

for ticket in ticket_dicts:
    if 'suggested_story_points' in ticket and ticket['action_item'] != 'Nothing to do':
        username = ticket['user']
        str_representation = json.dumps(ticket)

        for m in members:
            if m['name'] == username:
                user_id = m['id']
                client.chat_postMessage(channel=user_id, text=str_representation)
