import requests
from django.conf import settings


def get_token():
    """
    Sms jonatishdan oldin olinadigan token
    """
    url = "https://notify.eskiz.uz/api/auth/login"
    payload = {
        'email': settings.ESKIZ_EMAIL,
        'password': settings.ESKIZ_SECRET_KEY,
    }
    response = requests.post(url, data=payload)
    return response.json().get('data').get('token')


def eskiz_send_message(phone_number, code):
    """
    phone_number ga code ni SMS qilib jonatish uchun funksiya
    """
    phone_number = phone_number.replace('+', '')
    url = "https://notify.eskiz.uz/api/message/sms/send"
    payload = {
        'mobile_phone': phone_number,
        'message': f"Confirmation code of Moscow Academy: {code}",
        'from': '4546',
        'callback_url': "http://0000.uz/test.php"
    }
    response = requests.post(url, payload, headers={'Authorization': f'Bearer {get_token()}'})
    return response
