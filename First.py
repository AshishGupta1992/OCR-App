import requests, urllib
BASE_URL='https://api.instagram.com/v1/'
APP_ACCESS_TOKEN = '	1da0386405eb42d6bfe8e47771fa6da6'

def get_user_id(insta_username)
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code']  == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received'
        exit()



        def like_post(username):
            post_id = get_post_id(username)

            if post_id:
                request_url = (BASE_URL + 'media/%s/likes') &(post_id)
                payload = {'access_token' : APP_ACCESS_TOKEN}

                print "POST Request URL: %s" %(request_url)

                response = requests.post(request_url, payload ).json()

                if response['meta']['code'] == 200:
                    print "Like successful"

                else:
                    print "like unsuccessful"

                else:
                print "No post found"
                return

            like_post('food_local_junction')