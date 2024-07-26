import sys

#Парсинг рядку логів у словник
def parse_log_line(line):
    parts = line.split(' ')

    if len(parts) < 4:
        print("Line is in wrong format")
        return {}

    return {
        "date" : parts[0],
        "time" : parts[1],
        "level" : parts[2],
        #Повідомлення може також містити пробіли
        "message" : ' '.join(parts[3:])
    }

#Зчитування файлу логів за шляхом у список словників
def load_logs(file_path):
    try:
        file = open(file_path, 'r')
        return [parse_log_line(line.strip()) for line in file]
    except Exception as ex:
        print('Помилка при зчитуванні файлу логів')
        print(ex)
        return []

#Фільтрування логів за рівнем
def filter_logs_by_level(logs, level):
    return filter(lambda x: x['level'] == level, logs)

#Підрахунок кількості логів за кожним рівнем
def count_logs_by_level(logs):
    counts = {}
    
    for item in logs:
        if item['level'] in counts:
            counts[item['level']] += 1
        else:
            counts[item['level']] = 1

    return counts

#Виведення кількості логів за кожним рівнем в консоль
def display_log_counts(counts):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for key, value in counts.items():
        print(key + ' '*(17-len(key)) + f'| {value}')

#Виведення логів певного рівня в консоль
def display_log(logs, level):
    filtered_logs = filter_logs_by_level(logs, level)
    print()
    print(f"Деталі логів для рівня '{level}':")
    for item in filtered_logs:
        print(f"{item['date']} {item['time']} - {item['message']}")

if len(sys.argv) < 2:
    print("There is no path argument")
    exit()

path = sys.argv[1]
logs = load_logs(path)
counts = count_logs_by_level(logs)
display_log_counts(counts)

if len(sys.argv) > 2:
    display_log(logs, sys.argv[2].upper())
