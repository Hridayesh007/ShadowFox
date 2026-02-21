justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Number of members
print("Number of founding members: ",len(justice_league))

# 2. Recruitment
justice_league.extend(["Batgirl", "Nightwing"])
print(f"After recruitment: {justice_league}")

# 3. New Leader
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("New leader WW: ",justice_league)

# 4. Separate Flash and Aquaman
justice_league.remove("Green Lantern")
# Find Aquaman's index and insert GL after him
aquaman_idx = justice_league.index("Aquaman")
justice_league.insert(aquaman_idx + 1, "Green Lantern")
print("Separated Flash/Aquaman:  ",justice_league)

# 5. New Team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Team: ",justice_league)

# 6. Sort and Leader
justice_league.sort()
print("Sorted List: ",justice_league)
print("New Leader: ",justice_league[0]) 
print("As C comes first in the sorted order, my guess is: Cyborg")