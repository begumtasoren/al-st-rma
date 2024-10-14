def is_palindrome(n):
    # 1. Girdi sadece harf ve rakamlardan oluşacak şekilde filtrelenir.
    filtered_n = ''.join(filter(str.isalnum, n)).lower()

    # 2. Başlangıç ve bitiş pointer'ları.
    left, right = 0, len(filtered_n) - 1

    # 3. Pointer'lar ortada buluşuncaya kadar karşılaştırma yapılır.
    while left < right:
        if filtered_n[left] != filtered_n[right]:
            return False  # Eşleşme başarısızsa palindrom değil.
        left += 1  # Sol pointer'ı sağa kaydır.
        right -= 1  # Sağ pointer'ı sola kaydır.

    return True  # Tüm karakterler eşleşirse palindromdur.

# Kullanıcıdan sürekli veri alacağımız döngü.
while True:
    user_input = input("Bir metin girin (çıkmak için 'q' yazın): ")

    # Kullanıcı çıkmak isterse döngüden çıkılır.
    if user_input.lower() == 'q':
        print("Programdan çıkılıyor...")
        break

    # Palindrom kontrolü yapalım ve sonucu gösterelim.
    if is_palindrome(user_input):
        print(f"'{user_input}' bir palindromdur.")
    else:
        print(f"'{user_input}' bir palindrom değildir.")
