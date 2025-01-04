from pydub import AudioSegment
from pydub.playback import play

target_filename = "open_door.mp3"

sound = AudioSegment.from_file(target_filename, "mp3")

reversed_sound = sound.reverse()

reversed_sound.export("output.mp3", "mp3")