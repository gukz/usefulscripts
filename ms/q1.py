"""
3.15
3.85
+ 结果7
3.2
3.9
+ 结果7.1
平均3.6
引导过程太慢
编码第一遍有问题
没有考虑符号位
没有考虑入参范围
"""


def round_by(origin, round_bit):
    flag = 1 if origin > 0 else -1
    origin *= flag
    power_origin = origin * pow(10, round_bit)
    int_origin = int(origin * pow(10, round_bit))
    if power_origin == int_origin:
        return origin * flag
    round_up = False
    if power_origin - int_origin == 0.5:
        if int_origin % 2 == 1:
            round_up = True
    elif power_origin - int_origin > 0.5:
        round_up = True
    if round_up:
        return (int_origin + 1) / pow(10, round_bit) * flag
    else:
        return int_origin / pow(10, round_bit) * flag


if __name__ == "__main__":
    tests = [
        (3.1415, 3.142,),
        (3.8765, 3.876),
        (3.9292, 3.929),
        (3.1827, 3.183),
        (3.6545, 3.654),
        (3.2275, 3.228),
        (3.888501, 3.889),
        (3.9995, 4),
        (-3.9995, -4),
    ]
    for t in tests:
        print(t, round_by(t[0], 3))
        assert t[1] == round_by(t[0], 3)
