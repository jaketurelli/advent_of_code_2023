import file_helper as fh

def get_winners_and_hand(line_arg):
    """get winners and hand numbers in arrays from a line"""
    winners_and_hand = line_arg.split(":")[1].strip().split("|")
    winners  = [int(i) for i in winners_and_hand[0].strip().split()]
    hand = [int(i) for i in winners_and_hand[1].strip().split()]
    return winners, hand

def part_1(data_arg):
    """part 1"""
    
    total_score = 0
    for line in data_arg:
        winners, hand = get_winners_and_hand(line)

        card_score = 0
        for x in hand:
            if x in winners:
                card_score = 1 if card_score == 0 else card_score * 2

        total_score += card_score
    return total_score

def part_2(data_arg):
    """part 2"""
    total_cards = 0
    card_count = [1] * len(data_arg)
    for i, line in enumerate(data_arg):
        winners, hand = get_winners_and_hand(line)
        number_matches = 0
        for x in hand:
            if x in winners:
                number_matches += 1
        
        for j in range(number_matches):
            card_count[i+j+1] += 1 * card_count[i]
        

    return sum(card_count)


data_1 = fh.get_data('day_04.txt')
data_2 = fh.get_data('day_04.txt')
print(part_1(data_1))
print(part_2(data_2))