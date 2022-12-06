from aocd import data


def get_msg(msg, msg_len):
    for i in range(msg_len, len(msg)):
        if len(set(msg[i - msg_len : i])) == msg_len:
            return i


print(get_msg(data, 4))
print(get_msg(data, 14))
