def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def test(fun):
    test_string=fun("Can you hear me")
    print test_string

test(shout)
test(whisper)
