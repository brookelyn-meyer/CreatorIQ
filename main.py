from video_data import videos

from analytics import (
    get_video_views,
    find_video,
    find_most_viewed,
    get_video_titles,
    count_popular_videos,
    average_views
)


def print_video(video):
    print("Title:", video["title"])
    print("Platform:", video["platform"])
    print("Views:", video["views"])
    print("Likes:", video["likes"])
    print("Comments:", video["comments"])


def main():
    print("All videos:")
    print()

    for video in videos:
        print_video(video)
        print()

    total_views = get_video_views(videos)
    print("Total views:", total_views)

    popular_count = count_popular_videos(videos)
    print("Popular videos:", popular_count)

    average = average_views(videos)
    print("Average views:", average)

    most_viewed_video = find_most_viewed(videos)

    print()
    print("Most viewed video:")

    if most_viewed_video is not None:
        print_video(most_viewed_video)

    searched_video = find_video(videos, "Morning Routine")

    print()
    print("Search result:")

    if searched_video is not None:
        print_video(searched_video)
    else:
        print("Video not found.")

    titles = get_video_titles(videos)

    print()
    print("Video titles:", titles)


main()