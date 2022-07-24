def create_youtube_video(title, description):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments":{}}
	return youtube_video
def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video

def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1
	return video
def add_comment(video, username, comment_text):
	video["comments"][username] = comment_text
	return video

youtube = create_youtube_video("hello world", "video about the world")
for i in range(495):
	like(youtube)
print(like(youtube))

print(add_comment(youtube, "Sivan", "That's a good video"))