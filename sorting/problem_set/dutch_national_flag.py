def dutch_national_flag(balls):
    l = 0
    r = len(balls) - 1
    i = 0

    def swap(i, j):
        balls[i], balls[j] = balls[j], balls[i]
        
    while i < r:
        if balls[i] == 'R':
            swap(i, l)
            l += 1
          
        if balls[i] == 'B':
            swap(i, r)
            r -= 1
      
        if balls[r] == 'R':
            swap(r, l)
            l += 1


        i += 1

    return balls
    
a = ["G", "B", "G", "G", "R", "B", "R", "G"]
# ["R", "R", "G", "G", "G", "G", "B", "B"]

print(dutch_national_flag(a))