def wordFrequencyCounter():
    print("=== Word Frequency Counter ===")
    text = input("Enter a paragraph: ")
    
    if not text.strip():
        print("Friendly message: Empty string provided. Please enter a valid paragraph next time.")
        return

    text_lower = text.lower()
    cleaned_chars = []
    for char in text_lower:
        if char.isalnum() or char.isspace():
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(" ")  
            
    cleaned_text = "".join(cleaned_chars)
    words = cleaned_text.split()
    
    if not words:
        print("Friendly message: No valid words found after cleaning.")
        return

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\n--- Word Counts ---")
    for word, count in word_counts.items():
        print(f"{word} = {count}")

    try:
        n = int(input("\nEnter N for top words to display: "))
    except ValueError:
        n = 3  # Default fallback if input is invalid
        print("Invalid input. Defaulting N to 3.")

    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    top_n = sorted_words[:n]
    
    print(f"Top {n} Words:")
    for word, count in top_n:
        print(f"- {word} ({count})")

    once_words = sorted([word for word, count in word_counts.items() if count == 1])
    print("\nWords Appearing Exactly Once:")
    if once_words:
        print(", ".join(once_words))
    else:
        print("None")

    inverted = {}
    for word, freq in word_counts.items():
        inverted.setdefault(freq, []).append(word)
    
    for freq in inverted:
        inverted[freq].sort()

    print("\nInverted Dictionary ({frequency: [words]}):")
    print(inverted)

    by_length = {}
    for word in word_counts.keys():  # unique words from keys
        length = len(word)
        by_length.setdefault(length, []).append(word)
        
    for length in by_length:
        by_length[length].sort()

    print("\nGrouped by Length ({length: [unique words]}):")
    print(by_length)

    print("\n--- Word Search ---")
    search_query = input("Enter a word to search: ").strip().lower()

    search_query = "".join([c for c in search_query if c.isalnum()])
    
    count = word_counts.get(search_query, 0)
    if count > 0:
        print(f"Result: '{search_query}' appears {count} time(s).")
    else:
        print(f"Result: '{search_query}' not found.")

if __name__ == "__main__":
    wordFrequencyCounter()