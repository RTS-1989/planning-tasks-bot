COUNTRY_DATA_TO_SEARCH = ['name', 'capital', 'population', 'borders', 'currencies', 'languages']

REGIONS = {
    '1': ['Африка', 'africa'],
    '2': ['Европа', 'europe'],
    '3': ['Азия', 'asia'],
    '4': ['Северная и Южная Америка', 'americas'],
    '5': ['Океания', 'oceania'],
    '6': ['Полярный регион', 'polar']
}

COUNTRIES = {'Afghanistan': 'Афганистан',
             'Åland Islands': 'Аландские острова',
             'Albania': 'Албания',
             'Algeria': 'Алжир',
             'American Samoa': 'Американское Самоа',
             'Andorra': 'Андорра',
             'Angola': 'Ангола',
             'Anguilla': 'Ангилья',
             'Antarctica': 'Антарктика',
             'Antigua and Barbuda': 'Антигуа и Барбуда',
             'Argentina': 'Аргентина',
             'Armenia': 'Армения',
             'Aruba': 'Аруба',
             'Australia': 'Австралия',
             'Austria': 'Австрия',
             'Azerbaijan': 'Азербайджан',
             'The Bahamas': 'Багамские Острова',
             'Bahrain': 'Бахрейн',
             'Bangladesh': 'Бангладеш',
             'Barbados': 'Барбадос',
             'Belarus': 'Белоруссия',
             'Belgium': 'Бельгия',
             'Belize': 'Белиз',
             'Benin': 'Бенин',
             'Bermuda': 'Бермудские Острова',
             'Bhutan': 'Бутан',
             'Bolivia': 'Боливия',
             'Bonaire': 'Бонайре',
             'Bosnia and Herzegovina': 'Босния и Герцеговина',
             'Botswana': 'Ботсвана',
             'Bouvet Island': 'Остров Буве',
             'Brazil': 'Бразилия',
             'British Indian Ocean Territory': 'Британская Территория в Индийском Океане',
             'United States Minor Outlying Islands': 'Внешние малые острова США',
             'Virgin Islands (British)': 'Британские Виргинские острова',
             'Virgin Islands (U.S.)': 'Американские Виргинские острова',
             'Brunei': 'Бруней',
             'Bulgaria': 'Болгария',
             'Burkina Faso': 'Буркина-Фасо',
             'Burundi': 'Бурунди',
             'Cambodia': 'Камбоджа',
             'Cameroon': 'Камерун',
             'Canada': 'Канада',
             'Cape Verde': 'Кабо-Верде',
             'Cayman Islands': 'Каймановы острова',
             'Central African Republic': 'Центральноафриканская Республика',
             'Chad': 'Чад',
             'Chile': 'Чили',
             'China': 'Китай',
             'Christmas Island': 'Остров Рождества',
             'Cocos (Keeling) Islands': 'Кокосовые острова (Килинг)',
             'Colombia': 'Колумбия',
             'Comoros': 'Коморские острова',
             'Republic of the Congo': 'Республика Колнго',
             'Democratic Republic of the Congo': 'Демократическая республика конго',
             'Cook Islands': 'Острова Кука',
             'Costa Rica': 'Коста-Рика',
             'Croatia': 'Хорватия',
             'Cuba': 'Куба',
             'Curaçao': 'Кюрасао',
             'Cyprus': 'Кипр',
             'Czech Republic': 'Чехия',
             'Denmark': 'Дания',
             'Djibouti': 'Джибути',
             'Dominica': 'Доминика',
             'Dominican Republic': 'Доминиканская республика',
             'Ecuador': 'Эквадор',
             'Egypt': 'Египет',
             'El Salvador': 'Сальвадор',
             'Equatorial Guinea': 'Экваториальная гвинея',
             'Eritrea': 'Эритрея',
             'Estonia': 'Эстония',
             'Ethiopia': 'Эфиопия',
             'Falkland Islands': 'Фолклендские острова',
             'Faroe Islands': 'Фарерские острова',
             'Fiji': 'Фиджи',
             'Finland': 'Финляндия',
             'France': 'Франция',
             'French Guiana': 'Французская Гвиана',
             'French Polynesia': 'Французская Полинезия',
             'French Southern and Antarctic Lands': 'Французские Южные и Антарктические земли',
             'Gabon': 'Габон',
             'The Gambia': 'Гамбия',
             'Georgia': 'Грузия',
             'Germany': 'Германия (ФРГ)',
             'Ghana': 'Гана',
             'Gibraltar': 'Гибралтар',
             'Greece': 'Греция',
             'Greenland': 'Гренландия',
             'Grenada': 'Гренада',
             'Guadeloupe': 'Гваделупа',
             'Guam': 'Гуам',
             'Guatemala': 'Гватемала',
             'Guernsey': 'Гернси',
             'Guinea': 'Гвинея',
             'Guinea-Bissau': 'Гвинея-Бисау',
             'Guyana': 'Гайана',
             'Haiti': 'Гаити',
             'Heard Island and McDonald Islands': 'Острова Херд и Макдональд',
             'Holy See': 'Ватикан (Святой Престол)',
             'Honduras': 'Гондурас',
             'Hong Kong': 'Гонконг',
             'Hungary': 'Венгрия',
             'Iceland': 'Исландия',
             'India': 'Индия',
             'Indonesia': 'Индонезия',
             'Ivory Coast': 'Кот-д’Ивуар',
             'Iran': 'Иран',
             'Iraq': 'Ирак',
             'Republic of Ireland': 'Ирландия',
             'Isle of Man': 'Остров Мэн',
             'Israel': 'Израиль',
             'Italy': 'Италия',
             'Jamaica': 'Ямайка',
             'Japan': 'Япония',
             'Jersey': 'Джерси (Остров)',
             'Jordan': 'Иордания',
             'Kazakhstan': 'Казахстан',
             'Kenya': 'Кения',
             'Kiribati': 'Кирибати',
             'Kuwait': 'Кувейт',
             'Kyrgyzstan': 'Киргизия',
             'Laos': 'Лаос',
             'Latvia': 'Латвия',
             'Lebanon': 'Ливан',
             'Lesotho': 'Лесото',
             'Liberia': 'Либерия',
             'Libya': 'Ливия',
             'Liechtenstein': 'Лихтенштейн',
             'Lithuania': 'Литва',
             'Luxembourg': 'Люксембург',
             'Macau': 'Макао',
             'Republic of Macedonia': 'Северная Македония (Македония)',
             'Madagascar': 'Мадагаскар',
             'Malawi': 'Малави',
             'Malaysia': 'Малайзия',
             'Maldives': 'Мальдивы',
             'Mali': 'Мали',
             'Malta': 'Мальта',
             'Marshall Islands': 'Маршалловы Острова',
             'Martinique': 'Мартиника',
             'Mauritania': 'Мавритания',
             'Mauritius': 'Маврикий',
             'Mayotte': 'Майотта',
             'Mexico': 'Мексика',
             'Federated States of Micronesia': 'Федеративные Штаты Микронезии',
             'Moldova': 'Молдавия',
             'Monaco': 'Монако',
             'Mongolia': 'Монголия',
             'Montenegro': 'Черногория',
             'Montserrat': 'Монсеррат',
             'Morocco': 'Марокко',
             'Mozambique': 'Мозамбик',
             'Myanmar': 'Мьянма',
             'Namibia': 'Намибия',
             'Nauru': 'Науру',
             'Nepal': 'Непал',
             'Netherlands': 'Нидерланды',
             'New Caledonia': 'Новая Каледония',
             'New Zealand': 'Новая Зеландия',
             'Nicaragua': 'Никарагуа',
             'Niger': 'Нигер',
             'Nigeria': 'Нигерия',
             'Niue': 'Ниуэ',
             'Norfolk Island': 'Северная Ирландия',
             'North Korea': 'Северная Корея',
             'Northern Mariana Islands': 'Северные Марианские острова',
             'Norway': 'Норвегия',
             'Oman': 'Оман',
             'Pakistan': 'Пакистан',
             'Palau': 'Палау',
             'Palestine': 'Палестина',
             'Panama': 'Панама',
             'Papua New Guinea': 'Папуа - Новая Гвинея',
             'Paraguay': 'Парагвай',
             'Peru': 'Перу',
             'Philippines': 'Филиппины',
             'Pitcairn Islands': 'Острова Питкэрн',
             'Poland': 'Польша',
             'Portugal': 'Португалия',
             'Puerto Rico': 'Пуэрто-Рико',
             'Qatar': 'Катар',
             'Republic of Kosovo': 'Республика Косово',
             'Réunion': 'Реюньон',
             'Romania': 'Румыния',
             'Russia': 'Россия',
             'Rwanda': 'Руанда',
             'Saint Barthélemy': 'Сен-Бартелеми',
             'Saint Helena': 'Остров Святой Елены',
             'Saint Kitts and Nevis': 'Сент-Китс и Невис',
             'Saint Lucia': 'Сент-Люсия',
             'Saint Martin': 'Сен-Мартен',
             'Saint Pierre and Miquelon': 'Сен-Пьер и Микелон',
             'Saint Vincent and the Grenadines': 'Сент-Винсент и Гренадины',
             'Samoa': 'Самоа',
             'San Marino': 'Сан-Марино',
             'São Tomé and Príncipe': 'Сан-Томе и Принсипи',
             'Saudi Arabia': 'Саудовская Аравия',
             'Senegal': 'Сенегал',
             'Serbia': 'Сербия',
             'Seychelles': 'Сейшельские Острова',
             'Sierra Leone': 'Сьерра-Леоне',
             'Singapore': 'Сингапур',
             'Sint Maarten': 'Синт-Мартен',
             'Slovakia': 'Словакия',
             'Slovenia': 'Словения',
             'Solomon Islands': 'Соломоновы Острова',
             'Somalia': 'Сомали',
             'South Africa': 'ЮАР',
             'South Georgia': 'Южная Георгия',
             'South Korea': 'Южная Корея',
             'South Sudan': 'Южный Судан',
             'Spain': 'Испания',
             'Sri Lanka': 'Шри-Ланка',
             'Sudan': 'Судан',
             'Suriname': 'Суринам',
             'Svalbard and Jan Mayen': 'Шпицберген и Ян-Майен',
             'Swaziland': 'Эсватини (Свазиленд)',
             'Sweden': 'Швеция',
             'Switzerland': 'Шаейцария',
             'Syria': 'Сирия',
             'Taiwan': 'Тайвань',
             'Tajikistan': 'Таджикистан',
             'Tanzania': 'Танзания',
             'Thailand': 'Тайланд',
             'East Timor': 'Восточный Тимор',
             'Togo': 'Того',
             'Tokelau': 'Токелау',
             'Tonga': 'Тонга',
             'Trinidad and Tobago': 'Тринидад и Тобаго',
             'Tunisia': 'Тунис',
             'Turkey': 'Турция',
             'Turkmenistan': 'Туркмения',
             'Turks and Caicos Islands': 'Тёркс и Кайкос',
             'Tuvalu': 'Тувалу',
             'Uganda': 'Уганда',
             'Ukraine': 'Украина',
             'United Arab Emirates': 'Объединённые Арабские Эмираты',
             'United Kingdom': 'Великобритания',
             'United States': 'США (Соединенные Штаты Америки)',
             'Uruguay': 'Уругвай',
             'Uzbekistan': 'Узбекистан',
             'Vanuatu': 'Вануату',
             'Venezuela': 'Венесуэлла',
             'Vietnam': 'Вьетнам',
             'Wallis and Futuna': 'Уоллис и Футуна',
             'Western Sahara': 'Западная Сахара',
             'Yemen': 'Йемен',
             'Zambia': 'Замбия',
             'Zimbabwe': 'Зимбабве'
             }