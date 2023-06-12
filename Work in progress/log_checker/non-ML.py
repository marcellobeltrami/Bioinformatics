
def deter_response(log_txt):
    import re
    from datetime import datetime
    # define the regular expression pattern to extract the timestamp and message
    pattern = r'^INFO\s+\[.+?\]\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+(.+)$'

    # define a dictionary to store the timestamps of each message
    timestamps = {}


    # open the file and read the lines
    with open(log_txt, 'r') as f:
        for line in f:
            # match the regular expression pattern against the line
            match = re.match(pattern, line)
            if match:
                # extract the timestamp and message from the match object
                timestamp, message = match.groups()
                # store the timestamp in the dictionary, with the message as the value
                timestamps[timestamp] = message

    # check if there are any missing timestamps
    previous_timestamp = None
    for timestamp in sorted(timestamps.keys()):
        if previous_timestamp is not None:
            # check if the current timestamp is more than a second later than the previous timestamp
            previous_time = datetime.strptime(previous_timestamp, '%Y-%m-%d %H:%M:%S,%f')
            current_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S,%f')
            time_difference = (current_time - previous_time).total_seconds()
            if time_difference > 1:
                return f"Anomaly detected: {timestamps[previous_timestamp]} and {timestamps[timestamp]} are more than a second apart."
        previous_timestamp = timestamp

print(deter_response("system-logdad.txt"))