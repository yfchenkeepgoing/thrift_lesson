from match_client.match import Match
from match_client.match.ttypes import User
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


# python从终端中读取op
from sys import stdin

def operate(op, user_id, username, score): #改名为操作函数，op是操作
    # Make socket
    transport = TSocket.TSocket('127.0.0.1', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    user = User(user_id, username, score) #根据参数来创建一个用

    #根据从终端输入的信息op来判断调用什么函数
    if op == "add":
        client.add_user(user, "")
    elif op == "remove":
        client.remove_user(user, "")

    # Close!
    transport.close()

#添加一个main函数
def main(): 
    for line in stdin:
        op, user_id, username, score = line.split(' ') #用空格隔开的四个参数

        # 需要将score和user_id转换成int类型，在定义变量时不需要定义变量类型
        operate(op, int(user_id), username, int(score))


if __name__ == "__main__":
    main()


