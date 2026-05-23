import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")
text = "Rohit Patil"

# 1. Get the token IDs
tokens = encoding.encode(text)
print(f"Token IDs: {tokens}")

print("\nToken Mapping:")
print(f"{'Token ID':<10} | {'Decoded Value'}")
print("-" * 25)

# 2. Check how each token is converted
for token_id in tokens:
    # decode_single_token_bytes returns a bytes object (e.g., b'Roh')
    token_bytes = encoding.decode_single_token_bytes(token_id)
    
    # Decode bytes to a readable string format
    token_string = token_bytes.decode('utf-8', errors='replace')
    
    # Using repr() to clearly show spaces or hidden characters
    print(f"{token_id:<10} | {repr(token_string)}")