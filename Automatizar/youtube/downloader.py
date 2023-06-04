from pytube import YouTube

video_url = ""
output_path = "/Users/lmos/Desktop/videos"

try:
    # create a YouTube object and print the video title
    yt = YouTube(video_url)
    print("Title:", yt.title)

    # get the highest resolution stream and download the video
    yd = yt.streams.get_highest_resolutio()
    yd.download(output_path)

    print("deu certo! ")
except Exception as e:
    print("Error:", e)

