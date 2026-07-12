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




# loop that prints all of the data from the videos dictionary
for video in videos:
        print("Title: ", video["title"])
        print("platform: ", video["platform"])
        print("views: ", video["views"])
        print("likes: ", video["likes"])
        print("comments: ", video["comments"])



print("Total Views: ", get_video_views(videos))

