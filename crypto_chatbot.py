# Define the cryptocurrency database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

print("Hello! I'm CryptoBuddy. How can I help you with crypto advice today?")
print("Type 'quit' to exit.")

while True:
    user_query = input("You: ").lower()

    if "quit" in user_query:
        print("CryptoBuddy: Goodbye!")
        break

    # Add your chatbot logic here based on user_query and crypto_db
    
    recommended_profitable = []
    recommended_sustainable = []

    for coin, data in crypto_db.items():
        # Check for profitability rules
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            recommended_profitable.append(coin)

        # Check for sustainability rules
        if data["energy_use"] == "low" and data["sustainability_score"] > 7/10:
            recommended_sustainable.append(coin)

    if "trending" in user_query or "profitable" in user_query:
        if recommended_profitable:
            print("CryptoBuddy: Based on profitability, you might want to look into: " + ", ".join(recommended_profitable) + ".")
        else:
            print("CryptoBuddy: I don't have enough data to recommend a trending/profitable coin right now.")
    
    elif "sustainable" in user_query or "eco-friendly" in user_query:
        if recommended_sustainable:
            print("CryptoBuddy: For sustainability, consider: " + ", ".join(recommended_sustainable) + ".")
        else:
            print("CryptoBuddy: I don't have enough data to recommend a sustainable coin right now.")

    else:
        # For now, a simple placeholder response
        print("CryptoBuddy: I'm still learning! Ask me about trending or sustainable coins.") 