import os

def get_env_list(var_name, default=None):
    """Вспомогательная функция для безопасного чтения списков ID из строк"""
    val = os.getenv(var_name)
    if not val:
        return default or []
    return [int(x.strip()) for x in val.split(',') if x.strip().isdigit()]

# --- КРИТИЧЕСКИЕ ДАННЫЕ (Без значений по умолчанию) ---
API_TOKEN = os.getenv('BOT_TOKEN')
if not API_TOKEN:
    raise ValueError("Критическая ошибка: Переменная BOT_TOKEN не задана на хостинге!")

# Список администраторов (если не задан, будет пустым)
admin = get_env_list('ADMIN_IDS', default=[])

# --- НАСТРОЙКИ БОТА И АДМИНА ---
bot_name = os.getenv('BOT_NAME', '@YourBot')
bot_username = os.getenv('BOT_USERNAME', 'YourBot')
admin_username = os.getenv('ADMIN_USERNAME', '@YourUsername')

# Ссылки на чаты и каналы
chat = os.getenv('CHAT_LINK', 't.me/YourChat')
channel = os.getenv('CHANNEL_LINK', 't.me/YourChannel')

# Игровые и системные параметры
start_money = int(os.getenv('START_MONEY', '0'))
chat_log = int(os.getenv('CHAT_LOG', '0'))
cleaning = int(os.getenv('CLEANING', '0'))

# Булево значение (True/False)
custom_modules = os.getenv('CUSTOM_MODULES', 'False').lower() in ('true', '1', 'yes')
