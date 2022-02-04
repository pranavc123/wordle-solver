class wordleSolver:
    def __init__(self):
        self.words = []
        self.solved = False

        #read in words
        lines = open("wordlist.txt", "r").readlines()
        for line in lines:
            self.words.append(line[:len(line) - 1])
        self.words[-1] += 'l'

    def solve(self):
        banned = set() #no words can have these characters
        must_contain = set() #all words must have these characters
        contain_order = {} #all words must have these characters in these positions
        ban_order = {} #all words must not have these characters in these positions
        remove = set() #words to remove from the full set of words

        while not self.solved:
            guessed_word = input("What word did you input? ")
            given_hints = input("What hints were you given? (Black = 0, Yellow = 1, Green = 2): ")

            for i in range(5):
                if given_hints[i] == '0':
                    banned.add(guessed_word[i])
                elif given_hints[i] == '1':
                    must_contain.add(guessed_word[i])
                    ban_order[i] = guessed_word[i]
                else:
                    contain_order[i] = guessed_word[i]
        
            #filter out ban list, then contained list, then correct
            for word in self.words:

                #if the word contains a letter in the ban list, remove it
                x = [c for c in word if (c in banned)]
                if len(x) != 0:
                    remove.add(word)

                #if the word does not contain every letter in the contained list, remove it
                for char in must_contain:
                    if char not in word:
                        remove.add(word)
                for key, value in contain_order.items():
                    if word[key] != value:
                        remove.add(word)
                for key,value in  ban_order.items():
                    if word[key] == value:
                        remove.add(word)
            
            if input("Did you solve the wordle already? (y/n)") == "y":
                self.solved = True
            self.words = [www for www in self.words if(www not in remove)]
            print('possible words: ')
            print(self.words)

if __name__ == '__main__':
    wordle_ = wordleSolver()
    wordle_.solve()