# =====================================
# 1. Caesar Cipher
# =====================================
def caesar_cipher(message, shift, decrypt=False):
    """Encrypt or decrypt a Caesar cipher."""

    if decrypt:
        shift = -shift

    result = ""

    for char in message:

        if char.isalpha():

            base = ord("A") if char.isupper() else ord("a")
            letter = ord(char) - base
            new_letter = (letter + shift) % 26

            result += chr(new_letter + base)

        else:
            result += char

    return result

# =====================================
# 2. Vigenère Cipher
# =====================================
def vigenere_cipher(message, keyword, encrypt=True, reverse=False):
    """
    reverse=False -> Standard Vigenère
        Encrypt: +key
        Decrypt: -key

    reverse=True -> Codecademy/challenge version
        Encrypt: -key
        Decrypt: +key
    """

    result = ""
    keyword = keyword.lower()
    key_index = 0

    for char in message:

        if char.isalpha():

            shift = ord(keyword[key_index % len(keyword)]) - ord("a")

            base = ord("A") if char.isupper() else ord("a")
            letter = ord(char) - base

            if reverse:
                if encrypt:
                    new_letter = (letter - shift) % 26
                else:
                    new_letter = (letter + shift) % 26
            else:
                if encrypt:
                    new_letter = (letter + shift) % 26
                else:
                    new_letter = (letter - shift) % 26

            result += chr(new_letter + base)
            key_index += 1

        else:
            result += char

    return result

# =====================================
# 3. Messages
# =====================================
# ======================
# Caesar Messages
# ======================

secret_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

new_secret_message = "Thanks for the message. I was able to decode it with help from Gemini, an AI assistant. Do you use AI assistant while coding?"

message_to_vishal = "Drkxuc pyb dro wocckqo. S gkc klvo dy nomyno sd gsdr rovz pbyw Qowsxs, kx KS kccscdkxd. Ny iye eco KS kccscdkxd grsvo mynsxq?"

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
        
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

most_recent_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# ======================
# Vigenère Messages
# ======================

vigenere_message = (
    "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
)

vigenere_reply = (
    "Hoouyz hv mvi mcy glbkwuu ts hzs hoszs jvhzssuupbn qvrlg. P howuy avpg tszghul kpzs pl rlqvrlr pb uc awts."
)

# =====================================
# 4. Main Program
# =====================================

def main():

    # Caesar Tests
    print(caesar_cipher(secret_message, 7, decrypt=True))
    print(caesar_cipher(first_message, 10, decrypt=True))
    print(caesar_cipher(second_message, 14, decrypt=True))

    print()      # Blank line for readability

    # Vigenère Test
    decoded = vigenere_cipher(
        vigenere_message,
        friends_keyword,
        encrypt=False,
        reverse=True
    )

    print(decoded)

# ======================
# Vigenère Tests
# ======================

friends_keyword = "friends"

decoded = vigenere_cipher(
    vigenere_message,
    friends_keyword,
    encrypt=False,
    reverse=True
)

print(decoded)

# =====================================
# 5. Run Program
# =====================================

if __name__ == "__main__":
    main()
