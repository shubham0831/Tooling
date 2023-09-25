Config file (yaml)

# Description: Configuration file for workflow automator

# App you use for your meetings. Currently only supporting zoom, in the future will add support for 
# teams and google meet.
meeting_app: "zoom"

# App you use for your messaging. Currently only supporting slack, in the future will add support for
# teams, discord, notion, etc. 
# This is where we send you your meeting notes and action items.
messaging_app: "slack"
messaging_app_token: ""
messaging_app_channel: ""

# Which AI do you want us to use for generating meeting notes and action items.
ai_bot: "anthropic"
# AI bot version.
ai_bot_version: "v1"
# AI bot token.
ai_bot_token: ""

# Which workflow tool do you use for your action items. Currently only supporting jira, will be adding 
# support for notion and asana pretty soon.
workflow_tool: "jira"

jira_server : "",
jira_username : "",
jira_token : "",
