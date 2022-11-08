from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.log import LogModel


class Log(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('spreadsheet_title',
                        type=str,
                        required=True,
                        help="Every item needs a Spreadsheet Title."
                        )
    parser.add_argument('spreadsheet_id',
                        type=str,
                        required=True,
                        help="Every item needs a Spreadsheet ID."
                        )
    parser.add_argument('api_key',
                        type=str,
                        required=True,
                        help="Every log needs a API KEY."
                        )
    parser.add_argument('trigger_source',
                        type=str,
                        required=False,
                        help="Every log needs a Trigger Source."
                        )
    parser.add_argument('api_hits',
                        type=int,
                        required=False,
                        help="Every log needs a API hits #."
                        )
    parser.add_argument('tsa_owner',
                        type=str,
                        required=False,
                        help="Every log needs a TSA Owner."
                        )

    def post(self):
        data = Log.parser.parse_args()
        log = LogModel(**data)
        try:
            log.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return {"message": "Log successfully add to the db."}, 201

class LogsList(Resource):
    @jwt_required()
    def get(self):
        return {'logs': list(map(lambda x: x.json(), LogModel.query.all()))}
