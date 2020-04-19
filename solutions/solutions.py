from string import punctuation


def parser_lyrics(lyrics):
    lyrics = lyrics.replace("\n", " ").lower()
    for p in punctuation:
        lyrics = lyrics.replace(p, "")
    return lyrics.split(" ")


def section1_partA(lyrics):
    lyrics_list = parser_lyrics(lyrics)
    word_counter = {}
    for word in lyrics_list:
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter


def section1_partB(lyrics):
    word_counter = section1_partA(lyrics)
    word_count_tuples = list(word_counter.items())
    word_count_tuples = sorted(word_count_tuples, key=lambda x: x[1])
    return word_count_tuples[-1][0]



def section2_partA(lyrics):
    word_counter = section1_partA(lyrics)
    word_counts = list(word_counter.values())
    return sum(word_counts)/len(word_counts)



def section2_partB(lyrics):
    word_counter = section1_partA(lyrics)
    mu = section2_partA(lyrics)
    squared_diffs = [(v-mu)**2 for v in word_counter.values()]
    return (sum(squared_diffs)/len(squared_diffs))**0.5


def section3_partA(lst):
    odds = [n for n in lst if n%2==1]
    return sum(map(lambda x: 3*x + 1, odds))


def section3_partB(numbers, divisors):
    s = ""
    for number in numbers:
        if any(number%d==0 for d in divisors):
            s += str(number)
    return s



def levelUp_partA(n):
    d = 2
    while True:
        if d >= n**0.5:
            break
        if n%d==0:
            return False
        d += 1
    return True


def levelUp_partB(lst1, lst2):
    s = set()
    for i in lst1:
        if i in lst2:
            s.add(i)
    return s


levelUp_partC = lambda lst: max(lst) - min(lst)