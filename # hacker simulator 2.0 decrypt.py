# hacker simulator decrypt.py
def decrypt(code_str):
    """
    Voorbeeld: "86:P5:G0:F0:AE" -> "86:F0:AE"
    Regels:
    - split op ':'
    - bewaar alleen tokens die volledig uit hex (0-9, A-F) bestaan
    - retourneer de eerste 3 geldige tokens joined met ':'
    """
    valid_chars = set("0123456789ABCDEF")
    parts = code_str.upper().split(':')
    valid = [p for p in parts if p and all(ch in valid_chars for ch in p)]
    if len(valid) < 3:
        raise ValueError("Te weinig geldige hex-tokens (minimaal 3 nodig).")
    return ':'.join(valid[:3])


# <-- hier prompt direct in input()
user_input = input("Input voor decryptie: ").strip()

try:
    result = decrypt(user_input)
    print("Gedecrypteerde code:", result)
except Exception as e:
    print("Fout tijdens decryptie:", e)
