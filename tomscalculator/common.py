
STATE_TAXES = {
    'UT': 6.85,
    'NV': 8,
    'TX': 6.25,
    'AL': 4,
    'CA': 8.25
}

DISCOUNTS = {
    50000: 15,
    10000: 10,
    7000: 7,
    5000: 5,
    1000: 3
}


def checkfields(amount, price, statecode):
    if statecode not in STATE_TAXES:
        return False

    try:
        if amount is None or int(amount) <= 0:
            return False
        if price is None or float(price) <= 0:
            return False
    except ValueError:
        return False

    return True


def process_calc(amount, price, statecode):
    result = {
        'result_price': 0,
        'price_with_discount': 0,
        'state_tax': 0
    }
    discount = 0
    amount = int(amount)
    price = float(price)
    price_sum = amount * price
    for i in sorted(DISCOUNTS.keys(), reverse=True):
        if price_sum >= i:
            discount = DISCOUNTS[i]
            break

    result['state_tax'] = STATE_TAXES[statecode]
    result['price_with_discount'] = price_sum * ((100 - discount) / 100)
    result['result_price'] = round(result['price_with_discount'] * ((100 + result['state_tax']) / 100), 2)

    return result
