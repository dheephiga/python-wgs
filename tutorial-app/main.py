from flask import Flask
from flask_restful import Resource, Api,reqparse, abort

app = Flask("VideoAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title',required=True)
videos = {
    'video1': {'title':'Python introduction'},
    'video2': {'title':'Matlab vs Python'}
}

class Video(Resource):
    
    def get(self,video_id):
        if video_id == "all":
            return videos
        return videos[video_id],
    
    def put(self,video_id):
        args = parser.parse_args()
        new_video = {'title':args['title']}
        videos[video_id] = new_video
        return {video_id: videos[video_id]}, 201    
    
    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f'Video {video_id} not found')
        del videos[video_id]
        return "", 204

api.add_resource(Video,'/videos/<video_id>')


if __name__ == "__main__":
    app.run(debug=True)
