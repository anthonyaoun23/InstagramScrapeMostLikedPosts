from instaloader import Instaloader, Profile
import os.path

PROFILE = "mindoftoto"   # Insert profile name here

L = Instaloader()

# Obtain profile
profile = Profile.from_username(L.context, PROFILE)

# Get all posts and sort them by their number of likes
posts_sorted_by_likes = sorted(
    profile.get_posts(), key=lambda post: post.likes)

# Download the post with the most likes
current_directory = os.getcwd()
for x in range(10):
    final_directory = os.path.join(current_directory, str(x))


L.download_post(posts_sorted_by_likes[len(posts_sorted_by_likes)-1], PROFILE)
print(posts_sorted_by_likes[len(posts_sorted_by_likes)-1])

if not os.path.exists(final_directory):
    os.makedirs(final_directory)
