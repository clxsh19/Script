from pytube import YouTube

### resolution available = 360p, 480p ###

Link = str(input("Video URL: "))
Tags = {"360p":"18", "720p":"22"}

print("Opening link...")
try:
    yt = YouTube(Link)
    resolution = str(input("Res: ").lower())
except:
    print("Check URL or Connection")

filter = yt.streams.get_by_itag(Tags[resolution])

print("Downloading Video...")
try:
    filter.download()
    print("Download Successfull")
except:
    print("Connection Failed")
