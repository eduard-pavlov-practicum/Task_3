BASE_URL = 'https://qa-stellarburgers.education-services.ru'
API_BASE_URL = f'{BASE_URL}/api'

# UI urls
FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
RESET_PASSWORD_URL = f'{BASE_URL}/reset-password'
CONSTRUCTOR_URL = f'{BASE_URL}/'
LOGIN_URL = f'{BASE_URL}/login'
PROFILE_URL = f'{BASE_URL}/account/profile'
ORDER_HISTORY_URL = f'{BASE_URL}/account/order-history'
FEED_URL = f'{BASE_URL}/feed'

# API urls
REGISTER_API_URL = f"{API_BASE_URL}/auth/register"
USER_API_URL = f"{API_BASE_URL}/auth/user"
INGREDIENTS_API_URL = f'{API_BASE_URL}/ingredients'


def ingredient_card_url(ingredient_url):
    return f'{BASE_URL}{ingredient_url}'
