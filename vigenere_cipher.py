def vigenere_cipher(text, key, encrypt=True):
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A' if key_char.isupper() else 'a')
            if char.isupper():
                if encrypt:
                    result.append(chr((ord(char) + shift - ord('A')) % 26 + ord('A')))
                else:
                    result.append(chr((ord(char) - shift - ord('A')) % 26 + ord('A')))
            elif char.islower():
                if encrypt:
                    result.append(chr((ord(char) + shift - ord('a')) % 26 + ord('a')))
                else:
                    result.append(chr((ord(char) - shift - ord('a')) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def main():
    while True:
        print("Pilih operasi:")
        print("1. Enkripsi")
        print("2. Deskripsi")
        print("3. Keluar")
        choice = input("Masukkan pilihan (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Masukkan teks yang ingin dienkripsi: ")
            key = input("Masukkan kunci: ")
            cipher_text = vigenere_cipher(plaintext, key, encrypt=True)
            print("Teks terenkripsi:", cipher_text)
        elif choice == '2':
            ciphertext = input("Masukkan teks yang ingin didekripsi: ")
            key = input("Masukkan kunci: ")
            decrypted_text = vigenere_cipher(ciphertext, key, encrypt=False)
            print("Teks terdekripsi:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()
