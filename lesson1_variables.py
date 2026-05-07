# YOUR TASK: Fill in the blanks with realistic values
# Use your imagination — make a real person!

customer_name    = "Hero Hindustani"    # Their full name (string)
customer_age     = 26    # Their age (integer)
wallet_balance   = 95222.84    # Their app wallet balance (float)
is_premium_user  = True    # Are they premium? (boolean)
city             = "Mumbai"    # Their city (string)
total_orders     = 25    # How many orders placed (integer)
avg_order_value  = 4590.25    # Average order amount (float)
is_verified      = True    # KYC verified? (boolean)
# Wallet balance stored in INR
# Note: RBI regulation caps unverified wallets at ₹10,000
# This field flags compliance review if is_verified=False

# Now print ALL of them with labels
# AND print the TYPE of each variable

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
