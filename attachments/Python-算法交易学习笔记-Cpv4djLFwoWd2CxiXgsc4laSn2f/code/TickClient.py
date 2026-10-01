#
# Python Script
# with Tick Data Client
#
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
# 先在另一终端启动: python TickServer.py
# 本脚本以 SUB 连接 PUB，订阅 SYMBOL 频道并打印消息。
# 无限循环；Ctrl+C 结束。
#
import zmq  # ZeroMQ 的 Python 封装

context = zmq.Context()  # 客户端核心对象，与服务器一样
socket = context.socket(zmq.SUB)  # SUB：订阅端（服务器是 PUB）
socket.connect("tcp://0.0.0.0:5555")  # 连到发布端的地址与端口
# 订阅频道前缀；消息须以 SYMBOL 开头才能匹配（见 TickServer 的 msg 格式）
socket.setsockopt_string(zmq.SUBSCRIBE, "SYMBOL")

while True:  # 持续接收；无数据时会阻塞
    data = socket.recv_string()  # 取一条字符串消息
    print(data)  # 打到 stdout
