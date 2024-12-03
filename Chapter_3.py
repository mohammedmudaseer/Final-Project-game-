def chapter_three():
    print("Chapter 3: Confronting Robotic Sentinels")
    
    # Action 1: Choose combat or stealth
    choice = input("Choose your approach (combat/stealth): ").lower()
    if choice == "combat":
        if engage_combat():
            print("Combat successful! Acquired advanced weaponry.")
        else:
            print("Defeated! Returning to Chapter 2 to gather resources.")
            from Chapter_2 import chapter_two  # Lazy import
            chapter_two()
    elif choice == "stealth":
        if evade_sentinals():
            print("Stealth successful! Uncovered hidden treasures.")
        else:
            print("Detected! Returning to Chapter 2.")
            from Chapter_2 import chapter_two  # Lazy import
            chapter_two()
    
    # Progress to Chapter 4
    from Chapter_4 import chapter_four  # Lazy import
    chapter_four()

def engage_combat():
    print("Engaging in combat...")
    return True  # Change to False for testing

def evade_sentinals():
    print("Attempting to evade sentinels...")
    return True