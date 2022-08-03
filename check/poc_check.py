import requests


# poc检测,传入一个payload
def check_poc(poc):
    # 打开需要检测的url文件
    for url in open('url.txt'):
        url = url.replace('\n', '')
        poc_url = url + poc
        try:
            print("正在检测：")
            print(poc_url)
            poc_data = requests.get(poc_url)
            # 判断返回状态码是否为200
            if poc_data.status_code == 200:
                print(poc_data.content.decode('utf-8'))
                # 把结果写入result文件里
                with open(r'result.txt', 'a+') as f:
                    f.write(poc_url + '\n')
                    f.close()
        except Exception as e:
            # time.sleep(0.5)
            pass


if __name__ == '__main__':
    # poc后缀
    poc = "/general/index/UploadFile.php"
    check_poc(poc)
