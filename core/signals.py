from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Order
from .telegram import send_telegram_message


@receiver(m2m_changed, sender=Order.services.through)
def order_services_changed(sender, instance, action, **kwargs):
    if action == "post_add":  # ← ВАЖНО: только после добавления услуг!
        services = ", ".join([s.name for s in instance.services.all()])
        message = (
            f"*Новый заказ!* 📩\n\n"
            f"*Клиент:* {instance.client_name}\n"
            f"*Телефон:* {instance.phone}\n"
            f"*Мастер:* {instance.master.name}\n"
            f"*Услуги:* {services}\n"
            f"*Дата:* {instance.appointment_date.strftime('%d.%m.%Y %H:%M')}\n"
            f"*Статус:* {instance.get_status_display()}"
        )
        send_telegram_message(message)  # ← ЭТО ОТПРАВЛЯЕТ СООБЩЕНИЕ
