from os import path
from random import choice
from time import time
from string import ascii_uppercase
from asyncio import async, get_event_loop, coroutine

__author__ = 'Owain van Brakel'
__class__ = 'Bin1f'
__student__ = 'S1094204'
__email__ = 'S1094204@hsleiden.nl'


class Coroutines:
    @staticmethod
    @coroutine
    def open_file(file: str, mode: str = 'r') -> any:
        """
        Open a file in a given mode

        :param file: Filename
        :param mode: Mode to open the file (r/w/a)

        :return: Opened file
        """
        return open(file, mode)

    @staticmethod
    @coroutine
    def close_file(file: any) -> None:
        """
        Close an opened file

        :param file: File name

        :return: None
        """
        file.close()

    @staticmethod
    @coroutine
    def read_data(file: any) -> str:
        """
        Read the contents of a file

        :param file: Opened file

        :return: Contents of the file
        """
        loop = get_event_loop()
        data = yield from loop.run_in_executor(None, file.read)

        return data

    @staticmethod
    @coroutine
    def write_data(file: any, data: str) -> None:
        """
        Write data to a file

        :param file: Opened file
        :param data: Data to write

        :return: None
        """
        print(data, file=file)


class StringManipulation:
    @staticmethod
    def strip_special_chars(word: str) -> str:
        """
        Strip all non alphabetical characters from a string

        :param word: Input string

        :return: Stripped string
        """
        return ''.join([i for i in word if i.isalpha()]).lower()

    @staticmethod
    def check_word_length(word: str, min_length: int, max_length: int)\
            -> bool:
        """
        Check if a given word is between a given minimum and maximum
        length
        All non alphabetical characters will be stripped prior to the
        check

        :param word: Word to check
        :param min_length: Minimum length
        :param max_length: Maximum length

        :return: True if the word is between the minimum and maximum
        false otherwise
        """
        return min_length <= len(StringManipulation.
                                 strip_special_chars(word)) <= max_length


class WordList:
    def __init__(self, current_path: str, file_name: str) -> None:
        """
        Initialization of the WordList class

        :param current_path: Path where the script is executed
        :param file_name: Filename of the file which contains all the
        words

        :return: None
        """
        self.file = current_path + file_name
        self.all_words = []

        if not path.isfile(self.file):
            # Throw an error if the file doesn't exist
            raise RuntimeError('Het woordenlijst bestand '
                               'bestaat niet! (woorden.lst)')

        loop = get_event_loop()
        loop.call_soon(async, self.get_all_words(self.file, loop))
        loop.run_forever()  # Run until stopped

    @staticmethod
    @coroutine
    def save_list(file: str, data: list, loop: any) -> None:
        """
        Save the new list to a file

        :param file: Filename of the file which contains all the words
        :param data: New list with words
        :param loop: Current event loop

        :return: None
        """
        file = yield from async(Coroutines.open_file(file, 'w'))
        yield from async(Coroutines.write_data(file, '\n'.join(
            map(str, data))))
        yield from async(Coroutines.close_file(file))

        loop.stop()

    @coroutine
    def get_all_words(self, filename: str, loop: any) -> None:
        """
        The main coroutine will get all the words from the word list

        :param filename: Filename of the file which contains all the
        words
        :param loop: Current event loop

        :return: None
        """
        file = yield from async(Coroutines.open_file(filename))
        data = yield from async(Coroutines.read_data(file))
        yield from async(Coroutines.close_file(file))

        self.all_words = data.split()

        loop.stop()

    def display_all_words(self) -> list:
        """
        Print all words

        :return: All the words
        """
        return self.all_words

    def check_word_exist(self, word: str) -> bool:
        """
        Check if a given word is already present in the word list

        :param word: Word to check

        :return: True if the word already exists false otherwise
        """
        return word in self.all_words

    def sort_list(self) -> None:
        """
        Sort list by length and alphabetical order

        :return: Sorted list
        """
        self.all_words.sort(key=lambda item: (len(item), item))

    def add_word_to_list(self, word: str) -> bool:
        """
        Add a new word to the word list

        :param word: Word to add

        :return: True if the word has been added false otherwise
        """
        word = StringManipulation.strip_special_chars(word)

        if self.check_word_exist(word):
            return False
        else:
            self.all_words.append(word)
            self.sort_list()

            loop = get_event_loop()
            loop.call_soon(async,
                           self.save_list(self.file, self.all_words, loop))
            loop.run_forever()  # Run until stopped

            return True

    def random_word(self) -> str:
        """
        Get a random word from the word list

        :return: Random word
        """
        return choice(self.all_words)


