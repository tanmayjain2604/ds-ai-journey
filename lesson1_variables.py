# YOUR TASK: Fill in the blanks with realistic values
# Use your imagination — make a real person!

customer_name    = "Hero Hindustani"    # Their full name (string)
customer_age     = 26    # Their age (integer)
wallet_balance   = 95222.84    # Their app wallet balance (float)
is_premium_user  = True    # Are they premium? (boolean)
city             = "Mumbai"    # Their city (string)
total_orders     = 25    # How many orders placed (integer)
avg_order_value  = 4590.25    # Average order amount (float)
is_verified      = False    # KYC verified? (boolean)

# Now print ALL of them with labels
# AND print the TYPE of each variable

# print("Customer Name:", customer_name)
# print("Age:", customer_age)
# print("Wallet Balance:", wallet_balance)
# print("Premium User?", is_premium_user)
# print("City:", city)
# print("Orders Placed:", total_orders)
# print("Average Order Amount:", avg_order_value)
# print("KYC Verified?", is_verified)
# print(type(customer_name))
# print(type(customer_age))
# print(type(wallet_balance))
# print(type(is_premium_user))
# print(type(city))
# print(type(total_orders))
# print(type(avg_order_value))
# print(type(is_verified))

# ============================================
# SENIOR VERSION — combine label + type together
# ============================================
print(f"Customer Name : {customer_name} (Type: {type(customer_name).__name__})")
print(f"Age           : {customer_age} (Type: {type(customer_age).__name__})")
print(f"Wallet Balance: {wallet_balance} (Type: {type(wallet_balance).__name__})")
print(f"Premium User? : {is_premium_user} (Type: {type(is_premium_user).__name__})")
print(f"City          : {city} (Type: {type(city).__name__})")
print(f"Total Orders  : {total_orders} (Type: {type(total_orders).__name__})")
print(f"Avg Order Val : {avg_order_value} (Type: {type(avg_order_value).__name__})")
print(f"KYC Verified? : {is_verified} (Type: {type(is_verified).__name__})")