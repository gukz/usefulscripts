def reverse_words(sent):
    words = list()
    start = 0
    end = 0

    while end < len(sent):
        if sent[end] == " ":
            words.append(sent[start:end])
            start = end + 1
        end += 1
    words.append(sent[start:end])
    new_sent = ""
    for word in words[::-1]:
        new_sent += word + " "
    return new_sent[:-1]


if __name__ == "__main__":
    sent = " hello  world aaa"
    reversed_word = reverse_words(sent)
    print(reversed_word)
    assert reversed_word == "aaa world  hello "
