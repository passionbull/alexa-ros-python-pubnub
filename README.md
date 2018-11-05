# alexa-ros-python-pubnub
Connect amazon alexa vocie and ROS using alexa skill, lambda, pubnub


# I wrote detail description for setup.
https://passionbull.net/2018/11/robot/connect-amazon-alexa-and-ros-using-alexa-skill-lambda-pubnub/
https://passionbull.net/2018/11/robot/connect-amazon-alexa-vocie-and-ros-using-alexa-skill-lambda-pubnub-2/

# setup

- Amazon alexa skill
    - create alexa skill and connect lambda
    - copy alexa_skill/Interaction Model.json to amazon-console
    - https://developer.amazon.com/alexa/console/ask?
- Lambda setup
    - create lambda function and connect alexa skill
    - copy lambda to amazon aws console
    - https://ap-northeast-1.console.aws.amazon.com/console/home?region=ap-northeast-1#
- Pubnub
    - create pubnub project and copy publish/subscribe key
    - set key to files
    - https://admin.pubnub.com
    

# execute

- git clone https://github.com/passionbull/alexa-ros-python-pubnub
- cd path_git
- python ros_pubnub_sample.py

# need to check
- setup alexa-skill, pubnub, lambda
- check subscribe_key, publish_key,channels
- check message key (messageResult.message.get('action'))
