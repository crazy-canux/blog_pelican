Title: WebSocket
Date: 2018-04-03 14:46:19
Tags: Network, WebSocket



# WebSocket

websocket用于server和browser之间通讯．

websocket采用特殊报头，使得浏览器和服务器只需要做一个握手的动作．

通讯数据以\x00开头，以\xFF结尾．

url:

    ws://
    wss://

一个客户端只建立一个tcp连接

服务端可以推送/push数据到web客户端

有更加亲量级的头，减少数据传送．
