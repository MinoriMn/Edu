import socket
import subprocess
import time
import threading


HOST = "localhost"
PORT = 10500


def julius_receiver():
    global p
    global pid
    global client

    # julius起動スクリプトを実行
    p = subprocess.Popen(["sh julius_start.sh"], stdout=subprocess.PIPE, shell=True)
    pid = p.stdout.read().decode('utf-8')  # juliusのプロセスIDを取得
    print(pid)
    time.sleep(2)
    # TCPクライアントを作成し接続
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    juliusReceiverThread = threading.Thread(target=receive, name='julius_receiver_thread')
    juliusReceiverThread.start()


def receive():
    global p
    global pid
    global client

    # サーバからのデータ受信と
    try:
        data = ""
        sentence = ""

        while 1:
            if "</RECOGOUT>\n." in data:
                word = ""
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index + 6:line.find('"', index + 6)]
                        word = str(line)

                    if word != '' and word != '[s]' and word != '[/s]':
                        sentence += word
                        print(sentence)

                    data = ""

                sentence = ""

            else:
                data = data + client.recv(1024).decode('utf-8')

    except KeyboardInterrupt:
        # CTRL+Cで終了
        print("KeyboardInterrupt occured.")
        p.kill()  #
        subprocess.call(["kill " + pid], shell=True)  # juliusのプロセスを終了
        client.close()


# for debug
# julius_receiver()
