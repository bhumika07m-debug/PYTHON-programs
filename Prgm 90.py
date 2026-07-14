import sys
def job_completed():

    print("Success: The job is completed successfully!")
    print('\a')
    sys.exit(0)
if __name__ == "__main__":
    print("Running your job...")
    job_completed()
