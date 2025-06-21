from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_text_to_video(input_path, output_path, text):
    clip = VideoFileClip(input_path)
    txt = TextClip(text, fontsize=70, color='white', font="Arial-Bold") \
        .set_position(('center', 'bottom')).set_duration(clip.duration)
    final = CompositeVideoClip([clip, txt])
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')