# Lollipop discord bot

## Usage
```
COMMANDS
--------
$help                     : Display this menu
$img  <content>           : Return requested image
$random                   : Return random facts
$chat <query>             : Return chatting response, tagging the user
$news <query> <content part> <language>
$exit                     : Command only allowed by admins
```

## SETTING API KEYS
Lollipop is using APIs in order to work properly. The following are the APIs that are being used, add it to your code.

### Discord Token
You can get a discord API by sign in [here](https://discord.com/developers/). <br>
Once you get the API, please add it to the line 10 of the [main script](https://github.com/ianchu0317/Lollipop-DiscordPy/blob/main/Lollipop.py): <br>
![image](https://user-images.githubusercontent.com/71509578/157579502-411fee37-f814-4153-898c-19cb4837f265.png)

### Chatting API 
Get API [here](https://brainshop.ai/). <br>
Add to line 9 of the [chatting script](https://github.com/ianchu0317/Lollipop-DiscordPy/blob/main/src/Chat/Chatbot.py): <br>
![image](https://user-images.githubusercontent.com/71509578/157580314-47b452e6-e47f-4cf1-bf31-e369ee19b3cd.png)

### Pexels API 
Get API [here](https://www.pexels.com/api/documentation/). <br>
Add to line 6 of [get image script](https://github.com/ianchu0317/Lollipop-DiscordPy/blob/main/src/Images/Image.py): <br>
![image](https://user-images.githubusercontent.com/71509578/157580477-55c46ed6-27ac-43da-b8bf-002f21c53435.png)

### Newsapi API KEY
Get API [here](https://newsapi.org/). <br>
Add to line 5 of [get news script](): <br>
![image](https://user-images.githubusercontent.com/71509578/157580796-16610dba-cee1-489c-99bd-444be27da31d.png)


## Usage Examples
- Chatting and Image Example ($chat, $img): <br>
![image](https://user-images.githubusercontent.com/71509578/157580946-3df6b088-87c8-41f8-8b7f-710e4c397587.png) <br>

- Get News Example ($news): <br>
![image](https://user-images.githubusercontent.com/71509578/157581175-52eb3ef9-970a-401a-855d-836b2d1d65f0.png)

- Get Random Facts Example (%random): <br>
![image](https://user-images.githubusercontent.com/71509578/157581286-a562b039-f229-4995-9c56-0547452840c5.png)
