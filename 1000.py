from Crypto.Util.number import *



hex_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_data = bytes.fromhex(hex_str)
long_data = bytes_to_long(bytes_data)
print(long_data)
a = (2**4+2**12+2**20+2**28+2**4+2**4+2**4+2**4+2**4+2**4+2**4+2**4+2**4+ ) ^ long_data
print(a)
print(long_to_bytes(a))