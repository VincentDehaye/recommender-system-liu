from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from Product.RecommendationManager.model.create_new_model import CreateNewModel
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Retrieve.RetrieveRating import RetrieveRating


# TODO: Remove test in the bottom
class UpdateSuccessRate:
    """
    Author: Marten Bolin
    Date: 2017-11-22
    Last update:
    Purpose: This will be ran continously to check for any changes made and rearrange the model
    """

    def __init__(self, daemon=False):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose: The instantiation of the class, make sure to catch it in a variable so it can be
        terminated properly. Start the scheduler
        :param daemon : Sets daemon, (Optional) Default is False
        """

        # Set up and start the scheduler
        self.scheduled = BackgroundScheduler()
        if not daemon:
            self.scheduled.daemon = False
        self.scheduled.add_job(self._run, 'interval', days=1, id="3")
        self.scheduled.start()
        self.scheduled.modify_job(job_id="3", next_run_time=datetime.now())

    def _run(self):
        """
        Author: Marten Bolin
        Date:2017-11-22
        Last update:
        Purpose: The acutal process that will be ran
        """
        # TODO: This is the actions that will be done in each interval

    def terminate(self):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose: Terminates the process
        """
        print("Shutting down update_success_rate..")
        self.scheduled.shutdown()
        print("Update_success_rate has been shut down.")
