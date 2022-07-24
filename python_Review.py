def create_youtube_video(title, description):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments":{"username" : ""}}
	return youtube_video
def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video

def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video
def add_comment(video, username, comment_text):
