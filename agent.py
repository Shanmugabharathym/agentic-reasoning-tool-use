from tools import search_ecommerce, estimate_shipping, apply_discount, compare_prices, check_return_policy

# Define a simple agent class
class ShoppingAgent:
    def __init__(self):
        self.system_prompt = "You are a virtual shopping assistant. Help users find the best shopping deals and provide necessary information on shipping, prices, and return policies."
    
    def process_query(self, user_query):
        """
        Process the user query by detecting relevant information (e.g., items, price, size, etc.)
        and invoking appropriate tools.
        """
        if "find" in user_query and "skirt" in user_query:
            # Example: "Find a floral skirt under $40 in size S."
            return self.handle_item_search(user_query)
        
        if "shipping" in user_query:
            # Example: "Can it arrive by Friday?"
            return self.handle_shipping(user_query)
        
        if "discount" in user_query:
            # Example: "Can I apply a discount code SAVE10?"
            return self.handle_discount(user_query)
        
        if "compare" in user_query:
            # Example: "Can you compare prices for a casual denim jacket?"
            return self.handle_price_comparison(user_query)
        
        if "return" in user_query:
            # Example: "Do they accept returns on this product?"
            return self.handle_return_policy(user_query)
    
    def handle_item_search(self, user_query):
        # Parse the query for price and size constraints (mocked)
        price_range = "under $40"
        size = "S"
        # Use the e-commerce search tool
        products = search_ecommerce("floral skirt", price_range, size)
        
        # Present the results
        result = "I found the following floral skirts under $40 in size S:\n"
        for product in products:
            result += f"{product['product_name']} from {product['store']} - ${product['price']}. In stock: {product['in_stock']}\n"
        
        return result
    
    def handle_shipping(self, user_query):
        # Parse the query for product, location, and deadline
        product = {"product_name": "White Sneakers", "size": "8", "price": 65}  # Example product
        user_location = "NYC"
        desired_delivery = "Friday"
        
        # Estimate shipping
        shipping_details = estimate_shipping(product, user_location, desired_delivery)
        
        # Respond with shipping info
        result = f"Shipping for {product['product_name']} to {user_location} will cost ${shipping_details['shipping_cost']} and will arrive by {shipping_details['estimated_delivery']}."
        return result
    
    def handle_discount(self, user_query):
        # Example of product to apply discount to
        product = {"product_name": "Floral Skirt", "price": 35}
        discount_code = "SAVE10"
        
        # Apply discount
        discounted_price = apply_discount(product, discount_code)
        
        # Return the result
        result = f"After applying the discount code '{discount_code}', the new price is ${discounted_price:.2f}."
        return result
    
    def handle_price_comparison(self, user_query):
        # Compare prices for a denim jacket
        product_name = "casual denim jacket"
        
        # Get price comparison results
        price_comparison = compare_prices(product_name)
        
        result = f"Here is a price comparison for the {product_name}:\n"
        for store in price_comparison:
            result += f"{store['store']} - ${store['price']}\n"
        
        return result
    
    def handle_return_policy(self, user_query):
        # Example of checking return policy for a store
        store = "StoreB"
        
        # Get return policy for the store
        return_policy = check_return_policy(store)
        
        result = f"The return policy for {store}: {return_policy}"
        return result

# Example of running a complete interaction
if __name__ == "__main__":
    agent = ShoppingAgent()
    
    # Simulate user input
    user_query = "Find a floral skirt under $40 in size S. Is it in stock, and can I apply a discount code 'SAVE10'?"
    response = agent.process_query(user_query)
    print(response)
    
    user_query = "I need white sneakers (size 8) for under $70 that can arrive by Friday."
    response = agent.process_query(user_query)
    print(response)
    
    user_query = "Can you compare prices for a casual denim jacket?"
    response = agent.process_query(user_query)
    print(response)
    
    user_query = "Do they accept returns on this product?"
    response = agent.process_query(user_query)
    print(response)
