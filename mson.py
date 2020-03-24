import json


def parse(s: str):
    start = 0
    stop = 0

    result = []
    chunk = []

    for i in range(len(s)):
        if s[i] == "{":
            start += 1
        elif s[i] == "}":
            stop += 1

        chunk.append(s[i])

        if start == stop and start != 0:
            # json字符串
            start = 0
            stop = 0
            try:
                result.append(json.loads("".join(chunk)))
            except json.decoder.JSONDecodeError as e:
                print("mson.parse: ", e)
                result.append("".join(chunk))
            chunk = []

    # 视为非json字符串
    if len(chunk) > 0:
        result.append("".join(chunk))

    return result


if __name__ == "__main__":
    # value = '{"size": {"width": 0, "height": 0}, "action": "capture", "debug": 1}{xxxxxxx}'
    value = '{"size": {"width": 0, "height": 0}, "action": "capture", "debug": 1}{"size": {"width": 0, "height": 0}, "action": "capture", "debug": 1}}'

    print(isinstance(parse(value)[2], dict))
