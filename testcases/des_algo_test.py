from models.des_algorithm import DES

des = DES()

message = "0123456789ABCDEF"
original_key = "133457799BBCDFF1"

message_bits = des.hex_to_binary(message)

# print(message_bits)

original_key_bits = des.hex_to_binary(original_key)

print(f"KEY: {original_key_bits}")

# print(original_key_bits)

des.generate_keys(original_key_bits)

print(f"\n\nMSG: {des.hex_to_binary(message, present=True)}")

encrypted_bits = des.encrypt_bits(message_bits)

# print(f"E: {encrypted_bits}")

print(f"E_bits: {len(encrypted_bits)}")

print(f"Cipher(E_bits): {des.convert_to_hex(encrypted_bits)}")