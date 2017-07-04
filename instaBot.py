import requests, urllib

ACCESS_TOKEN = "1595866987.0d51ae1.ecb2290bd5f74b1584894260fc8cfd64"
BASE_URL= "https://api.instagram.com/v1/"

def apni_jaankari():
    request = (BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request)
    user_information = requests.get(request).json()
    if user_information["meta"]["code"] == 200:
        if len(user_information["data"]):
            print "Username: %s" % (user_information["data"]["username"])
            print "Followers: %s" % (user_information["data"]["counts"]["followed_by"])
            print "Following: %s" % (user_information["data"]["counts"]["follows"])
            print "Posts: %s" % (user_information["data"]["counts"]["media"])
        else:
            print "USER DOES NOT EXIST"
    else:
        print "RECIEVED STATUS CODE IS NOT 200"

def get_user_id(instagram_username):
    request = (BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username, ACCESS_TOKEN)
    print 'GET request url : %s' % (request)
    user_information = requests.get(request).json()
    if user_information["meta"]["code"] == 200:
        if len(user_information["data"]):
            return user_information["data"][0]["id"]
        else:
            return None
    else:
        print "RECIEVED STATUS CODE IS NOT 200"
        exit()


def get_user_information(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request = (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request)
    user_information = requests.get(request).json()

    if user_information["meta"]["code"] == 200:
        if len(user_information["data"]):
            print "Username: %s" % (user_information["data"]["username"])
            print "Followers: %s" % (user_information["data"]["counts"]["followed_by"])
            print "Following: %s" % (user_information["data"]["counts"]["follows"])
            print "Posts: %s" % (user_information["data"]["counts"]["media"])
        else:
            print "There is no data for this user"
    else:
        print "Recieved status code is not 200"


def khudki_post():
    request = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request)
    apni_post = requests.get(request).json()

    if apni_post["meta"]["code"] == 200:
        if len(apni_post["data"]):
            print apni_post["data"][0]["id"]
            tasveer_ka_naam = apni_post["data"][0]["id"] + ".jpeg"
            link = apni_post["data"][0]["images"]["standard_resolution"]["url"]
            urllib.urlretrieve(link, tasveer_ka_naam)
            print "Aapki tasveer download ho chuki hai"
        else:
          print "Media does not exist"
    else:
        print "Recieved status code is not 200"

def get_users_post(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print "User does not exist!"
        exit()
    request = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)
    print "GET request url : %s" % (request)
    user_media = requests.get(request).json()

    if user_media["meta"]["code"] == 200:
        if len(user_media["data"]):
            link = user_media["data"][0]["images"]["standard_resolution"]["url"]
            tasveer_ka_naam = user_media["data"][0]["id"] + ".jpeg"
            urllib.urlretrieve(link, tasveer_ka_naam)
            print"Aapke dost ki tasveer download hp chuki hai"
            return user_media["data"][0]["id"]
        else:
          print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    return user_media

def bot_main():
    while True:
        print '\n'"Hey! Welcome to instaBot!\n\nHere are your menu options:\n" \
              "a.Get your own details\nb.Get details of a user by username\n" \
              "c.Get your own recent post\nd.Get the recent post of a user by username\n"
        choose_option = raw_input("Choose any option from tha given menu:")
        if choose_option == "a":
            apni_jaankari()
        elif choose_option == "b":
            instagram_username= raw_input("Enter the username of user")
            get_user_information(instagram_username)
        elif choose_option == "c":
            khudki_post()
        else:
            instagram_username = raw_input("Enter the username of user")
            get_users_post(instagram_username)
bot_main()













