import time
from Product.RecommendationManager.run_recommendation_configurations.recreate_model \
    import RecreateModel
from Product.RecommendationManager.run_recommendation_configurations.update_success_rate \
    import UpdateSuccessRate
from Product.RecommendationManager.Recommendation.create_recommendations_for_all_users import CreateRecommendationsForAllUsers
"""
    Author: Marten Bolin
    Date: 2017-11-22
    Last update:
    Purpose: This starts the observer that creates and checks

"""
# Be aware that these will run until terminated! Do not forget them running in the background!
# Instantiate the class that will check for updates and recreate the model
model_updater = RecreateModel()

# Wait for RecreateModel to run once before updating success_rate
time.sleep(2)

# Instantiate the class that will update the succesrate daily
success_rate_updater = UpdateSuccessRate()

stop_loop=False
while not stop_loop:
    try:
        CreateRecommendationsForAllUsers.execute(10)
        stop_loop=True
    except ValueError:
        print("Waiting for TrendScore to commit, wait 5 seconds and then try again")
        time.sleep(5)