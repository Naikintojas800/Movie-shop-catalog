from datetime import datetime

class TimeCurrent:
    def get_time(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_datetime