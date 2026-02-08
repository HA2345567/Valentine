
from moviepy import VideoFileClip

def convert_video_to_gif(video_path, gif_path):
    try:
        # Load the video file
        clip = VideoFileClip(video_path)
        
        # Resize to a reasonable width for README (e.g., 600px) to keep file size manageable
        # GitHub has a 10MB limit for image uploads, but larger GIFs might load slowly.
        # Let's try to keep it under 10MB. 
        # Duration: convert first 10 seconds or full video if short.
        # Reduce FPS to 10 for size.
        
        duration = min(clip.duration, 10) # 10 seconds max for preview
        subclip = clip.subclipped(0, duration)
        resized_clip = subclip.resized(width=600)
        
        # Write the GIF file
        resized_clip.write_gif(gif_path, fps=10, logger=None)
        
        print(f"Successfully converted {video_path} to {gif_path}")
        
    except Exception as e:
        print(f"Error converting video: {str(e)}")

if __name__ == "__main__":
    convert_video_to_gif("video.mp4", "preview.gif")
