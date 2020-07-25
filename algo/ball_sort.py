def sort_balls(balls):
    red, yellow, blue = 0, 0, len(balls) - 1
    while yellow <= blue:
        if balls[yellow] == 1:
            yellow += 1
        elif balls[yellow] == 0:
            balls[red], balls[yellow] = balls[yellow], balls[red]
            red += 1
            yellow = max(yellow, red)
        else:
            balls[blue], balls[yellow] = balls[yellow], balls[blue]
            blue -= 1


a = [2, 2, 0, 2, 2, 2, 1, 1]
sort_balls(a)
print(a)
