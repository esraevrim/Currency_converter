import services 
SELECTION_1 = "1"
SELECTION_2 = "2"
SELECTION_3 = "3"
SELECTION_4 = "4"
while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1. Döviz Alış Ve Satış Görüntüleme")
    print("2. Döviz Çevirme")
    print("3. Döviz Bilgisi Görüntüleme")
    print("4. Programdan Çıkış")
    choice = input("Seçiminizi girin (1, 2, 3 ya da 4): ")
    if choice == SELECTION_1:
        services.buying_selling_info()
    elif choice == SELECTION_2:
        services.convert_money()
    elif choice == SELECTION_3:
        services.currency_info()
    elif choice == SELECTION_4:
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim patınız lütfen tekrar deneyin.")