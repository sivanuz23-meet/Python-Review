def create_youtube_video(title, description, hashtag):
	youtube_video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments":{}, "hashtag": hashtag}
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

def similarity_to_video(a,b):
	counter = 0
	for i in a:
		if a[i] == b[i]:
			counter+=1
	percentage = counter/len(b)
	print(str(percentage*100.0) + "%")

youtube1 = create_youtube_video("hello world", "video about the world", ["#great", "#good movie"])
youtube2 = create_youtube_video("testing", "random description", ["#good", "#brilliant"])
similarity_to_video(youtube1, youtube2)
for i in range(495):
	like(youtube1)
print(like(youtube1))

print(add_comment(youtube1, "Sivan", "That's a good video"))