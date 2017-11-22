from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from Product.RecommendationManager.model.create_new_model import CreateNewModel
from Product.RecommendationManager.Recommendation.create_recommendations_for_all_users\
    import CreateRecommendationsForAllUsers
import time

# TODO: Docstrings and make check for chnages before update model
class RecreateModel:

    def __init__(self, daemon=False):
        self.scheduled = BackgroundScheduler()

        if not daemon:
            self.scheduled.daemon = False
        self.scheduled.add_job(self._run, 'interval', seconds=2, id="2")
        self.scheduled.start()
        self.scheduled.modify_job(job_id="2", next_run_time=datetime.now())

    def _run(self):
        print("Creating Model")
        CreateNewModel.create_new_model()

    def terminate(self):
        """
        Author: Marten Bolin
        Date:
        Last update:
        Purpose: Terminates the process
        """
        print("Shutting down update_recommendations..")
        self.scheduled.shutdown()

updating = RecreateModel()
time.sleep(60)
updating.terminate()

