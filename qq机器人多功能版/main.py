from receive import rev_msg
import socket
import requests
import random
import datetime
import time
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import string
from  binascii import hexlify
from Crypto.Cipher import AES
import requests,os,json,base64
qq_robot=eval(input('请输入机器人QQ号：'))
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}
tiangou_list=['我不想再做舔狗了 好聚好散吧 以后你走你的独木桥 我在下面撑着桥呜呜呜 你过桥一定要小心啊。'
    ,'我爸说再敢网恋就打断我的腿，幸好不是胳膊，这样我还能继续和你打字聊天，就算连胳膊也打断了，我的心里也会有你位置。'
,'她吊着我怎么了 她爱我才吊着我 她怎么不吊着别人。'
    ,'昨天在工地扛沙袋我一下子扛了三袋 工友们问我为什么这么能扛?我眼泪瞬间就下来了，是啊为什么我这么能扛就是扛不住想你。'
    ,'今天我问你“你爱我吗”你跟我说了一句“我爱你妈”我不禁陷入了沉思原来你已经爱我到连我妈都思考在内了我们一定会长久的。',
         '“下雨了，雨伞借给你” “那你呢?” “没关系，我摇花手回去”。',
         '今天厂里发工资了，发了3000，你以为我会给你3000?不对，我只给你300，因为我同时舔了十个。','只要你回头，我就在。',
         '只要我舔的够快，其他的狗就无从下手。','晚上：以后再也不主动找你了 第二天：早安。',
         '今天我对他说我想问一下：爱奇艺会员你有吗?他没发现是“我爱你”的藏头诗 还叫我滚。',
         '我给你发了99条消息 你终于肯回我了 你说“你发你妈 烦不烦” 我一下子就哭了，原来努力真的有用，你已经开始考虑见我的妈妈了，你也挺喜欢我的吧。',
         '他从来不说想我 聊天记录搜索了一下“想你”两个字 全都是:“那波你怎么不上啊 你在想你妈呢”。',
         '孩子生下来吧，我跟他姓。',
         '看你在线，邀你吃鸡，秒被拒绝，再看你已经开了，我知道，你肯定是为了不连累我才不和我玩。',
         '兄弟 你回一下她吧 她高兴了 就会回我了。',
         '宝 每次跟你打王者 我总希望对面有人来偷水晶 你会说我们家被偷了 这时我就很开心 原来我可以跟你有个家。',
         '宝 你今天怎么没有跟我说早啊 群发没有勾上我吗 明天一定要勾上我噢',
         '今天他终于叫了我的名字 虽然叫错了，但是没关系 我马上就去改名',
         '大哥，求你哄哄她吧，她心情好了，就愿意理我了',
         '他朋友圈屏蔽我了，我陷入了沉思，大都是屏蔽家人，原来他把我当做她家人了，他好细节啊，我更爱他了',
         '我一个月工资五千 你以为我会给你五千吗 我会再借二百发5200给你 太爱你了 宝',
         '宝 你永远都不知道 我最爱你的时候哭得我荞麦枕头都发芽了',
         '今天晚上有点冷，本来以为街上没有人，结果刚刚偷电瓶的时候被抓，本来想反抗，结果警察说了一句老实点别动，我立刻就放弃了抵抗，因为我记得你说过你喜欢老实人。',
         '今天下雨了，你跟她出门的时候记得要带伞，多穿一点衣服，玫瑰花扎手，拿的时候，注意不要被扎到了，亲嘴的时候记得要看一下她的健康码呀！宝贝，呜呜呜'];
help='菲菲内置多种功能，通过发送命令可执行特殊操作\n★★ 示例 ★★\n查询天气预报信息，示例：天气深圳\n查询成语介绍，示例：成语一心一意\n按歌曲名称查询歌词，示例：歌词 歌曲名称\n按歌曲名称分享音乐，示例：歌曲 歌曲名称\n中译英、英译中，示例：翻译i love you\n查询星座今日运势，示例：星座运势 天秤座\n' \
     '查询星座介绍请直接发送：天秤座\n汉字五笔拼音笔画查询示例：礡字\n想看笑话，请直接发送：笑话\n生日书示例：生日书 02-02 性格，可以查询的有性格、爱情、财运、事业、健康、幸运数字、适合的恋爱对象、适合的朋友对象\n发送：舔狗语录，头像，壁纸，学习，爆照，帅哥，不用加参数'
