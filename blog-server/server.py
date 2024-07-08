from flask import Flask
from flask import render_template
import requests
from post import Post

#--------Getting all the posts-------------#
all_posts = []
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
response_data = response.json()
for data in response_data:
    post = Post(data)
    all_posts.append(post)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blog_posts=all_posts)

@app.route('/post/<int:blog_id>')
def display_blog(blog_id):

    blog = None
    for post in all_posts:
        if blog_id == post.id:
            print("True")
            blog = post
            break
    return render_template('post.html', blog=blog)    

if __name__ == "__main__":
    app.run()