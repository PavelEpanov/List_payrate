def main():

    NUM_PLAYERS = 6

    pay = 67.50
    salary = []

    hours = [0] * NUM_PLAYERS
    index = 0
    for job in hours:
        hours[index] = int(input(f"Введите часы для {index+1} рабочего: "))
        index += 1

    salary_index = 0

    for line in hours:
        salary.append(hours[salary_index] * pay)
        salary_index += 1

    index_for = 0

    for pays in salary:
        print(pays)


main()
