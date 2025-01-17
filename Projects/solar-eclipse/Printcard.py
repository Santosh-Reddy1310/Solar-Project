def printCard(number, shape):
    # Define border characters and suit symbols
    border = {"top_left": "╔", "top_right": "╗", "bottom_left": "╚", "bottom_right": "╝", "horizontal": "═", "vertical": "║"}
    suits = {"club": "♣", "heart": "♥", "diamond": "♦", "spade": "♠", "none": " "}
    
    # Map numbers to card faces
    face_cards = {1: "A", 12: "Q", 13: "K"}
    number = face_cards.get(number, number)  # Use face value if applicable
    
    # Get the symbol for the shape
    symbol = suits.get(shape, " ")

    # Card dimensions
    width = 11
    height = 9

    for row in range(height):
        if row == 0:
            # Top border
            print(border["top_left"] + border["horizontal"] * (width - 2) + border["top_right"])
        elif row == height - 1:
            # Bottom border
            print(border["bottom_left"] + border["horizontal"] * (width - 2) + border["bottom_right"])
        elif row == 1:
            # Top number
            print(border["vertical"] + f" {number}".ljust(width - 2) + border["vertical"])
        elif row == height - 2:
            # Bottom number
            print(border["vertical"] + f"{number} ".rjust(width - 2) + border["vertical"])
        elif row == height // 2:
            # Center symbol
            print(border["vertical"] + symbol.center(width - 2) + border["vertical"])
        else:
            # Empty rows
            print(border["vertical"] + " " * (width - 2) + border["vertical"])
# Ace of Spades
printCard(1, "spade")

# Queen of Hearts
printCard(12, "heart")

# 10 of Clubs
printCard(10, "club")

# King of Diamonds
printCard(13, "diamond")

# Blank Card with No Shape
printCard(0, "none")
