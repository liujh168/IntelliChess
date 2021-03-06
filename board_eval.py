# eval info for Chinese Chess by Fei Li

strength = {
    'Shuai': 100000,
    'Shi': 120,
    'Xiang': 120,
    'Che': 620,
    'Ma': 260,
    'Pao': 380,
    'Bing': 30
}

position = {
    'Shuai': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [-2, -4, -6, 0, 0, 0, 0, 0, 0, 0],
              [0, -2, -4, 0, 0, 0, 0, 0, 0, 0],
              [-2, -4, -6, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

    'Shi': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -4, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -4, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

    'Xiang': [[0, 0, -4, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -4, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, -4, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, -4, 0, 0, 0, 0, 0, 0, 0]],

    'Che': [[-2, 8, 4, 6, 12, 12, 12, 12, 16, 14],
            [10, 4, 8, 10, 16, 14, 18, 12, 20, 14],
            [6, 8, 6, 8, 14, 12, 16, 12, 18, 12],
            [14, 16, 14, 14, 20, 18, 22, 18, 24, 18],
            [12, 8, 12, 14, 20, 18, 22, 18, 26, 16],
            [14, 16, 14, 14, 20, 18, 22, 18, 24, 18],
            [6, 8, 6, 8, 14, 12, 16, 12, 18, 12],
            [10, 4, 8, 10, 16, 14, 18, 12, 20, 14],
            [-2, 8, 4, 6, 12, 12, 12, 12, 16, 14]],

    'Ma': [[0, 0, 4, 2, 4, 6, 8, 12, 4, 4],
           [-4, 2, 2, 6, 12, 16, 24, 14, 10, 8],
           [0, 4, 8, 8, 16, 14, 18, 16, 28, 16],
           [0, 4, 8, 6, 14, 18, 24, 20, 16, 12],
           [0, -2, 4, 10, 12, 16, 20, 18, 8, 4],
           [0, 4, 8, 6, 14, 18, 24, 20, 16, 12],
           [0, 4, 8, 8, 16, 14, 18, 16, 28, 16],
           [-4, 2, 2, 6, 12, 16, 24, 14, 10, 8],
           [0, 0, 4, 2, 4, 6, 8, 12, 4, 4]],

    'Pao': [[0, 0, 4, 0, -2, 0, 0, 2, 2, 6],
            [0, 2, 0, 0, 0, 0, 0, 2, 2, 4],
            [2, 4, 8, 0, 4, 0, -2, 0, 0, 0],
            [6, 6, 6, 2, 2, 2, 4, -10, -4, -10],
            [6, 6, 10, 4, 6, 8, 10, -8, -14, -12],
            [6, 6, 6, 2, 2, 2, 4, -10, -4, -10],
            [2, 4, 8, 0, 4, 0, -2, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 2, 2, 4],
            [0, 0, 4, 0, -2, 0, 0, 2, 2, 6]],

    'Bing': [[0, 0, 0, 0, 2, 6, 10, 14, 18, 0],
             [0, 0, 0, 0, 0, 12, 20, 26, 36, 3],
             [0, 0, 0, -2, 8, 18, 30, 42, 56, 6],
             [0, 0, 0, 0, 0, 18, 34, 60, 80, 9],
             [0, 0, 0, 4, 8, 20, 40, 80, 120, 12],
             [0, 0, 0, 0, 0, 18, 34, 60, 80, 9],
             [0, 0, 0, -2, 8, 18, 30, 42, 56, 6],
             [0, 0, 0, 0, 0, 12, 20, 26, 36, 3],
             [0, 0, 0, 0, 2, 6, 10, 14, 18, 0]]
}
