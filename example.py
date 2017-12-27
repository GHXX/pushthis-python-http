import pushthis.pushthis as Please

class Example:

    ## SINGLE PAYLOAD EXAMPLE ##

    ##define these wherever floats your boat
    key = ''
    secret = ''
    accessPointAPI = ''
    accessPointAuth = ''

    ##Create new instance of Pushthis
    pushthis = Please.Pushthis(key, secret, accessPointAPI)

    ##Set the channel and event
    pushthis.set_channel('pushthisNetwork')
    pushthis.set_event('demo')

    ##Lets build the payload
    payload = {
        'username' : 'bob dole',
        'message'  : 'omg soo cool!'
    }

    #Pass the payload
    pushthis.attach(payload)

    #lets send this off!
    response = pushthis.send()
    print('Single payload response is: ' + str(response))






    ## MULTI-PAYLOAD EXAMPLE ##

    pushthis = Please.Pushthis(key, secret, accessPointAPI)


    sendToModerator = {
        'channel' : 'pushthisNetwork',
        'event' : 'demo',
        'data' : {
            'username' : 'bob dole',
            'message'  : 'he trolled me.'
        }
    }

    sendToChatRooms = {
        'channel': 'pushthisNetwork',
        'event': 'demo',
        'data': {
            'username': 'bob dole',
            'message': 'thanks for your report.'
        }
    }

    ## lets queue these payloads ##
    pushthis.add(sendToModerator)
    pushthis.add(sendToChatRooms)

    ## lets send the queued payloads
    response = pushthis.send()
    print('Multi-payload response is: ' + str(response))




    ## AUTHORIZING PAYLOAD REQUEST ##

    pushthis = Please.Pushthis(key, secret, accessPointAuth)
    # pushthis.authorize(boolean, channel, socket_id) # Example of args
    responseTrue = pushthis.authorize(True, 'python-private-chat-room', '49fjD_damkoij3d')
    responseFalse = pushthis.authorize(False, 'python-private-chat-room', '49fjD_damkoij3d')
    print('True request response is: ' + str(responseTrue))
    print('False request response is: ' + str(responseFalse))