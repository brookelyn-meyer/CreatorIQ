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

videos = [
        
        {"title": "Morning Routine", "Platform": "Tiktok", "Views": 100000, "likes": 10000, "comments": 200},
        {"title": "Nespresso Latte", "Platform": "Instagram", "Views": 25000, "likes": 20000, "comments": 260}
]

for video in videos:
        print("Title: ", video["title"])
        print("Platform: ", video["Platform"])
        print("Views: ", video["Views"])
        print("likes: ", video["likes"])
        print("comments: ", video["comments"])
