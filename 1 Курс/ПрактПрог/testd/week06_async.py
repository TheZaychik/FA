import asyncio
import re
import copy
import json

dict = {}


def response_proc(data):
    result1 = re.match(r'put \w+ [0-9]*[.,]?[0-9]+ \d\n', data.decode())
    result2 = re.match(r'get \w+\n', data.decode())
    result3 = re.match(r'get .\n', data.decode())
    if not result1 and not result2 and not result3:
        return "error\nwrong command"
    metrics = data.decode().split(" ")
    if metrics[0] == "put":
        metrics.pop(0)
        if metrics[0] not in dict:
            dict[metrics[0]] = []
        for i in range(1, len(metrics) - 1):
            dict[metrics[0]].append((int(metrics[i + 1]), float(metrics[i])))
        print('Dict\n', dict)
        return "ok"
    elif metrics[0] == "get":
        metrics.pop(0)
        metrics[0] = metrics[0][0:-1]
        print(metrics)
        if metrics[0] == "*":
            ret = copy.deepcopy(dict)
            ret = json.dumps(ret)
            print(ret)
            # for key in dict.keys():
            #     ret += key
            #     for elem in dict[key]:
            #         ret += " " + str(elem)
            # print(ret)
            # ret = ret[0:-1]
            # ret += "\n\n"
        else:
            ret = "ok\\"
            for elem in dict[metrics[0]]:
                ret += metrics[0] + " " + str(elem[1]) + " " + str(elem[0]) + "\\"
            ret = ret[1:-1]
            ret += "\n\n"
        return ret
    else:
        return None


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = response_proc(data)
        self.transport.write(resp.encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8181
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
