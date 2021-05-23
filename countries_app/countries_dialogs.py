from dataclasses import dataclass


@dataclass(frozen=True)
class CountriesMessages:
    choose_country: int = 'Выберите страну'
    choose_region: str = 'Выберите регион для поиска стран'
    write_country: str = 'Напишите наименование страны'


countries_msg = CountriesMessages()
