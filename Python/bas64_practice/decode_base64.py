# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
import base64

base64_message = "PHRyYWNlX2lkPjE3OTc3NTM4ODY2NTg2ODE1MzkxPC90cmFjZV9pZD48YmF0Y2hfbnVtYmVyPjAwMDMwOTM0PC9iYXRjaF9udW1iZXI+PGNoZWNrX2JhdGNoX3NlcXVlbmNlPjE8L2NoZWNrX2JhdGNoX3NlcXVlbmNlPjxkZXBvc2l0X2RhdGU+MjAyMDA5MDI8L2RlcG9zaXRfZGF0ZT48bWZ0PjIxPC9tZnQ+PHRyYW5zYWN0aW9uX2NvZGU+NDY4PC90cmFuc2FjdGlvbl9jb2RlPg=="
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)
