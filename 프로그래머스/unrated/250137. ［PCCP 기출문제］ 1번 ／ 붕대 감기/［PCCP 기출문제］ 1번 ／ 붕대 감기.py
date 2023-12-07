def solution(bandage, health, attacks):
    answer = health
    timer = 0
    attack_num = 0

    for i in range(attacks[-1][0] + 1):

        
        if attacks[attack_num][0] == i:
            answer -= attacks[attack_num][1]
            attack_num += 1
            timer = 0
        elif timer + 1 == bandage[0]:
             timer = 0
             answer += bandage[2] + bandage[1]
        else:
            answer += bandage[1]
            timer += 1

        if answer > health: answer = health       
        if answer <= 0: return -1
        
            
    return answer