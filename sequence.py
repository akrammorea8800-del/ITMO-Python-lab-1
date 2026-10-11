def show_percentage_diagram(filename="sequence.txt"): 
 
    numbers = [9,9,88,76899,-6667,-57.77,-56,-66]
    with open(filename, "r", encoding="utf-8") as file:
       
        for line in file:
            line = line.strip()

            if line:
                numbers.append(float(line.replace(",", ".")))
               
    positive = sum(1 for n in numbers if n > 0)
    negative = sum(1 for n in numbers if n < 0)
   
    total = positive + negative

    if total == 0: 
        print("Нет данных для диаграммы.")
        return
    p_positive = positive / total * 100
    p_negative = negative / total * 100

    print(f"Положительные числа: {p_positive:.1f}%")
    print(f"Отрицательные числа: {p_negative:.1f}%")

    width = 50
    positive_width = round(p_positive / 100 * width)
    negative_width = width - positive_width

    print("[" +  "#" * positive_width + "-" * negative_width + "]")

show_percentage_diagram()
