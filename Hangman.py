def hangman():
    solution = False
    m = 0
    n = ''
    r = False
    s = 5
    secret_word = input("Type in a word and someone else will try to guess it.").upper()
    secret_word_2 = secret_word.replace('', ' ')
    secret_word_2 = secret_word_2[1: -1]
    m = len(secret_word)
    n = ' '.join('_' * m)
    print(n)
    n = list(n)
    t = [w.replace(' ', '') for w in n]
    n[0] = secret_word[0]
    while not solution:
        print("".join(n))
        o = input().upper()
        for p in range(1, m):
            if o == secret_word[p]:
                n[p*2] = secret_word[p]
                r = True
        if not r:
            s -= 1
            if s == 0:
                print("You lost.")
                solution = True
            else:
                print("You have %s more guesses. " % s)
        r = False
        t = [w.replace(' ', '') for w in n]
        if str("".join(t)) == secret_word:
            print("".join(n))
            print("Congrats! You guessed the word!")
            solution = True
hangman()
