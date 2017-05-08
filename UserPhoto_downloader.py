import requests

# script to download all photos with user tagged on from vk.com


# to receive token to download photos go to https://vk.com/editapp?act=create and create standalone app
# then go to https://oauth.vk.com/authorize?client_id={your_app_id}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos&response_type=token&v=5.52
# where {your_app_id} is id of just created standalone app, then copy the access_token field in browser address bar
# token will be active for next 24 hours
token = 'your toke here'
# id of your or somebody`s VK page
user_id = 'your id here'
# path to existing folder to store photos
path = r'your path here'


def main():
    url = 'https://api.vk.com/method/photos.getUserPhotos'
    params = {'access_token': token,
              'user_id': user_id,
              'sort': 0,
              'count': 1000}
    keys = ['xxxbig', 'xxbig', 'xbig', 'big'] 
    res = requests.get(url, params=params)
    json = res.json()
    for num, photo in enumerate(json['response'][1:]):
            for key in keys:
                key = 'src_' + key
                link = photo.get(key)
                if link:
                    file_name = 'photo_{:0>4}.jpg'.format(num)
                    result = requests.get(link)
                    open(path+file_name, 'wb').write(result.content)
                    print('{} saved'.format(file_name))
                    break
    print('Finished')


if __name__ == '__main__':
    main()
    
