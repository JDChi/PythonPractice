#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json


def get_url(url):
   
    song_id = url.split('=')[1]
    params='bH4mVlBL2afZUOhrGNI1ymmRq74eAWE0/9n1ACW0UpQwPvn1wF2gXV3EdCVfAc1OJYqQrqbcR3huPdakdKJrT5TPkYKKr7+bjTWxq7a9/Owh8hrE3scJtN7IG/IRk4OxfJxS9QwOzDRy0Bhs9jE4dVxGfXR3QRQqadSz5WO1FezXy5RtX8GUhcEzmHUbrIfD'
    encSecKey='c2d1978dc95ab5ed4f0a662beedb23ec698d674e652e05c8f43b637d764578d52434f380691e8795207bba7fad19b64acb6101ffb603001e8fc93ffcd1abfc75400c411532e68b0468c6b05be4f5c0278c6473b41801b4a6af8d3d83e47c5072974e4747ad6014bd0505dcc79c15420db5e81d743b799f501248d8906cd2a970'
    
    #加入请求头，防止被当做欺骗
    headers = {
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0',
       'Referer': 'https://music.163.com/song?id={}'.format(song_id)

    }

    request_params = {
        'params':params ,
        'encSecKey':encSecKey
    }

    comment_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(song_id)

    json_string = requests.post(comment_url , headers = headers , data = request_params)

    #取得hotcomments对象
    hotComments = json.loads(json_string.text)['hotComments']
   
    return hotComments

def main():
	host = input("输入网易云音乐的歌曲地址:")
	
	data = get_url(host)
	result = []

	with open('web.txt' , 'w' ) as f:
		for key in data:
			f.write(str(key.get('user').get('nickname')) + "\n" + str(key.get('content')) + "\n")
			

if __name__ == '__main__':
 	main()








 	

# POST /weapi/v1/resource/comments/R_SO_4_1330348068?csrf_token= HTTP/1.1
# Host: music.163.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0
# Accept: */*
# Accept-Language: en-US,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.5,zh-HK;q=0.3,en;q=0.2
# Accept-Encoding: gzip, deflate, br
# Referer: https://music.163.com/song?id=1330348068
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 474
# DNT: 1
# Connection: keep-alive
# Cookie: JSESSIONID-WYYY=PNjoGFnnZbyjAmF3CKYtgsyJkGG%2Fru3gbmbU9h%5CabUjEF9i06gt%2BfPyKndiT8pMgn7JpC%5CAn30Mv3h0b5IE%2B9Yx757Qss%2FZ200WHZnkDdy0EwljQeh8pZmw%5Cmuki3JgnTRYoMpb3B7UsC7SVQWNfE6o06%2B%2F2gSJiEs7Gyj48Clif31j1%3A1544427253399; _iuqxldmzr_=32; _ntes_nnid=77670a63afbf3b62e8c83ccc8b4a72eb,1533202319225; _ntes_nuid=77670a63afbf3b62e8c83ccc8b4a72eb; __utma=94650624.111609738.1533202320.1544413513.1544423714.12; __utmz=94650624.1544423714.12.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; UM_distinctid=165054e817c52-0ab3295e6b069f8-4a5369-1fa400-165054e817d896; vinfo_n_f_l_n3=1200dc824ce486ac.1.7.1533392356382.1540202246870.1541035195675; __gads=ID=ff7f3e727fe2a902:T=1533392360:S=ALNI_MbVdrJ2agUl0xODr4Tw38dUZe1Xww; usertrack=ezq0o1toC+cXHexIA3dCAg==; _ga=GA1.2.302741250.1533545449; vjuids=-7d0f8634d.16521958b6d.0.2771ea56d515e8; vjlast=1533866773.1541148723.12; WM_NI=Wy8pVj6dcA8SLUWBnqUViDGZr7muqNGIU55hPpLu3tsb5ihkB5WcJcdApxWMgBwNuc%2FTZ3LbVH%2F0PW2WRHWyF53IzzYdgo4rCGCcQF8urGjY2UMkKWcjxR8BCgVOsILLSVk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea5e46fa3a99eafc860869e8ab2d84b979a9baaf348b8bdc0b5b74b82eeb888b42af0fea7c3b92a95a7f891d562f6bcada2bb59908b99a3ed7b978aa7a5c652b2e9a396f44685979bd6b86494b08496b280b1befb8aeb6182eb9984c969a89fc099d647a59eb9aff869ed8c96d4cf6a9698e1d1d35df2899ea9d67386ebfdaaf9729bbca990b77a81998d84d44efcabbea8e953f28b838cca5da1b6b8b3bb4a81b99ab0f24390949db7ea37e2a3; WM_TID=1jDSWqQzwpNEVBVRQVIoPF3HlyRVrOB1; isGd=1; isFs=1; __oc_uuid=3ab3f440-ba42-11e8-8f03-873757ca3946; __utma=187553192.302741250.1533545449.1537165425.1537165425.1; __utmz=187553192.1537165425.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); NTES_CMT_USER_INFO=57027025%7C623893416%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7Cfalse%7CNjIzODkzNDE2QHFxLmNvbQ%3D%3D; __f_=1541489546703; P_INFO=mdhk3399@163.com|1541831561|0|mail163|00&99|hongkong&1541663956&mail163#gud&440100#10#0#0|&0|mail163|mdhk3399@163.com; mail_psc_fingerprint=251b32830baa40c38830adf7389f14a4; __utmc=94650624