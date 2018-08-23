import praw # Wrapper for Reddit Api
import config

def main():
    reddit = praw.Reddit(client_id = config.c_id,
                         client_secret = config.c_secret,
                         username = config.username,
                         password = config.password,
                         user_agent= config.user_a)


    subreddit = reddit.subreddit('test')
    newest_posts = subreddit.new(limit=5)

    for posts in subreddit.new(limit=10):
        if "test" in posts.title and posts.visited == False and comment.author != reddit.user.me():
            reply(posts)
        else:
            print("No new posts...")
            break
            
def reply(posts):
    message = open('Reply.txt', 'r+')

    posts.reply(message.read())
    message.close()

if __name__ == '__main__':
    while True:
        main()
