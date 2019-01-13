from instaloader import Instaloader, Profile

PROFILE = "mindoftoto"   # Insert profile name here

L = Instaloader()

# Obtain profile
profile = Profile.from_username(L.context, PROFILE)

# Get all posts and sort them by their number of likes
posts_sorted_by_likes = sorted(
    profile.get_posts(), key=lambda post: post.likes)

# Download the post with the most likes
L.download_post(posts_sorted_by_likes[len(posts_sorted_by_likes)-1], PROFILE)
