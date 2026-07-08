import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Get API key from .env file
api_key = os.getenv("api_key")
client = genai.Client(api_key=api_key)
mobiles = []
while True:
    print("\n==== ˆ_□   MOBILE SHOP DASHBOARD ====")
    print("1. Add Mobile")
    print("2. View Mobiles") 
    print("3. Update Mobile") 
    print("4. Delete Mobile") 
    print("5. Search Mobile") 
    print("6. Sort by Price")
    print("7. AI Chatbot Help ") 
    print("8. Exit")
    choice = int(input("Enter choice: ")) 
    match choice:
        # ❭ CREATE
        case 1:
            name = input("Enter mobile name: ") 
            brand = input("Enter brand: ")
            price = int(input("Enter price: "))

            mobile = [name, brand, price] 
            mobiles.append(mobile)
            print("Mobile added successfully")
        # ❭ READ
        case 2:
            print("\nMobile List:") 
            for m in mobiles:
                print(m)
        # ❭ UPDATE
        case 3:
            name = input("Enter mobile name to update: ")

            for m in mobiles:
                if m[0] == name:
                    m[1] = input("Enter new brand: ") 
                    m[2] = int(input("Enter new price: ")) 
                    print(" Updated successfully")
        # ❭ DELETE
        case 4:
            name = input("Enter mobile name to delete: ")

            for m in mobiles:
                if m[0] == name:

                    mobiles.remove(m)
                    print(" Deleted successfully")
        # ❭ CUSTOM: SEARCH
        case 5:
            keyword = input("Enter search keyword: ")

            print("\nSearch Results:") 
            for m in mobiles:
                if keyword.lower() in m[0].lower():
                    print(m)
        # ❭ CUSTOM: SORT
        case 6:
            mobiles.sort(key=lambda x: x[2]) 
            print(" Sorted by price")
            for m in mobiles: print(m)
        # ❭ AI FEATURE (Gemini)
        case 7:
            query = input("Ask about any mobile: ")

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents="Give mobile details and suggestion: " + query)

            print("\nAI Response:") 
            print(response.text)
        # ❭ EXIT
        case 8:
            print(" Exiting...") 
            break
        case _:
            print("+ Invalid choice")
