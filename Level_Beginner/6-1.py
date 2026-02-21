# 6.1 List of Tuples
friends = ["Aditya", "Beatrix", "Charlie", "Danielle", "Emerson"]
friend_lengths = [(name, len(name)) for name in friends]
print(f"Friend Name Lengths: {friend_lengths}")