class Hangman:
    GALLOW = [
        '         ;         ;         ;         ;         ;         ',
        '         ;  |      ;  |      ;  |      ;  |      ; / \     ',
        '   ____  ;  |/     ;  |      ;  |      ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |      ;  |      ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |    O ;  |      ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |    O ;  |    | ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |   \O ;  |    | ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |   \O/;  |    | ;  |      ; / \     ',
        '   ____  ;  |/   | ;  |   \O/;  |    | ;  |   /  ; / \     ',
        '   ____  ;  |/   | ;  |   \O/;  |    | ;  |   / \; / \     '
    ]

    def __init__(self, generated_word: str) -> None:
        """
        Initialization of the Hangman class

        :param generated_word: Randomly generated word

        :return: None
        """
        self.current_word = generated_word.upper()
        self.guesses = []
        self.faults = 0
        self.force_guessed = False

    @staticmethod
    def stars_or_chars(guesses: list, word: str = '', asc: str = '*') -> any:
        """
        Return a star or a character for each character in a string or
        a list

        If the param word is given the function will replace the
        characters in the word with param asc if the original character
        hasn't been guessed yet

        If the param word is not given the function will return every
        character from the alphabet replaced with param asc if the
        original character hasn't been guessed yet

        :param guesses: List with all the guessed characters
        :param word: Randomly generated word (optional)
        :param asc: Character that will replace the original character
        (optional)

        :return: String or list with param asc instead of characters
        that haven't been guessed
        """
        if word:
            new_word = ''

            for i in word:
                if i not in guesses:
                    i = asc

                new_word += i

            return ' '.join(new_word)

        chars = []

        for i in ascii_uppercase:
            if i in guesses:
                chars.append(i)
            else:
                chars.append(asc)

        return chars

    @staticmethod
    def print_gallow_and_chars(guesses: list, generated_word: str,
                               faults: int) -> str:
        """
        Give back a formatted string of the gallow the alphabet and the
        current word

        :param guesses: List with all the guesses
        :param generated_word: Randomly generated word
        :param faults: Amounts of faults

        :return: Formatted string
        """
        chars = Hangman.stars_or_chars(guesses)
        word = Hangman.stars_or_chars(guesses, generated_word)

        chars = [' '.join(chars[:9]),
                 ' '.join(chars[9:18]),
                 ' '.join(chars[18:26])]

        current_gallow = Hangman.GALLOW[faults].split(';')

        # PEP 8 readability...
        return '{:>8} {:>67}\n' \
               '{:>9} {:>66}\n' \
               '{:>9}\n' \
               '{:>9} {:>66}\n' \
               '{:>9}\n' \
               '{:>9} {:>65}\n' \
               '{:>9}\n\n' \
               '{:>47}\n' \
               '{}\n\n' \
            .format('Galgje:', 'Gebruikte letters',
                    current_gallow[0], chars[0],
                    current_gallow[1],
                    current_gallow[2], chars[1],
                    current_gallow[3],
                    current_gallow[4], chars[2],
                    current_gallow[5],
                    'Het te raden woord:',
                    (' ' * (37 - int(len(word) / 2))) + word)

    def get_current_word(self) -> str:
        """
        Return the randomly generated word

        :return: Randomly generated word
        """
        return self.current_word

    def new_guess(self, inp: str) -> bool:
        """
        Check if the input (word or single character) is correct
        otherwise the amount of faults will be increased

        :param inp: Player's input

        :return: None
        """
        inp = StringManipulation.strip_special_chars(inp).upper()

        if len(inp) == 0:
            return False
        elif len(inp) == 1:
            if inp not in self.guesses:
                self.guesses.append(inp)

                if inp not in self.current_word:
                    self.faults += 1
            else:
                if inp not in self.current_word:
                    self.faults += 1

            return True
        else:
            if inp != self.current_word.upper():
                self.faults += 3

                if self.faults > 9:
                    self.faults = 9
            else:
                self.force_guessed = True
                for i in inp:
                    self.guesses.append(i)

            return True

    def check_guessed(self) -> bool:
        """
        Check if the word has been guessed already

        :return: True if the word has been guessed (forced or character
        by character) false otherwise
        """
        if self.force_guessed:
            return True

        for i in self.current_word:
            if i not in self.guesses:
                return False

        return True


