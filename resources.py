dialog_income = {
    "title": "Доход",
    "submit_label": "Submit",
    "callback_id": "income_form",
    "elements": [
        {
            "label": "Категория",
            "type": "select",
            "name": "income_from",
            "placeholder": "Выберите категорию",
            "value": "products",
            "options": [
                {
                    "label": "Products",
                    "value": "products"
                },
                {
                    "label": "Email",
                    "value": "email"
                },
                {
                    "label": "Plus",
                    "value": "plus"
                },
                {
                    "label": "Banners",
                    "value": "banners"
                }
            ]
        },

        {
            "label": "Валюта",
            "type": "select",
            "name": "income_currency",
            "placeholder": "Выберите валюту",
            "value": "usd",
            "options": [
                {
                    "label": "USD",
                    "value": "usd"
                },
                {
                    "label": "RUR",
                    "value": "rur"
                },
                {
                    "label": "EUR",
                    "value": "eur"
                }
            ]
        },

        {
            "type": "text",
            "label": "Сколько?",
            "name": "income_value"
        }
    ]
}

mouth_dic = {
    '1':'b',
    '2':'c',
    '3':'d',
    '4':'e',
    '5':'f',
    '6':'g',
    '7':'h',
    '8':'i',
    '9':'j',
    '10':'k',
    '11':'l',
    '12':'m'
}