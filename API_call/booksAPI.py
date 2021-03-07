import json
from flask import Response
from flask_restful import Resource, reqparse
from API_call.model import Books
from flask_jwt import jwt_required, current_identity

class ALL_BOOK(Resource):

    def get(self):
        all_book = Books.query.all()
        data = [dict(id=book.id, title=book.title, author=book.author, language=book.language) for book in all_book]
        if len(data) > 0:
            return {'message': 'Success', 'data': data}, 200
        else:
            return 'No Content Found', 404

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help="title cannot be blank!")
        parser.add_argument('author', type=str, required=True, help="author cannot be blank!")
        parser.add_argument('language', type=str, required=True, help="language cannot be blank!")
        # Parse the arguments into an object
        args = parser.parse_args()
        print(args)
        newBook = Books( title=args['title'], author=args['author'], language=args['language'] )
        newBook.save_to_db()
        print("Inserted book id is : {}".format(newBook.id))
        latest = Books.query.filter_by(id=newBook.id).first()
        if latest is not None:
            data = {'message': 'book registered',
                    'data': {'id': latest.id, 'title': latest.title, 'author': latest.author, 'language': latest.language}}
            response = Response(response=json.dumps(data), status=201, mimetype='application/json')
            return response
        else:
            data = {'message': 'Something went wrong. Try again later'}
            response = Response(response=json.dumps(data), status=500, mimetype='application/json')
            return response


class ONE_BOOK(Resource):

    def get(self,id):
        book = Books.query.filter_by(id=id).first()
        if book is not None:
            data = {'message': 'Success',
                    'data': {'id': book.id, 'title': book.title, 'author': book.author, 'language': book.language}}
            response = Response(response=json.dumps(data), status=200, mimetype='application/json')
            return response
        if book is None:
            data = {'message': 'No Content found with this ID. Try something else'}
            response = Response(response=json.dumps(data), status=404, mimetype='application/json')
            return response

    @jwt_required()
    def put(self,id):
        book = Books.query.filter_by(id=id).first()
        if book is not None:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help="title cannot be blank!")
            parser.add_argument('author', type=str, required=True, help="author cannot be blank!")
            parser.add_argument('language', type=str, required=True, help="language cannot be blank!")
            # Parse the arguments into an object
            args = parser.parse_args()
            book.title = args['title']
            book.author = args['author']
            book.language = args['language']
            book.save_to_db()
            updatedBook = Books.query.filter_by(id=id).first()
            data = {'message': 'Success',
                    'data': {'id': updatedBook.id, 'title': updatedBook.title, 'author': updatedBook.author, 'language': updatedBook.language}}
            response = Response(response=json.dumps(data), status=200, mimetype='application/json')
            return response
        if book is None:
            data = {'message': 'No Content found with this ID. Create the resourse using post request.'}
            response = Response(response=json.dumps(data), status=404, mimetype='application/json')
            return response

    @jwt_required()
    def delete(self, id):
        book = Books.query.filter_by(id=id).first()
        if book is not None:
            book.delete_row()
            return "The book with id: {} has been deleted.".format(id), 204

        if book is None:
            data = {'message': 'No Content found with this ID. Try something else'}
            response = Response(response=json.dumps(data), status=404, mimetype='application/json')
            return response

    @jwt_required()
    def patch(self, id):
        book = Books.query.filter_by(id=id).first()
        if book is not None:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('author', type=str )
            parser.add_argument('language', type=str )
            # Parse the arguments into an object
            args = parser.parse_args()
            print(args)
            if args['title'] is not None:
                book.title = args['title']
            if args['author'] is not None:
                book.author = args['author']
            if args['language'] is not None:
                book.language = args['language']

            book.save_to_db()
            updatedBook = Books.query.filter_by(id=id).first()
            data = {'message': 'Success',
                    'data': {'id': updatedBook.id, 'title': updatedBook.title, 'author': updatedBook.author,
                             'language': updatedBook.language}}
            response = Response(response=json.dumps(data), status=200, mimetype='application/json')
            return response

        if book is None:
            data = {'message': 'No Content found with this ID. Create the resourse using post request.'}
            response = Response(response=json.dumps(data), status=404, mimetype='application/json')
            return response







