from Product.TrendManager.TrendScoreToDatabase import TrendingToDB
import time
# TrendingToDB has two in parameters, background means that it will be ran i the background until the application
# terminates and continous = True means that it will run continously. If false it will only run one iteration
# If background is set to True(default) a timer can be used in this case with time.sleep(seconds) that will make it
# run for seconds
# trending_run.terminate() will stop the function
trending_run = TrendingToDB(daily=False)
time.sleep(50000)
trending_run.terminate()
time.sleep(10)
print("Finished")

