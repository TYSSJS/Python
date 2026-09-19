import subprocess, json, os

INPUT = "/home/vkjayaram/Videos/GNUT0691.MOV"
OUTPUT = "/home/vkjayaram/Videos/GNUT0691_compressed.MOV"

# 9.8 million bytes = 9.8 MB = safe under 10.0 MB on all platforms
HARD_LIMIT_BYTES = 9800000 
AUDIO_KBPS = 32
PASSLOG = "/tmp/ffmpeg2pass"

def get_duration(p):
    cmd = ["ffprobe","-v","error","-show_entries","format=duration","-of","json",p]
    r = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(json.loads(r.stdout)["format"]["duration"])

duration = get_duration(INPUT)
print(f"Duration: {duration:.1f}s")

# Calculate video bitrate for 9.5MB to leave room
target_mb = 9.2
target_bits = target_mb * 1024 * 1024 * 8
video_kbps = int(max(80_000, (target_bits - AUDIO_KBPS*1000*duration) / duration) / 1000)

print(f"Encoding at {video_kbps}k video + {AUDIO_KBPS}k audio with hard cap {HARD_LIMIT_BYTES} bytes")

for f in [f"{PASSLOG}-0.log", f"{PASSLOG}-0.log.mbtree"]:
    if os.path.exists(f): os.remove(f)

subprocess.run([
    "ffmpeg","-y","-i",INPUT,
    "-vf","scale=-2:720", # REMOVE this line if video is <60 sec and you want original res
    "-c:v","libx264","-preset","slow",
    "-b:v",f"{video_kbps}k","-maxrate",f"{video_kbps}k","-bufsize",f"{video_kbps}k",
    "-pass","1","-passlogfile",PASSLOG,"-an","-f","null",os.devnull
], check=True)

subprocess.run([
    "ffmpeg","-y","-i",INPUT,
    "-vf","scale=-2:720",
    "-c:v","libx264","-preset","slow",
    "-b:v",f"{video_kbps}k","-maxrate",f"{video_kbps}k","-bufsize",f"{video_kbps}k",
    "-pass","2","-passlogfile",PASSLOG,
    "-c:a","aac","-b:a",f"{AUDIO_KBPS}k",
    "-movflags","+faststart",
    "-fs", str(HARD_LIMIT_BYTES), # <--- 9800000 bytes = guaranteed <=10MB
    OUTPUT
], check=True)

final = os.path.getsize(OUTPUT)
print(f"Final: {final} bytes = {final/(1024*1024):.2f} MiB = {final/1000000:.2f} MB")
print("PASS" if final <= 10000000 else "FAIL - still over")