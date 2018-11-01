from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-xx"
pnconfig.publish_key = "pub-c-xx"
pnconfig.ssl = True
 
pubnub = PubNub(pnconfig)
presenceResult = None
messageResult = None

class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass
        # The status object returned is always related to subscribe but could contain
        # information about subscribe, heartbeat, or errors
        # use the operationType to switch on different options
        if status.operation == PNOperationType.PNSubscribeOperation \
                or status.operation == PNOperationType.PNUnsubscribeOperation:
            if status.category == PNStatusCategory.PNConnectedCategory:
                pass
                # This is expected for a subscribe, this means there is no error or issue whatsoever
            elif status.category == PNStatusCategory.PNReconnectedCategory:
                pass
                # This usually occurs if subscribe temporarily fails but reconnects. This means
                # there was an error but there is no longer any issue
            elif status.category == PNStatusCategory.PNDisconnectedCategory:
                pass
                # This is the expected category for an unsubscribe. This means there
                # was no error in unsubscribing from everything
            elif status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
                pass
                # This is usually an issue with the internet connection, this is an error, handle
                # appropriately retry will be called automatically
            elif status.category == PNStatusCategory.PNAccessDeniedCategory:
                pass
                # This means that PAM does allow this client to subscribe to this
                # channel and channel group configuration. This is another explicit error
            else:
                pass
                # This is usually an issue with the internet connection, this is an error, handle appropriately
                # retry will be called automatically
        elif status.operation == PNOperationType.PNSubscribeOperation:
            # Heartbeat operations can in fact have errors, so it is important to check first for an error.
            # For more information on how to configure heartbeat notifications through the status
            # PNObjectEventListener callback, consult <link to the PNCONFIGURATION heartbeart config>
            if status.is_error():
                pass
                # There was an error with the heartbeat operation, handle here
            else:
                pass
                # Heartbeat operation was successful
        else:
            pass
            # Encountered unknown status type
 
    def presence(self, pubnub, presence):
        global presenceResult
        presenceResult = presence
        pass  # handle incoming presence data
 
    def message(self, pubnub, message):
        global messageResult
        messageResult = message
        print messageResult.message.get('action')
        print messageResult.channel
        pass  # handle incoming messages
 
 
pubnub.add_listener(MySubscribeCallback())

###subscribe
pubnub.subscribe().channels('fiona').execute()


### publishing
from pubnub.exceptions import PubNubException
try:
    envelope = pubnub.publish().channel("fiona").message({
        'name': 'Alex',
        'online': True
    }).sync()
    print("publish timetoken: %d" % envelope.result.timetoken)
except PubNubException as e:
    handle_exception(e)


