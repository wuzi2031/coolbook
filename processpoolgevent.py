from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests,gevent
import time,os
def get_page(url):
    gevent.spawn_raw(requests,url)

def requests(url):
    print('<%s> is getting [%s]' % (os.getpid(), url))
    response = requests.get(url)
    if response.status_code == 200:  # 200代表状态：下载成功了
        return {'url': url, 'text': response.text}
def parse_page(res):
    res = res.result()
    print('<%s> is getting [%s]'%(os.getpid(),res['url']))
    with open('db.txt','a') as f:
        parse_res = 'url:%s size:%s\n'%(res['url'],len(res['text']))
        f.write(parse_res)
if __name__ == '__main__':
    # p = ThreadPoolExecutor()
    # p = ProcessPoolExecutor()
    l = [
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
        'http://www.baidu.com',
    ]
    with ProcessPoolExecutor() as p:
        for url in l:
            res = p.submit(get_page,url).add_done_callback(parse_page) #这里的回调函数拿到的是一个对象。得
        #  先把返回的res得到一个结果。即在前面加上一个res.result() #谁好了谁去掉回调函数
                                # 回调函数也是一种编程思想。不仅开线程池用，开线程池也用
    # p.shutdown()  #相当于进程池里的close和join
    print('主',os.getpid())