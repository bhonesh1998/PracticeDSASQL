from datetime import datetime

epoch_time = 1714922863337 / 1000  # Convert milliseconds to seconds
timestamp_with_ms = datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S.%f')

print(timestamp_with_ms)