import base64

file = open("b64.txt", "r")
coded_string = file.read()
file.close()

def base64_decode(coded_string):

    code = coded_string
    decoded_string = base64.b64decode(code)
    return decoded_string.decode('utf-8')

def main():
    
    plain_text = coded_string
    for i in range(50):
        plain_text = base64_decode(plain_text)
    print(plain_text)

main()
