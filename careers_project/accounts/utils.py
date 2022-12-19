from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import ResetToken

User = get_user_model()
def forget_password_email(*args):
    try:
        user = User.objects.get(email=args[0])
        reset_token = ResetToken.objects.get(user=user)
        if user.email:
            
            if user.is_superuser:
                pass
            else:
                message = MIMEMultipart()
                message['From'] = 'Career'
                message['To'] =  user.email
                message['Subject'] = 'Career'
                html = f"""
                                    <html>
                                        <body>
                                        <h3>
                                            Hi {user.first_name}, 
                                            <p>Click on the below link to reset your password:</p>
                                            <a href="http://127.0.0.1:8000/accounts/reset_password/{str(reset_token.id)}"> Reset Password </a>
                                        </h3>
                                        </body>
                                    </html>
                                    """
                message.attach(MIMEText(html, 'html'))
                with smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(user=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD)
                    smtp.send_message(message)
    except Exception as error:
        pass
        print(str(error))
