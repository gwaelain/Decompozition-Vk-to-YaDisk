from Vk import VkUser
from Yandex import UploadToYaD


if __name__ == '__main__':
    vk_user_id = VkUser(input('Введите id пользователя: '))
    uploader = UploadToYaD(input('Введите токен YaDisk: '))
    print('Скачивание и сохранение фото на YaDisk')
    uploader.from_vk_to_yad(vk_user_id)