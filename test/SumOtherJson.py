from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def testjsonify():
    uuid_name_List = [('Imyong','Sibal'),('migsking','asdf')]
    a = 0

    Return_Str = str(jsonify(
        {
            'user': {
                'id': 'migsking',
                'name': 'mingi',
            }
        }
    ))

    while 1:
        if uuid_name_List is None:
            break
        else:
            Return_Str = Return_Str + str(jsonify(
                {
                    'workbook': {
                        a: {
                            'name': uuid_name_List[a][1],
                            'uuid': uuid_name_List[a][0],
                        },
                    }
                },
            ))

        del(uuid_name_List[a])
        a += 1

    print(jsonify({
        Return_Str
    }))

a = testjsonify()

