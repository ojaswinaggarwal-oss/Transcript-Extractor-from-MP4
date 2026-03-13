from faster_whisper import WhisperModel

Video_Path = "-----------"

model = WhisperModel("tiny")
segments, info = model.transcribe(Video_Path)

with open("transcript.txt", "w", encoding="utf-8") as f:
    for segment in segments:
        print(segment.text)          # prints in terminal
        f.write(segment.text + "\n") # saves to file

print("Transcript saved as transcript.txt")
