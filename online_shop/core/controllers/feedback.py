import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.utils import timezone
from core.models import FeedBack


class FeedBackController:
    def __init__(self, pk: int = None):
        self.feedback = None
        if pk:
            self.feedback = FeedBack.objects.get(id=pk)

    def create(self, email, text):
        self.feedback = FeedBack(
            email=email,
            text=text,
            date=timezone.now()
        )
        self.feedback.save()
        return self.feedback

    def send_to_email(self, send_me):
        addr_from = ""
        addr_to = "" #"qwerasdfzxcv1234"
        password = ""

        msg = MIMEMultipart()
        msg['From'] = addr_from
        msg['To'] = addr_to
        msg['Subject'] = "Новое обращение"
        flag = ""
        if send_me == False:
            flag += "не уведомлять"
        else:
            flag += "уведомить о получении"
        body = f'Поступило новое обращение с сайта Patter Hause\n' \
               f'Сообщение: {self.feedback.text}\nДля связи {self.feedback.email}.\n Пользователь просил {flag}'
        msg.attach(MIMEText(body, 'plain'))

        # ======== Настройка почтового провайдера ===============================================
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        print("Письмо отправлено")

    @staticmethod
    def delete(feedback: FeedBack):
        feedback.delete()
