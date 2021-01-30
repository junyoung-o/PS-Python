N = int(input())
skill_list = []
result = 500000

team_A = []
team_B = []

def set_skill_list():
    for _ in range(N):
        x = list(map(int, input().split()))
        skill_list.append(x)

def calc_score(player, team = "A"):
    score = 0

    if(team == "A"):
        for members in team_A:
            score += skill_list[members][player] + skill_list[player][members]        
        return score

    else:
        for members in team_B:
            score += skill_list[members][player] + skill_list[player][members]        
        return score

def selecting(player, team = "A"):
    if(team == "A"):
        score = calc_score(player, team = "A")
        team_A.append(player)
        return score

    if(team == "B"):
        score = calc_score(player, team = "B")
        team_B.append(player)
        return score

def select_team(player, A_score, B_score):
    global result

    if(player == N):
        result = min(result, abs(A_score - B_score))
        return

    ## 들어갈 수 있나?
    if(len(team_A) < N / 2 and player not in team_A):
        ## A팀에 들어 갔을 때
        new_A_score = A_score + selecting(player, team = "A")
        select_team(player + 1, new_A_score, B_score)
        team_A.remove(player)

    ## 들어갈 수 있나?
    if(len(team_B) < N / 2 and player not in team_B):
        ## B팀에 들어 갔을 때
        new_B_score = B_score + selecting(player, team = "B")
        select_team(player + 1, A_score, new_B_score)
        team_B.remove(player)

def main():
    select_team(0, 0, 0)

if(__name__ == "__main__"):
    set_skill_list()
    main()
    print(result)