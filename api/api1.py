from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

todos = {

1:  {"task":"write hello world program","summary":"code using python."},
2:  {"task":"Task 2","summary":"code using task 2."},
3:  {"task":"Task 3","summary":"code using task 3."},

}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help= "task is required", required=True)
task_post_args.add_argument("summary", type=str, help= "summary is required", required=True)


class TodoList(Resource):
    def get(self):
        return todos	

class TodoSimple(Resource):
    def get(self, todo_id):
        return todos[todo_id]

    def post(self, todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409,"Task ID exist")
        todos[todo_id] = {"task":args["task"],"summary":args["summary"]}
        return todos[todo_id]
       

    
api.add_resource(TodoSimple, '/todos/<int:todo_id>')

api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True)