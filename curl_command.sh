curl -X 'POST' \
  'http://127.0.0.1:8002/file/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@mixkit-arcade-retro-game-over-213.wav;type=audio/wav'
