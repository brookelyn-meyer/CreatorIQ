def get_video_views(videos):
    total = 0

    for video in videos:
        total += video["views"]

    return total


def find_video(videos, title):
    for video in videos:
        if video["title"].lower() == title.lower():
            return video

    return None


def find_most_viewed(videos):
    largest = None

    for video in videos:
        if largest is None:
            largest = video
        elif video["views"] > largest["views"]:
            largest = video

    return largest


def get_video_titles(videos):
    titles = []

    for video in videos:
        titles.append(video["title"])

    return titles


def count_popular_videos(videos):
    count = 0

    for video in videos:
        if video["views"] > 50000:
            count += 1

    return count


def average_views(videos):
    if len(videos) == 0:
        return 0

    total = get_video_views(videos)
    average = total / len(videos)

    return average