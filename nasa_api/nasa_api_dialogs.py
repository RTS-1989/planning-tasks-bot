from dataclasses import dataclass


NASA_PHOTO_BUTTON_TEXT = {
    '1': ' Фотография дня Nasa'
}


@dataclass(frozen=True)
class NasaApiMessages:
    choose_service: int = 'Выберите сервис Nasa'
    send_photo_of_the_day = 'Отправляем фото дня'


nasa_api_msg = NasaApiMessages()
