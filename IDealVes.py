def calculate_bmi(weight, height):
    return weight / (height ** 2)

def optimal_weight(height):
    # Идеальный ИМТ находится в диапазоне от 18.5 до 24.9
    lower_bound = 18.5
    upper_bound = 24.9

    # Вычисляем оптимальную массу тела для данного роста
    lower_weight = lower_bound * (height ** 2)
    upper_weight = upper_bound * (height ** 2)

    return lower_weight, upper_weight

def main():
    height = float(input("Введите ваш рост в метрах: "))
    
    lower_weight, upper_weight = optimal_weight(height)
    print(f"Оптимальная масса тела для роста {height} м:")
    print(f"Минимальная: {lower_weight:.2f} кг")
    print(f"Максимальная: {upper_weight:.2f} кг")

if __name__ == "__main__":
    main()
