import datetime
def convert_to_milli_seconds(lap_time_str):
    if lap_time_str == None:
        return None
    # Split the time into minutes, seconds, and milliseconds
    minutes, rest = lap_time_str.split(":")
    seconds, milliseconds = rest.split(".")

    # Convert the components to integers
    minutes = int(minutes)
    seconds = int(seconds)
    milliseconds = int(milliseconds)

    # Calculate the total time in milliseconds
    total_milliseconds = (
        minutes * 60 * 1000 +  # Convert minutes to milliseconds
        seconds * 1000 +      # Convert seconds to milliseconds
        milliseconds
    )

    return total_milliseconds

