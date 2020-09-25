# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
import base64

message = "<trace_id>17977538866586815391</trace_id><batch_number>00030934</batch_number><check_batch_sequence>1</check_batch_sequence><deposit_date>20200902</deposit_date><mft>21</mft><transaction_code>468</transaction_code>"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)