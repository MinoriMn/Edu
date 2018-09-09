import socket
import subprocess
import time


HOST = "localhost"
PORT = 10500


def julius_receiver():
    # julius起動スクリプトを実行
    p = subprocess.Popen(["sh julius_start.sh"], stdout=subprocess.PIPE, shell=True)
    pid = p.stdout.read().decode('utf-8') # juliusのプロセスIDを取得
    print(pid)
    time.sleep(4)
    # TCPクライアントを作成し接続
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # サーバからのデータ受信と
    try:
        data = ""
        # 前回認識した命令
        killword = ""

        while 1:
            if "</RECOGOUT>\n." in data:
                word = ""
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index + 6:line.find('"', index + 6)]
                        word += str(line)

                    if word != killword:
                        print(word)
                        killword = word
                        print("kill:" + killword)

            else:
                data = data + client.recv(1024).decode('utf-8')

    except KeyboardInterrupt:
        # CTRL+Cで終了
        print("KeyboardInterrupt occured.")
        p.kill()  #
        subprocess.call(["kill " + pid], shell=True)  # juliusのプロセスを終了
        client.close()