class HighScore:
    def __init__(self, current_path: str, file_name: str) -> None:
        """
        Initialization of the HighScore class

        :param current_path: Path where the script is executed
        :param file_name: Filename of the file that contains the high
        scores

        :return: None
        """
        self.start_time = 0
        self.file = current_path + file_name
        self.all_scores = []

        if not path.isfile(self.file):
            # Throw an error if the file doesn't exist
            raise RuntimeError('Het scorebord bestand '
                               'bestaat niet! (ranking.txt)')

        loop = get_event_loop()
        loop.call_soon(async, self.get_all_scores(self.file, loop))
        loop.run_forever()  # Run until stopped

    @staticmethod
    def sort_by(x: list) -> any:
        """
        Cast string to int (if the cast fails use infinity)

        :param x: List

        :return: List with an int or float instead of a string
        """
        try:
            return int(x[5])
        except ValueError:
            return float('inf')

    @staticmethod
    def add_position(scores: list) -> list:
        """
        Add the positions to the high score list

        :param scores: All high scores

        :return: All high scores with positions
        """
        for i in range(0, 11):
            if i > 0:
                scores[i][0] = i

        return scores

    @staticmethod
    def convert_high_score(scores: list) -> str:
        """
        Convert the high scores from nested lists to a string

        :param scores: All high scores

        :return: String formatted high scores
        """
        scores = HighScore.add_position(scores)
        string = ''

        for i in scores:
            for j in i:
                string += str(j) + ';'
            string = string[:-1]
            string += '\n'

        return string

    @staticmethod
    def get_score(word_length: int, tries: int, seconds: int) -> int:
        """
        Calculate the players score

        :param word_length: The length of the randomly generated word
        :param tries: Amount of tries before the word was guessed
        :param seconds: Amount of time spend before the word was
        guessed in seconds

        :return: Calculated score
        """
        score = 10000 * (word_length / ((seconds * tries) + 1))

        return int(score)

    @coroutine
    def convert_to_lists(self, data: str) -> None:
        """
        Convert the content of the high score file to nested lists so
        it's easier to work with

        :param data: Contents of the high score file

        :return: None
        """
        for i in data.split():
            self.all_scores.append(i.split(';'))

        self.sort_high_score_list()

    @coroutine
    def get_all_scores(self, filename: str, loop: any) -> None:
        """
        Get all the scores from the high score file

        :param filename: Filename of the file which contains all the scores
        :param loop: Current event loop

        :return: None
        """

        file = yield from async(Coroutines.open_file(filename))
        data = yield from async(Coroutines.read_data(file))
        yield from async(self.convert_to_lists(data))
        yield from async(Coroutines.close_file(file))

        loop.stop()

    @coroutine
    def save_high_score(self, loop: any) -> None:
        """
        Save the new high score list to a given file

        :param loop: Current event loop

        :return: None
        """
        string = self.convert_high_score(self.all_scores)

        file = yield from async(Coroutines.open_file(self.file, 'w'))
        yield from async(Coroutines.write_data(file, string))
        yield from async(Coroutines.close_file(file))

        loop.stop()

    def begin_timer(self) -> None:
        """
        Save the (epoch) time when the game starts

        :return: None
        """
        self.start_time = time()

    def end_timer(self) -> int:
        """
        Save the (epoch) time when the game ends and calculate the
        difference between the end time end the start time

        :return: Difference between the start time and the end time in
        seconds
        """
        end_time = time()

        return round(end_time - self.start_time)

    def show_all_scores(self) -> str:
        """
        Return an overview of all the scores in the high score list

        :return: A formatted overview of all the scores
        """
        string = ''
        count = 0
        for i in self.all_scores:
            string += '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}\n'.format(
                [i[0], count][count > 0], i[1], i[2], i[3], i[4], i[5])
            count += 1

        return string

    def sort_high_score_list(self) -> None:
        """
        Sort the high score list based on the obtained scores

        :return: None
         """
        self.all_scores.sort(key=HighScore.sort_by, reverse=True)

    def add_high_score(self, name: str, length: int,
                       tries: int, seconds: str, score: int) -> None:
        """
        Add a new score to the high scores

        :param name: Name of the player
        :param length: Length of the word
        :param tries: Amount of tries before the word was guessed
        :param seconds: Time spend in game (format XmXs)
        :param score: Obtained score

        :return: None
        """
        self.all_scores.append(['x', name, length, tries, seconds, score])
        self.sort_high_score_list()
        self.all_scores = self.all_scores[:-1]

        loop = get_event_loop()
        loop.call_soon(async, self.save_high_score(loop))
        loop.run_forever()  # Run until stopped

    def check_high_score(self, score: int) -> tuple:
        """
        Check if the score is one of the top 10 scores

        :param score: Obtained score

        :return: True and the placement if the score is high enough
        false otherwise
        """
        for i in range(1, 11):
            if score > int(self.all_scores[i][5]):
                return True, i

        return False, 0


