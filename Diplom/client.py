import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту predict с параметром json
    LAT = float(input('Введите широту: '))
    LNG = float(input('Введите долготу: '))
    year_built = int(input('Введите год постройки дома: '))
    sqft = float(input('Введите общую площадь дома: '))
    stories = int(input('Введите этажность дома: '))
    beds = int(input('Введите количество спален: '))
    baths = float(input('Введите количество ванных: '))
    lotsize = float(input('Введите площадь участка: '))
    mean_school_rating = float(input('Введите средний рейтинг ближайших школ: '))
    mean_school_distance = float(input('Введите среднее расстояние до ближайших школ: '))

    r = requests.post('http://localhost:5000/predict', json=[LNG, sqft, LAT, year_built, 
                                                             mean_school_rating, baths, stories, lotsize,
                                                             beds, mean_school_distance])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)