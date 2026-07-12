# CreatorIQ

# ----------------------------

# Morning Routine
# Platform: TikTok
# Views: 100000

# ----------------------------

# Nespresso Latte
# Platform: Instagram
# Views: 25000

#display every video currently stored in creatorIQ

# - loop through every video, print the title, print the platform, print the views, separate videos with a line.


# the "videos" dictionary that holds all of the information about the videos
videos = [
        
        {"title": "Morning Routine", "platform": "Tiktok", "views": 100000, "likes": 10000, "comments": 200},
        {"title": "Nespresso Latte", "platform": "Instagram", "views": 25000, "likes": 20000, "comments": 260}
]

# created a function that gets the total videos
def get_video_views(videos):
        total = 0

        for video in videos:
                total += video["views"]
        
        return total

def most_viewed(videos):
        largest = None
        for video in videos:
                if largest is None:
                        largest = video
                elif video["views"] > largest["views"]:
                        largest = video
                
                return largest

# loop that prints all of the data from the videos dictionary
for video in videos:
        print("Title: ", video["title"])
        print("platform: ", video["platform"])
        print("views: ", video["views"])
        print("likes: ", video["likes"])
        print("comments: ", video["comments"])

def print_video(video):
    print("Title:", video["title"])
    print("Platform:", video["platform"])
    print("Views:", video["views"])
    print("Likes:", video["likes"])
    print("Comments:", video["comments"])

def find_video(videos, title):
        for video in videos:
                if video["title"] == title:
                        return video
        
        
        return None


most_viewed = most_viewed(videos)
found_video = find_video(videos, "Morning Routine")

print("Total Views: ", get_video_views(videos))
print("Title: ", most_viewed["title"])
print("Views: ", most_viewed["views"])
print("Likes: ", most_viewed["likes"])
print("Comments: ", most_viewed["comments"])
print("The first video's information: ")
print_video(videos[0])
print(found_video)
