def GenerateCode(func):
    def decode(secret_code):
        decoded_message = ''
        for code in secret_code:
            decoded_message += chr(code)
        func(decoded_message)
    return decode


@GenerateCode
def print_decoded_message(decoded_message):
    print(decoded_message)


secret_code1 = bytearray([65, 69, 70, 73, 75])  
secret_code2 = bytearray([72, 101, 108, 108, 111])  
secret_code3 = bytearray([67, 111, 109, 112, 117, 116, 101, 114])  

print_decoded_message(secret_code1)
print_decoded_message(secret_code2)
print_decoded_message(secret_code3)
