
# Mock tool for e-commerce search
def search_ecommerce(query, price_range, size):
    # This is a mock search function, normally it would query e-commerce APIs
    return [
        {"product_name": "Floral Skirt", "price": 35, "size": "S", "store": "StoreA", "in_stock": True},
        {"product_name": "Floral Pattern Skirt", "price": 38, "size": "S", "store": "StoreB", "in_stock": True}
    ]

# Mock tool for shipping time estimator
def estimate_shipping(product, user_location, desired_date):
    # Returns mock shipping details
    return {
        "shipping_cost": 8,
        "estimated_delivery": "Friday"
    }

# Mock tool for discount checker
def apply_discount(product, discount_code):
    # Checks if discount code applies and returns the discounted price
    if discount_code == "SAVE10":
        return product['price'] * 0.9  # 10% off
    else:
        return product['price']

# Mock tool for competitor price comparison
def compare_prices(product_name):
    # Compare prices from various stores
    return [
        {"store": "StoreA", "price": 80},
        {"store": "StoreB", "price": 75},
        {"store": "StoreC", "price": 85}
    ]

# Mock tool for return policy checker
def check_return_policy(store):
    # Returns mock return policies
    return {
        "StoreA": "Returns accepted within 30 days, full refund for unworn items.",
        "StoreB": "Returns accepted within 15 days, exchange only."
    }
