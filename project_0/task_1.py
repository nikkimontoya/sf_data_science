from game_v2 import score_game


def bisect_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_boundary = 1
    max_boundary = 101
    while True:
        predict_number = min_boundary + (max_boundary - min_boundary)//2  # предполагаемое число
        count += 1        
        
        if number > predict_number:
            min_boundary = predict_number
        elif number < predict_number:
            max_boundary = predict_number
        else:
            break
        
    return count


if __name__ == "__main__":
    # RUN
    score_game(bisect_predict)
