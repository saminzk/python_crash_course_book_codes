from random import choice

lottery = ['B', 1, 2, 3, 'G',4, 5, 'H', 6, 7, 'D', 8, 9, 10, 'E']

winning_ticket = []


while len(winning_ticket) < 4:
    pulled_item = choice(lottery)

    if pulled_item not in winning_ticket: 
        print(f"We pulled a {pulled_item}")
        winning_ticket.append(pulled_item)