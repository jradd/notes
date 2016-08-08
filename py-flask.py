from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)


TODOS = {
    'todo1': {'task': 'This is task #1'},
    'todo2': {'task': 'This is task #2'},
    'todo3': {'task': 'This is task #3'},
    }

def abort_on_noent(todo_id):
  if todo_id not in TODOS:
    abort(404, message="ENOENT: Entry {} does not exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# read/get a single entry and delete item
class Todo(Resource):
  def get(self, todo_id):
    abort_on_noent(todo_id)
    return TODOS[todo_id]

  def delete(self, todo_id):
    abort_on_noent(todo_id)
    del TODOS[todo_id]
    return '', 204

  def put(self, todo_id):
    args = parser.parse_args()
    task = {'task': args['task']}
    TODOS[todo_id] = task
    return task, 201


class TodoList(Resource):
  """ List all entries, POST new entry """
  def get(self):
    return TODOS

  def post(self):
    args = parser.parse_args()
    todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    todo_id = 'todo%i' % todo_id
    TODOS[todo_id] = {'task': args['task']}
    return TODOS[todo_id], 201


class UpperString(entries.Raw):
  def format(self, value):
    return value.upper()
  
parser.add_argument('OddNumber', type=odd_number)
parser.add_argument('Status', type=task_status)
entries = {
    'name': entries.String,
    'name_upper': UpperString(attribute=name),
    }

def odd_number(value):
  if value % 2 == 0:
    raise ValueError("Value is not odd")

  return value

  def task_status(value):
    statuses = [u"init", u"in-progress", u"complete", u"deferred"]
    return statuses.index(value)


api = restful.Api(app)

@api.representation('text/csv')
def output_csv(data, code, headers=None):
  pass
# implement csv output

def output_json(data, code, headers=None):
  """ Make flask respond with JSON encoded body """
  resp = make_response(json.dump(data), code)
  resp.headers.extend(headers or {})
  return resp

# Alternative to using api.representation decorator
# Subclassing the Api class
class Api(restful.Api):
  def __init__(self, *args, **kwargs):
    super(Api, self).__init__(*args, **kwargs)
    self.representations = {
        'application/xml': output_xml,
        'text/html': output_html,
        'text/csv': output_csv,
        'application/json': output_json,
        }


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        acct = basic_authentication()  # custom account lookup function

        if acct:
            return func(*args, **kwargs)

        restful.abort(401)
    return wrapper


class Resource(restful.Resource):
    method_decorators = [authenticate]   # applies to all inherited resources

def log_exception(sender, exception, **extra):
    """ Log an exception to our logging framework """
    sender.logger.debug('Got exception during processing: %s', exception)

from flask import got_request_exception
got_request_exception.connect(log_exception, app)


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
  app.run(debug=True)
