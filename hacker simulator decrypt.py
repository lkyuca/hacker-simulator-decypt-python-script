# hacker simulator decrypt.py
def decrypt(code_str):
    valid_chars = set("0123456789ABCDEF")
    parts = code_str.upper().split(':')
    valid = [p for p in parts if p and all(ch in valid_chars for ch in p)]
    if len(valid) < 3:
        raise ValueError("Te weinig geldige hex-tokens (minimaal 3 nodig).")
    return ':'.join(valid[:3])


# <-- hier prompt direct in input()
while True:
    user_input = input("Input voor decryptie: ").strip()
    try:
     result = decrypt(user_input)
     print("Gedecrypteerde code:", result)
    except Exception as e:
     print("Fout tijdens decryptie:", e)
