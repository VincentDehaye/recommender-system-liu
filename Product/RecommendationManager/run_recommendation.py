import time
from Product.RecommendationManager.run_recommendation_configurations.recreate_model \
    import RecreateModel
from Product.RecommendationManager.run_recommendation_configurations.update_success_rate \
    import UpdateSuccessRate
"""
This script will be used to set up the running of recommendation.
"""

# Be aware that these will run until terminated! Do not forget them running in the background!
# Instantiate the class that will check for updates and recreate the model
model_updater = RecreateModel()

# Instantiate the class that will update the succesrate daily
success_rate_updater = UpdateSuccessRate()