def main() -> None:
    running = True

    try:
        word_list = WordList(path.dirname(path.abspath(__file__)) + "/",
                             'woorden.lst')
        high_score = HighScore(path.dirname(path.abspath(__file__)) + "/",
                               'ranking.txt')
    except RuntimeError as err:
        print(err)
        exit()

    while running:
        print('1. Een woord toevoegen\n'
              '2. Het spel spelen\n'
              '3. De ranking bekijken\n'
              '4. Student\n'
              '5. Stoppen')

        inp = input('\nWat wil je doen? [1 - 5]\n')

        if inp not in '12345' and not len(inp) == 1:
            print('Dit is geen geldige invoer, probeer opnieuw!')

        # <editor-fold desc="Add word">
        elif inp == '1':
            inp = input('Voer een woord in die je wilt '
                        'toevoegen aan de woordenlijst:\n')

            if StringManipulation.check_word_length(inp, 3, 38):
                if word_list.add_word_to_list(inp):
                    print('Het woord {} is toegevoegd aan de woordenlijst!\n'
                          .format(StringManipulation.
                                  strip_special_chars(inp)))

                else:
                    print('Het woord {} staat al in de woordenlijst!\n'
                          .format(StringManipulation.
                                  strip_special_chars(inp)))

            else:
                print('Het woord moet minstens 3 letters lang '
                      'zijn en maximaal 38 letters lang!')
        # </editor-fold>

        # <editor-fold desc="Hangman">
        elif inp == '2':
            name = ''

            while name == '':
                name = StringManipulation.strip_special_chars(
                    input('Wat is je naam?\n'))
                continue

            word = word_list.random_word()
            hangman = Hangman(word)
            high_score.begin_timer()
            game_running = True

            while hangman.faults <= 9 and game_running:
                # Python can't clear its own output (best scripting language
                # ever...) so printing a bunch of new lines is the only way
                print('\n' * 250)
                
                print(Hangman.print_gallow_and_chars(hangman.guesses,
                                                     hangman.current_word,
                                                     hangman.faults))

                if hangman.faults == 9:
                    # Stop the game
                    game_running = False

                    print('Helaas, je hebt het woord niet geraden. '
                          'Het woord was {}\n'.format(hangman.current_word.
                                                      lower()))

                elif hangman.check_guessed():
                    # Stop the game
                    game_running = False
                    seconds = high_score.end_timer()
                    score = high_score.get_score(len(hangman.current_word),
                                                 hangman.faults, seconds)

                    check_highscore = high_score.check_high_score(score)

                    print('Je hebt het geraden! Het woord was {}\n\n'
                          'Je hebt {} punten gescoord\n'
                          .format(hangman.current_word.lower(), score))

                    if check_highscore[0]:
                        print('Daarmee kom je op plaats {} '
                              'in de ranking!\n'
                              .format(check_highscore[1]))

                        # Convert the total amount of seconds to
                        # minutes and seconds
                        m, s = divmod(seconds, 60)

                        # PEP 8 readability...
                        high_score.add_high_score(name,
                                                  len(hangman.current_word),
                                                  hangman.faults,
                                                  '{}m{}s'
                                                  .format(m, s),
                                                  score)

                        print('\n' + high_score.show_all_scores())

                else:
                    while True:
                        if not hangman.new_guess(
                                input('Typ een letter of het woord:\n')):
                            print(
                                'Dit is geen geldige invoer probeer opnieuw!')
                        else:
                            break
        # </editor-fold>

        # <editor-fold desc="Highscores">
        elif inp == '3':

            print('\n' + high_score.show_all_scores())
        # </editor-fold>

        # <editor-fold desc="Student">
        elif inp == '4':

            print(__author__ + '\n' +
                  __student__ + '\n' +
                  __class__ + '\n' +
                  __email__ + '\n')

        # </editor-fold>

        # <editor-fold desc="Exit">
        elif inp == '5':

            running = False
        # </editor-fold>


if __name__ == "__main__":
    main()
