#             Search Engine
# you are given few sentenaces as a list ( python list of sentences ). Take a query string as an
# input from the user. you have to pull out the sentences in matchng a query inputted by the user
# in decreasing order of the relevance after converting every word in the query to lower case. Most
# relevant sentencec is teh one with the maximum number of matching words with the query.
#
# sentences = ["This is good", "python is good", "python is not python snake"]
#
# Input :
# please input your query string
# "python"
#
# Output:
# 3 results found :
#             1. python is not python snake
#             2. python is good
#             3. this is good




def matchingwords(sentence1, sentence2):
    # returns number of matching words in sentence1 and sentence2
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2} ")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    # print(matchingwords("This is good","python is good"))
    sentences = [" good python is good", "this is a python snake", "Pankaj is a good boy",
                 "Subscribe to this good python youtube channel"]

    query = input("Please enter query string \n ")
    scores = [matchingwords(query, sentence) for sentence in sentences]
    # print(scores)
    # zip a = [1,2,3]
    # b = [3,4,5]
    # zip(a,b) = [(1,3),(2,4),(3,5)]
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences),reverse = True)]
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found! \n")
    for score, item in sortedSentScore:
        print(f"\"{item}\" : with a score of {score}")
