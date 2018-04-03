import time
import threedb
import get_ids
import get_users
import analysis

start = time.clock()
if(__name__ == "__main__"):
    account_name = "JanusCapital" # Change username here!
    account_name = account_name.lower() # Ensure that there aren't multiple copies of the same brand
    get_ids.get_ids(account_name)  # Get IDs: Add to brands_db
    print("Done Getting Ids")
    get_users.get_user_info(account_name) # Get user info: Add to users_db
    print("Done Getting All the User Info!")
    analysis.analyze_user(account_name) # Categorizes users: Add fields to users_db
    print("Done Categorizing Users")
    threedb.createThird(account_name) # Get results: Add to results_db and current_db
    print("Done Making results_db and current_db")
    print("Time elapsed:")
    print(time.clock() - start)