class Encrypyed():
    '''传入歌曲的ID，加密生成'params'、'encSecKey 返回'''
    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    def aes_encrypt(self,text, key):
        iv = '0102030405060708'
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
        result = encryptor.encrypt(text.encode("utf-8"))
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str

    def rsa_encrpt(self,text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def work(self,ids,br=128000):
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        text = json.dumps(text)
        i=self.create_secret_key(16)
        encText =self.aes_encrypt(text, self.nonce)
        encText=self.aes_encrypt(encText,i)
        encSecKey=self.rsa_encrpt(i,self.pub_key,self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data

    def search(self,text):
        text = json.dumps(text)
        i = self.create_secret_key(16)
        encText = self.aes_encrypt(text, self.nonce)
        encText = self.aes_encrypt(encText, i)
        encSecKey = self.rsa_encrpt(i, self.pub_key, self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data


class search():
    '''跟歌单直接下载的不同之处，1.就是headers的referer
                              2.加密的text内容不一样！
                              3.搜索的URL也是不一样的
        输入搜索内容，可以根据歌曲ID进行下载，大家可以看我根据跟单下载那章，自行组合
                                '''
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/'} ###!!注意，搜索跟歌单的不同之处！！
        self.main_url='http://music.163.com/'
        self.session = requests.Session()
        self.session.headers=self.headers
        self.ep=Encrypyed()

    def search_song(self, search_content,search_type=1, limit=10):
        """
        根据音乐名搜索
      :params search_content: 音乐名
      :params search_type: 不知
      :params limit: 返回结果数量
      return: 可以得到id 再进去歌曲具体的url
        """
        song_id_list=[]
        url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        text = {'s': search_content, 'type': search_type, 'offset': 0, 'sub': 'false', 'limit': limit}
        data = self.ep.search(text)
        resp = self.session.post(url, data=data)
        result = resp.json()
        if result['result']['songCount']<= 0:
            print('搜不到！！')
        else:
            songs = result['result']['songs']
            for song in songs:
                song_id,song_name,singer,alia = song['id'],song['name'],song['ar'][0]['name'],song['al']['name']
                #print(song_id,song_name,singer,alia)
                song_id_list.append(song_id)
        return song_id_list[0]
def get_lyrics_pro(id):
    link='http://music.163.com/api/song/media?id='+str(id)
    web_data = requests.get(url=link, headers=headers).text
    json_data = json.loads(web_data)
    try:
        return json_data['lyric']
    except BaseException:
        return "歌曲id错误,请检查后重试！！！"
def send_msg(resp_dict):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, 5700))

    msg_type = resp_dict['msg_type']  # 回复类型（群聊/私聊）
    number = resp_dict['number']  # 回复账号（群号/好友号）
    msg = resp_dict['msg']  # 要回复的消息

    # 将字符中的特殊字符进行url编码
    msg = msg.replace(" ", "%20")
    msg = msg.replace("\n", "%0a")

    if msg_type == 'group':
        payload = "GET /send_group_msg?group_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    elif msg_type == 'private':
        payload = "GET /send_private_msg?user_id=" + str(
            number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
    print("发送" + payload)
    client.send(payload.encode("utf-8"))
    client.close()
    return 0

img_list1 = []
img_list2 = []
img_list3 = []
img_list4 = []
def get_img_list(key):
    img_list=[]
    for j in [0,24,48,72,96,120]:
        # 获取网站数据
        url = requests.get('https://www.duitang.com/search/?kw={}&type=feed&start={}'.format(key,j))
        # url.encoding = 'utf-8'  #如果需要用到页面中的汉字内容，则需要进行解码，否则中文会出现乱码
        html = url.text
        # 解析网页
        soup = BeautifulSoup(html, 'html.parser')
        # 获取所有的img标签
        movie = soup.find_all('div', class_='mbpho')
        # print(movie)
        # 获取src路径
        for i in movie:
            imgsrc = i.find_all('img')[0].get('src')
            img_list.append(imgsrc)
    return img_list
img_list1=get_img_list('女')
img_list2=get_img_list('头像')
img_list3 =get_img_list('壁纸')
img_list4 =get_img_list('男生头像')
img_list5 = []
def get_img_study():
    url = requests.get('https://www.163.com/dy/article/G6G1GED00516UFNV.html')
    # url.encoding = 'utf-8'  #如果需要用到页面中的汉字内容，则需要进行解码，否则中文会出现乱码
    html = url.text
    # 解析网页
    soup = BeautifulSoup(html, 'html.parser')
    # 获取所有的img标签
    movie = soup.find_all('p', class_='f_center')
    # print(movie)
    # 获取src路径
    for i in movie:
        imgsrc = i.find_all('img')[0].get('src')
        if 'gif' in imgsrc:
            img_list5.append(imgsrc)
        else:
            imgsrc = imgsrc[imgsrc.rfind('http'):]
            imgsrc = imgsrc[0:imgsrc.rfind('&thumbnail')]
            img_list5.append(imgsrc)
    return img_list5
get_img_study()

def horoscope(constellation):
    # 请求地址
    url = "http://web.juhe.cn/constellation/getAll?" + 'consName={}&type=today&key='.format(constellation)
    # 发送get请求
    r = requests.get(url)
    # 获取返回的json数据
    result = r.json()['summary']
    #print(result)
    return result

def birthday_book(birthday,key):
    url = "http://apis.juhe.cn/fapig/birthdayBook/query?" + 'keyword={}&key='.format(birthday)
    # 发送get请求
    r = requests.get(url)
    # 获取返回的json数据
    result = r.json()['result'][key].replace('<p>','').replace('</p>','')
    return result

def tiangou():
    url = "http://api.tianapi.com/txapi/tiangou/index?" + 'key='
    # 发送get请求
    r = requests.get(url)
    # 获取返回的json数据
    result = r.json()
    #print(result['newslist'][0]['content'])
    return result['newslist'][0]['content']
id_list=[]
while True:
    qq_list = []  # 输入要定时发送消息的QQ号
    now = datetime.datetime.now()
    if (now.hour == 0 and now.minute == 0):
        for qq in qq_list:
            send_msg({'msg_type': 'private', 'number': qq, 'msg': '晚安！'})
            send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:poke,qq={}]'.format(qq)})
        time.sleep(60)
        continue
    if (now.hour == 7 and now.minute == 0):
        for qq in qq_list:
            send_msg({'msg_type': 'private', 'number': qq, 'msg': '早安！'})
            send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:poke,qq={}]'.format(qq)})
        time.sleep(60)
        continue
    try:
        rev = rev_msg()
        id = rev['message_id']
        if (len(id_list) >= 50):
            id_list = []
        print(id_list)
        # print(time1==time2)
        if id not in id_list:
            id_list.append(id)
            print(rev)
        else:
            continue
    except:
        continue
    if rev["post_type"] == "message":
        #print(rev) #需要功能自己DIY
        if rev["message_type"] == "private": #私聊
            message=rev['raw_message']
            qq = rev['sender']['user_id']
            if message=='舔狗语录':
                try:
                    text=tiangou()
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': text})
                    continue
                except:
                    i = random.randint(0, 25)
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': tiangou_list[i]})
                    continue
            if 'face' in message:
                qq = rev['sender']['user_id']
                img = rev['raw_message']
                send_msg({'msg_type': 'private', 'number': qq, 'msg': img})
            elif 'image' in message:
                qq = rev['sender']['user_id']
                img=rev['raw_message']
                send_msg({'msg_type': 'private', 'number': qq, 'msg': img})
            elif '考研' in message:
                try:
                    url = img_list5[random.randint(0, len(img_list5))]
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:image,file={}]'.format(url)})
                except:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
            elif '学习' in message:
                try:
                    url = img_list5[random.randint(0, len(img_list5))]
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:image,file={}]'.format(url)})
                except:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
            elif '数学' in message:
                try:
                    url = img_list5[random.randint(0, len(img_list5))]
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:image,file={}]'.format(url)})
                except:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
            elif '美女' in message:
                try:
                    url = img_list1[random.randint(0, len(img_list1))]
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                except:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
            elif '帅哥' in message:
                try:
                    url = img_list4[random.randint(0, len(img_list4))]
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                except:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
            elif message=='头像':
                qq = rev['sender']['user_id']
                i = random.randint(0, len(img_list2))
                url2=img_list2[i]

                send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:image,file={}]'.format(url2)})
            elif message=='壁纸':
                qq = rev['sender']['user_id']
                i = random.randint(0, len(img_list3))
                url3=img_list3[i]
                send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:image,file={}]'.format(url3)})
            elif message in ['help','帮助']:
                qq = rev['sender']['user_id']
                send_msg({'msg_type': 'private', 'number': qq, 'msg': help})
            elif '戳一戳' in message:
                qq = rev['sender']['user_id']
                send_msg({'msg_type': 'private', 'number': qq, 'msg': '别戳了'})
            elif '星座运势' in message:
                try:
                    constellation = message.split(' ')[1]

                    text = horoscope(constellation)
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': text})
                except:
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '请在星座前面加上空格。'})
            elif '生日书' in message:
                dict = {'性格': 'nature', '爱情': 'love', '财运': 'money', '事业': 'business', '健康': 'health',
                        '幸运数字': 'lucky_num', '适合的恋爱对象': 'in_love', '适合的朋友对象': 'friend'}
                try:
                    birthday = message.split(' ')[1]
                    word = message.split(' ')[2]
                    text = birthday_book(birthday,str(dict[word]))
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': text})
                except:
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '请注意日期（9/1）格式。'})
            elif '爆照' in message:
                try:
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq,
                                  'msg': '[CQ:image,file={}]'.format(img_list1[random.randint(0, len(img_list1))])})

                except:
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '出错了'})
            else:
                url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + message
                s = quote(url, safe=string.printable)
                try:
                    with urllib.request.urlopen(s) as response:
                        html = response.read()
                        qq = rev['sender']['user_id']
                        send_msg({'msg_type': 'private', 'number': qq,
                                  'msg': eval(html.decode("utf-8"))["content"].replace('{br}', '\n')})
                except:
                    qq = rev['sender']['user_id']
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '出错了'})
        elif rev["message_type"] == "group":  # 群聊
            group = rev['group_id']
            if "[CQ:reply" in rev["raw_message"] and "[CQ:at,qq={}]".format(qq_robot) in rev["raw_message"]:#当别人群聊回复机器人时
                message = rev['raw_message'].split(' ')[2]
                url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + message
                s = quote(url, safe=string.printable)
                try:
                    with urllib.request.urlopen(s) as response:
                        html = response.read()
                        qq = rev['sender']['user_id']
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': eval(html.decode("utf-8"))["content"].replace('{br}', '\n')})
                except:

                    send_msg({'msg_type': 'group', 'number': group, 'msg': '重新连接中。。。'})
            elif "[CQ:at,qq={}]".format(qq_robot) in rev["raw_message"]:#群聊艾特
                try:
                    if rev['raw_message'].split(' ')[1] == '在吗':
                        qq = rev['sender']['user_id']
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})
                    elif '爆照' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list1[random.randint(0, len(img_list1))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '学习' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list5[random.randint(0, len(img_list5))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '考研' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list5[random.randint(0, len(img_list5))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '学不下去' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list5[random.randint(0, len(img_list5))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '数学' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list5[random.randint(0, len(img_list5))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '美女' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list1[random.randint(0, len(img_list1))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '照片' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list1[random.randint(0, len(img_list1))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,type=flash,file={}]'.format(url)})

                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif '帅哥' in rev['raw_message'].split(' ')[1]:
                        try:
                            url = img_list4[random.randint(0, len(img_list4))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,type=flash,file={}]'.format(url)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif rev['raw_message'].split(' ')[1] == '壁纸':
                        try:
                            url3 = img_list3[random.randint(0, len(img_list3))]
                            send_msg({'msg_type': 'group', 'number': group,
                                      'msg': '[CQ:image,file={}]'.format(url3)})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '出错了'})
                    elif rev['raw_message'].split(' ')[1] == '舔狗语录':
                        try:
                            text = tiangou()
                            send_msg({'msg_type': 'group', 'number': group, 'msg': text})
                        except:
                            i = random.randint(0, 9)
                            send_msg({'msg_type': 'group', 'number': group, 'msg': tiangou_list[i]})
                    elif rev['raw_message'].split(' ')[1] in ['help', '帮助']:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': help})
                    elif rev['raw_message'].split(' ')[1] in ['头像']:
                        i = random.randint(0, len(img_list2))
                        url2 = img_list2[i]

                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:image,file={}]'.format(url2)})
                    elif 'face' in rev['raw_message'].split(' ')[1]:
                        send_msg({'msg_type': 'group', 'number': group,
                                  'msg': '{}'.format(rev['raw_message'].split(' ')[1])})
                    elif rev['raw_message'].split(' ')[1] == '星座运势':

                        try:
                            constellation = rev['raw_message'].split(' ')[2]
                            text = horoscope(constellation)
                            send_msg({'msg_type': 'group', 'number': group, 'msg': text})
                        except:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '请在星座前面加上空格。'})
                    elif rev['raw_message'].split(' ')[1] == '歌词':
                        try:
                            str1 = '[CQ:at,qq={}] 歌词 '.format(qq_robot)
                            # print(str)
                            song = rev['raw_message'].replace(str1, '')
                            d = search()
                            id = d.search_song(song)
                            text = get_lyrics_pro(id)
                            qq = rev['sender']['user_id']
                            send_msg({'msg_type': 'group', 'number': group, 'msg': text})
                        except:
                            qq = rev['sender']['user_id']
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '请在歌名前面加上空格。'})
                    elif rev['raw_message'].split(' ')[1] == '歌曲':
                        try:
                            str1='[CQ:at,qq={}] 歌曲 '.format(qq_robot)
                            #print(str)
                            song = rev['raw_message'].replace(str1, '')
                            d = search()
                            id=d.search_song(song)
                            qq = rev['sender']['user_id']
                            send_msg(
                                {'msg_type': 'group', 'number': group, 'msg': '[CQ:music,type=163,id={}]'.format(id)})
                        except:
                            qq = rev['sender']['user_id']
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '请在歌名前面加上空格。'})
                    elif rev['raw_message'].split(' ')[1] == '生日书':
                        dict = {'性格': 'nature', '爱情': 'love', '财运': 'money', '事业': 'business', '健康': 'health',
                                '幸运数字': 'lucky_num', '适合的恋爱对象': 'in_love', '适合的朋友对象': 'friend'}
                        try:
                            birthday = rev['raw_message'].split(' ')[2]
                            word = rev['raw_message'].split(' ')[3]
                            text = birthday_book(birthday, str(dict[word]))
                            qq = rev['sender']['user_id']
                            send_msg({'msg_type': 'group', 'number': group, 'msg': text})
                        except:
                            qq = rev['sender']['user_id']
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '请注意格式。'})
                    else:
                        message = rev['raw_message'].split(' ')[1]
                        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + message
                        s = quote(url, safe=string.printable)
                        try:
                            with urllib.request.urlopen(s) as response:
                                html = response.read()
                                # 将获取到的响应内容进行解码，并将json字符串内容转换为python字典格式
                                # 通过下标取到机器人回复的内容
                                qq = rev['sender']['user_id']
                                # print(eval(html.decode("utf-8"))["content"])
                                if 'face' in eval(html.decode("utf-8"))["content"]:
                                    send_msg({'msg_type': 'group', 'number': group,
                                              'msg': '[CQ:face,id=32]'})
                                else:
                                    send_msg({'msg_type': 'group', 'number': group,
                                          'msg': eval(html.decode("utf-8"))["content"].replace('{br}', '\n')})
                                # print(eval(html.decode("utf-8"))["content"])
                        except:

                            send_msg({'msg_type': 'group', 'number': group, 'msg': '重新连接中。。。'})
                except:
                    continue


        else:
            continue
    elif rev["post_type"] == "notice":
        try:
            if rev['sub_type'] == 'poke' and rev['target_id'] == qq_robot and rev['group_id']!=None:
                group = rev['group_id']
                send_msg({'msg_type': 'group', 'number': group, 'msg': '戳我干嘛！'})
        except:
            continue
    else:  # rev["post_type"]=="meta_event":
        continue