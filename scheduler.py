import schedule, time, os
from text_overlay import add_text_to_video
from upload_to_ig import post_reel

def job():
    files = os.listdir("reels")
    if not files:
        print("No videos found.")
        return

    filename = files[0]
    input_path = f"reels/{filename}"
    output_path = f"edited/{filename}"

    print(f"[+] Processing {filename}")
    add_text_to_video(input_path, output_path, "🔥 Stay motivated!")
    post_reel(output_path)
    os.remove(input_path)

def start_schedule():
    schedule.every().day.at("10:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)