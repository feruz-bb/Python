# Alfavit
# def generate_vigenere_table():
#     table = []
#     for i in range(26):
#         row = []
#         for j in range(26):
#             row.append(chr((i + j) % 26 + ord('A')))
#         table.append(row)
#     return table
#
#
# # Matnni faqat harflar (A-Z) ga aylantirish
# def clean_text(text):
#     return ''.join([char.upper() for char in text if char.isalpha()])
#
#
# # Kalitni kengaytirish (kalitni asl matn uzunligiga yetkazish)
# def extend_key(message, key):
#     key = list(key.upper())
#     if len(message) == len(key):
#         return key
#     else:
#         for i in range(len(message) - len(key)):
#             key.append(key[i % len(key)])
#     return ''.join(key)
#
#
# # Shifrlash funksiyasi
# def vigenere_encrypt(message, key):
#     table = generate_vigenere_table()
#     message = clean_text(message)
#     key = extend_key(message, key)
#
#     encrypted_message = []
#
#     for i in range(len(message)):
#         row = ord(key[i]) - ord('A')
#         col = ord(message[i]) - ord('A')
#         encrypted_message.append(table[row][col])
#
#     return ''.join(encrypted_message)
#
#
# # Dekriptatsiya funksiyasi
# def vigenere_decrypt(encrypted_message, key):
#     table = generate_vigenere_table()
#     encrypted_message = clean_text(encrypted_message)
#     key = extend_key(encrypted_message, key)
#
#     decrypted_message = []
#
#     for i in range(len(encrypted_message)):
#         row = ord(key[i]) - ord('A')
#         col = table[row].index(encrypted_message[i])
#         decrypted_message.append(chr(col + ord('A')))
#
#     return ''.join(decrypted_message)
#
#
# # Misol
# message = ""
# key = ""
#
# # Shifrlash
# encrypted_message = vigenere_encrypt(message, key)
# print("Shifrlangan matn:", encrypted_message)
#
# # Dekriptatsiya
# decrypted_message = vigenere_decrypt(encrypted_message, key)
# print("Dekriptatsiya qilingan matn:", decrypted_message)
#
# print(vigenere_decrypt('WXAWEBNPJE', 'INNOVATION'))


# Matnni bitlarga aylantirish

#
# def text_to_bits(text):
#     bits = ''.join(format(ord(char), '08b') for char in text)
#     return bits
#
#
# # Bitlarni matnga aylantirish
# def bits_to_text(bits):
#     chars = [chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8)]
#     return ''.join(chars)
#
#
# # Shifrlash funksiyasi (Vernam usuli)
# def vernam_encrypt(message, key):
#     # Matn va kalitning bitlarga aylantirilishi
#     message_bits = text_to_bits(message)
#     key_bits = text_to_bits(key)
#
#     # XOR amalini bajarish
#     encrypted_bits = ''.join(str(int(m) ^ int(k)) for m, k in zip(message_bits, key_bits))
#
#     # Bitlarni qayta matn holiga keltirish
#     encrypted_message = bits_to_text(encrypted_bits)
#     return encrypted_message
#
#
# # Deshifrlash funksiyasi (Vernam usuli)
# def vernam_decrypt(encrypted_message, key):
#     # Shifrlangan matn va kalitning bitlarga aylantirilishi
#     encrypted_bits = text_to_bits(encrypted_message)
#     key_bits = text_to_bits(key)
#
#     # XOR amalini bajarish
#     decrypted_bits = ''.join(str(int(e) ^ int(k)) for e, k in zip(encrypted_bits, key_bits))
#
#     # Bitlarni qayta matn holiga keltirish
#     decrypted_message = bits_to_text(decrypted_bits)
#     return decrypted_message
#
#
# # Misol
# message = "BAQOYEV"  # Shifrlamoqchi bo'lgan matn
# key = "FERUZFE"  # Kalit (kalit uzunligi matnga teng bo'lishi kerak)
#
# # Shifrlash
# encrypted_message = vernam_encrypt(message, key)
# print("Shifrlangan matn:", encrypted_message)
#
# # Deshifrlash
# decrypted_message = vernam_decrypt(encrypted_message, key)
# print("Dekriptatsiya qilingan matn:", decrypted_message)



