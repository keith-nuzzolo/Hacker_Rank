'''
You are given a list of N people who are attending ACM-ICPC World Finals.
Each of them are either well versed in a topic or they are not.
Find out the maximum number of topics a 2-person team can know.
And also find out how many teams can know that maximum number of topics.

Output Format

On the first line,
print the maximum number of topics a 2-person team can know.
On the second line,
print the number of 2-person teams that can know the maximum number of topics.
Sample Input:
4 5
10101
11100
11010
00101

Sample Output:
5
2
9.8276 original time
v2 = 5.9366
v3 = .526
'''
def create_team(team_length):
    '''
    Creates a team with the given inputs and returns the team as a list
    '''
    return [input() for i in range(team_length)]


def subjects(member1, member2):
    '''
    Returns the number of subjects a two member input can know
    '''

    return bin(int(member1,2)|int(member2,2))

def max_subjects(team):
    '''
    Returns the maximum number of topics that one team can know
    '''
    maximum_topics = bin(0)
    position = 0
    for member in team:
        position += 1
        for second_member in team[position:]:
            s = subjects(member, second_member)
            if s.count('1') > maximum_topics.count('1'):
                maximum_topics = s
    return maximum_topics

def pairs(team, max_t):
    '''
    Takes in the maximum number of topics and a list of team members and
    returns how many pairs can achieve that number of topics    
    '''
    number_of_pairs = 0
    position = 0
    for member in team:
        position += 1
        for second_member in team[position:]:
            if subjects(member, second_member).count('1') == max_t.count('1'):
                number_of_pairs += 1
    return number_of_pairs

def icpc_team():
    '''
    takes in the number of teams and their length and then builds the topics
    known by each member, and returns the maximum number of topics one pair can
    know and the number of pairs that can acieve that number of topics
    '''
    team_dynamics = input().strip().split(' ')
    team = create_team(int(team_dynamics[0]))
    print(max_subjects(team).count('1'))
    print(pairs(team, max_subjects(team)))
icpc_team()
