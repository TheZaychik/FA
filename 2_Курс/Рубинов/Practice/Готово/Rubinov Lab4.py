from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('<Блэкджек Рубинов>')
root.geometry("1200x800")
root.configure(background="green")


# Достаточно (проверка)
def stand():
    global player_total, dealer_total, player_score
    player_total = 0
    dealer_total = 0

    for score in dealer_score:
        dealer_total += score

    for score in player_score:
        player_total += score

    card_button.config(state="disabled")
    stand_button.config(state="disabled")

    if dealer_total >= 17:
        if dealer_total > 21:
            messagebox.showinfo("Игрок выйграл!!", f"Игрок выйграл!  Дилер: {dealer_total}  Игрок: {player_total}")
        elif dealer_total == player_total:
            messagebox.showinfo("Ничья!!", f"Ничья!!  Дилер: {dealer_total}  Игрок: {player_total}")
        elif dealer_total > player_total:
            messagebox.showinfo("Дилер выйграл!!", f"Дилер выйграл!  Дилер: {dealer_total}  Игрок: {player_total}")
        else:
            messagebox.showinfo("Игрок выйграл!!", f"Игрок выйграл!  Дилер: {dealer_total}  Игрок: {player_total}")
    else:
        dealer_hit()
        stand()


# Проверка Блекджека на раздаче
def blackjack_shuffle(player):
    global player_total, dealer_total, player_score
    player_total = 0
    dealer_total = 0
    if player == "dealer":
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                blackjack_status["dealer"] = "yes"

    if player == "player":
        if len(player_score) == 2:
            if player_score[0] + player_score[1] == 21:
                blackjack_status["player"] = "yes"
        else:
            for score in player_score:
                player_total += score

            if player_total == 21:
                blackjack_status["player"] = "yes"
            elif player_total > 21:
                for card_num, card in enumerate(player_score):
                    if card == 11:
                        player_score[card_num] = 1
                        player_total = 0
                        for score in player_score:
                            player_total += score

                        if player_total > 21:
                            blackjack_status["player"] = "bust"
                else:
                    if player_total == 21:
                        blackjack_status["player"] = "yes"
                    if player_total > 21:
                        blackjack_status["player"] = "bust"

    if len(dealer_score) == 2 and len(player_score) == 2:
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            messagebox.showinfo("Пуш!", "Ничья!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif blackjack_status["dealer"] == "yes":
            messagebox.showinfo("Дилер выйграл!", "Блекджек! Дилер выйграл!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif blackjack_status["player"] == "yes":
            messagebox.showinfo("Игрок выйграл!", "Блекджек! Игрок выйграл!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")

    # Проверка 21 во время игры
    else:
        if blackjack_status["dealer"] == "yes" and blackjack_status["player"] == "yes":
            messagebox.showinfo("Пуш!", "Ничья!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif blackjack_status["dealer"] == "yes":
            messagebox.showinfo("Дилер выйграл!", "21! Дилер выйграл!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
        elif blackjack_status["player"] == "yes":
            messagebox.showinfo("Игрок выйграл!", "21! Игрок выйграл!")
            card_button.config(state="disabled")
            stand_button.config(state="disabled")
    if blackjack_status["player"] == "bust":
        messagebox.showinfo("Игрок перебрал!", f"Игрок проиграл! {player_total}")
        card_button.config(state="disabled")
        stand_button.config(state="disabled")


# Регулеровка размера карт
def resize_cards(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((150, 218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image


# Замешивание карт
def shuffle():
    global blackjack_status, player_total, dealer_total

    player_total = 0
    dealer_total = 0
    blackjack_status = {"dealer": "no", "player": "no"}
    card_button.config(state="normal")
    stand_button.config(state="normal")

    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player, dealer_spot, player_spot, dealer_score, player_score
    dealer = []
    player = []
    dealer_score = []
    player_score = []
    dealer_spot = 0
    player_spot = 0

    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    root.title(f'Карт в колоде: {len(deck)}')

# Добор дилера
def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            dcard = int(dealer_card.split("_", 1)[0])
            if dcard == 14:
                dealer_score.append(11)
            elif dcard == 11 or dcard == 12 or dcard == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(dcard)

            global dealer_image1, dealer_image2, dealer_image3, dealer_image4, dealer_image5

            if dealer_spot == 0:
                dealer_image1 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image1)
                dealer_spot += 1
            elif dealer_spot == 1:
                dealer_image2 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image2)
                dealer_spot += 1
            elif dealer_spot == 2:
                dealer_image3 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_3.config(image=dealer_image3)
                dealer_spot += 1
            elif dealer_spot == 3:
                dealer_image4 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_4.config(image=dealer_image4)
                dealer_spot += 1
            elif dealer_spot == 4:
                dealer_image5 = resize_cards(f'cards/{dealer_card}.png')
                dealer_label_5.config(image=dealer_image5)
                dealer_spot += 1
            root.title(f'Карт в колоде: {len(deck)}')
        except:
            root.title(f'Нет карт')
        blackjack_shuffle("dealer")

# Добор Игрока
def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)
            pcard = int(player_card.split("_", 1)[0])
            if pcard == 14:
                player_score.append(11)
            elif pcard == 11 or pcard == 12 or pcard == 13:
                player_score.append(10)
            else:
                player_score.append(pcard)

            global player_image1, player_image2, player_image3, player_image4, player_image5

            if player_spot == 0:
                player_image1 = resize_cards(f'cards/{player_card}.png')
                player_label_1.config(image=player_image1)
                player_spot += 1
            elif player_spot == 1:
                player_image2 = resize_cards(f'cards/{player_card}.png')
                player_label_2.config(image=player_image2)
                player_spot += 1
            elif player_spot == 2:
                player_image3 = resize_cards(f'cards/{player_card}.png')
                player_label_3.config(image=player_image3)
                player_spot += 1
            elif player_spot == 3:
                player_image4 = resize_cards(f'cards/{player_card}.png')
                player_label_4.config(image=player_image4)
                player_spot += 1
            elif player_spot == 4:
                player_image5 = resize_cards(f'cards/{player_card}.png')
                player_label_5.config(image=player_image5)
                player_spot += 1
            root.title(f'Карт в колоде:  {len(deck)}')
        except:
            root.title(f'Карт нет')
        blackjack_shuffle("player")




my_frame = Frame(root, bg="green")
my_frame.pack(pady=0)

# Рамки для кард
dealer_frame = LabelFrame(my_frame, text="Дилер", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Игрок", bd=0)
player_frame.pack(ipadx=20, pady=10)

# Карты Дилера
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Карты Игрока
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

# Рамка для кнопок
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Кнопки
shuffle_button = Button(button_frame, text="Начать заного", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Ещё!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=1, column=0, pady=10)

stand_button = Button(button_frame, text="Достаточно!", font=("Helvetica", 14), command=stand)
stand_button.grid(row=2, column=0)

# Замешать колоду вначале
shuffle()

root.mainloop()