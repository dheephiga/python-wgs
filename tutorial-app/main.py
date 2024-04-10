from flask import Flask
from flask_restful import Resource, Api

app = Flask("VideoAPI")
api = Api(app)

videos = {
    'video1': {'title':'Python introduction'},
    'video2': {'title':'Matlab vs Python'}
}

class Video(Resource):
    
    def get(self,video_id):
        if video_id == "all":
            return videos
        return videos[video_id]

api.add_resource(Video,'/videos/<video_id>')

if __name__ == "__main__":
    app.run(debug=True)
