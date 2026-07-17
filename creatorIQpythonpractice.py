
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
