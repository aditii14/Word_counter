def count_words(sentence):
   
    
    # Check if the input sentence is empty
    if not sentence:
        return 0
    
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    
    # Return the number of words in the sentence
    return len(words)

def main():
   
    print("Welcome to the Word Counter!")
    
    # Prompt the user to enter a sentence or paragraph
    sentence = input("Please enter a sentence or paragraph: ")
    
    # Count the number of words in the input
    word_count = count_words(sentence)
    
    # Display the word count to the user
    print(f"\nThe number of words in the input is: {word_count}")

if __name__ == "__main__":
    main()
