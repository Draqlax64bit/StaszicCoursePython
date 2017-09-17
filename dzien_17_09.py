def pollution(part_name):
    with open('2016_PM2.5_1g.csv', 'r') as file:
        lines = file.read().splitlines()
        column_number = -1
        column_list = []
        for name in lines[1].split(';'):
            column_number += 1
            if part_name in name:
                column_list.append(column_number)
        if len(column_list) == 0:
            return 'City not found'
        name_list = []
        names = lines[1].split(';')
        for column_number in column_list:
            name_list.append(names[column_number])

        sum_list = []
        for column_number in column_list:
            sum = 0  # licznik
            counter = 0  # mianownik
            for line in lines[6:]:
                value = line.split(';')[column_number]
                if value is not '':
                    counter += 1
                    sum += float(value.replace(',', '.'))
            sum_list.append(sum / counter)
        result = {}
        for index, _ in enumerate(column_list):
            result.update({name_list[index]: sum_list[index]})
        return result


print(pollution('Kato'))
