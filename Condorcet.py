fname = 'CSCI364_VotingGameDay_Votes.csv'
file = open(fname, 'r')

movies = []
rankingDict = {}

for i, line in enumerate(file):
    if i == 0:
        for movie in line.split(","):
            movies.append(movie)
    else:
        rankings = line.split(',')
        for i, rank in enumerate(rank):


file.close()