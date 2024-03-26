CITIES_EXPECTED = [
    {"id": 1, "name": "Москва"},
    {"id": 2, "name": "Санкт-Петербург"},
    {"id": 3, "name": "Вологда"},
    {"id": 4, "name": "Казань"},
    {"id": 5, "name": "Владивосток"},
    {"id": 6, "name": "Красноярск"},
    {"id": 7, "name": "Воронеж"},
    {"id": 8, "name": "Белгород"},
]
VACANCY_NAMES_EXPECTED = [
    {"id": 1, "name": "Frontend-разработчик"},
    {"id": 2, "name": "Python-разработчик"},
    {"id": 3, "name": "UX-дизайнер"},
    {"id": 4, "name": "Аудитор"},
    {"id": 5, "name": "бизнес-аналитик"},
    {"id": 6, "name": "бухгалтер"},
    {"id": 7, "name": "адвокат"},
    {"id": 8, "name": "нотариус"},
    {"id": 9, "name": "юрист"},
]
CATEGORIES_EXPECTED = [
    {
        "id": 1,
        "name": "Информационные технологии",
        "specializations": [
            {"id": 1, "name": "Frontend-разработчик"},
            {"id": 2, "name": "Python-разработчик"},
            {"id": 3, "name": "UX-дизайнер"},
        ],
    },
    {
        "id": 2,
        "name": "Экономика",
        "specializations": [
            {"id": 4, "name": "Аудитор"},
            {"id": 5, "name": "бизнес-аналитик"},
            {"id": 6, "name": "бухгалтер"},
        ],
    },
    {
        "id": 3,
        "name": "Юриспруденция",
        "specializations": [
            {"id": 7, "name": "адвокат"},
            {"id": 8, "name": "нотариус"},
            {"id": 9, "name": "юрист"},
        ],
    },
]

SPECIALIZATION_EXPECTED = {  # for vacancy_name_id = 2
    "id": 2,
    "name": "Python-разработчик",
    "category_id": 1,
    "responsibilities": [
        {"id": 4, "name": "разработка приложений и кода для серверной части"},
        {
            "id": 5,
            "name": "тестирование созданных программ и приложений (а также создание автотестов)",
        },
        {
            "id": 6,
            "name": "написание технической документации и пользовательских инструкций",
        },
    ],
    "requirements": [
        {"id": 4, "name": "знание Python и опыт разработки на нем"},
        {"id": 5, "name": "понимание сетевых технологий"},
        {"id": 6, "name": "знание SQL/MySQL/PostgreSQL/Redis"},
    ],
}

DATA_EXPECTED = {  # for vacancy_name_id = 1
    "category_id": 1,
    "name": "Frontend-разработчик",
    "id": 1,
    "responsibilities": [
        {
            "name": "разработка новых npm модулей для существующих приложений",
            "id": 1,
            "specialization_id": 1,
        },
        {
            "name": "проведение рефакторинга (улучшения и оптимизации кода) и ускорение работы сайтов/приложений",
            "id": 2,
            "specialization_id": 1,
        },
        {
            "name": "активное взаимодействие с backend-разработчиками",
            "id": 3,
            "specialization_id": 1,
        },
    ],
    "requirements": [
        {
            "name": "знание языков JavaScript/HTML5/CSS3",
            "specialization_id": 1,
            "id": 1,
        },
        {
            "name": "опыт адаптивной и кроссбраузерной верстки",
            "specialization_id": 1,
            "id": 2,
        },
        {
            "name": "понимание JS фреймворков Angular2/ReactJS/jQuery/Node.js",
            "specialization_id": 1,
            "id": 3,
        },
    ],
    "salary": {"min": 1000, "max": 2000},
    "conditions": [
        {"name": "оформление по ТК РФ", "id": 1},
        {"name": "обустроенный офис", "id": 2},
        {"name": "ДМС", "id": 3},
    ],
}
