import time
from plyer import notification

count = 0
print("The pomodoro timer has started, start working!")

if __name__ == "__main__":
    while True:
        time.sleep(10)
        count += 1
        notification.notify(
            title = "Good work!",
            message = "Take a 10 minute break! You have completed " + str(count) + " pomodoros so far",
        )
        time.sleep(5)
        notification.notify(
            title = "Back to work!",
            message = "Try doing another pomodoro...",
        )