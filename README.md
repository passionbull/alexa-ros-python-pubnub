# alexa-ros-python-pubnub
Connect amazon alexa vocie and ROS using alexa skill, lambda, pubnub


# I wrote detail description for setup.
https://passionbull.net/2018/11/robot/connect-amazon-alexa-and-ros-using-alexa-skill-lambda-pubnub/
https://passionbull.net/2018/11/robot/connect-amazon-alexa-vocie-and-ros-using-alexa-skill-lambda-pubnub-2/

# execute

- git clone https://github.com/passionbull/alexa-ros-python-pubnub
- cd path_git
- python ros_pubnub_sample.py

# need to check
- setup alexa-skill, pubnub, lambda
- check subscribe_key, publish_key,channels
- check message key (messageResult.message.get('action'))
