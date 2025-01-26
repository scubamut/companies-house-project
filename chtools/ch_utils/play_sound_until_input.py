def play_sound_until_input(path_to_sound_file):

    """
    Play a sound in a loop until the user provides input.

    This function uses threading to play a sound continuously in the background 
    while waiting for the user to provide input. Once the input is received, the sound stops.

    The sound file to be played is specified by its path. Make sure the file exists 
    at the specified location.

    Returns:
    str: The input provided by the user.

    Example:
    >>> user_input = play_sound_until_input()
    Please enter input until sound stops: Hello
    Sound stopped and program finished.
    """
    
    import threading
    import time
    from pydub import AudioSegment
    from pydub.playback import play

    # Define a function to play the sound in a loop
    def play_sound_loop():
        sound = AudioSegment.from_wav(path_to_sound_file)
        while not stop_event.is_set():
            play(sound)
            # Add a small delay to prevent overwhelming the CPU
            time.sleep(1)

    # Function to wait for user input
    def get_user_input(prompt):
        user_input = input(prompt)
        stop_event.set()
        return user_input

    # Create an Event object to signal when to stop playing the sound
    stop_event = threading.Event()

    # Start the thread to play sound
    sound_thread = threading.Thread(target=play_sound_loop)
    sound_thread.start()

    # Wait for user input
    user_input = get_user_input("Please enter input until sound stops: ")

    # Wait for the sound thread to finish
    sound_thread.join()

    return user_input


if __name__ == "__main__":
    # Example usage
    user_input = play_sound_until_input('/home/scubamut1/Downloads/ring2.wav')
    print(f"User input: {user_input}")
