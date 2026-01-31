import whisper

model = whisper.load_model("base")  # or tiny, small, medium, large

result = model.transcribe("https://cdnydm.com/wh_new/Ymu8LdSRhTA4LQXpjxRisA.oga", fp16 = False)

print(result["text"])
