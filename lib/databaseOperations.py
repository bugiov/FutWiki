import pymongo
from bson import ObjectId


# CONNECT TO DATABASE
connection = pymongo.MongoClient("localhost", 27017)

# CREATE DATABASE
database = connection['fifa19db']
# CREATE COLLECTION
collection = database['players']
print("Database connected")


def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged

def get_one_player_by_name(player_name):
    """
    get one document data by player_name
    :param player_name:
    :return:
    """
    data = collection.find_one({
        "player_extended_name": {
        "$regex": player_name,
        "$options": 'i'
        }
    })
    return data

def get_data_by_player_name(player_name):
    """
    get document data by player_name
    :param player_name:
    :return:
    """
    data = collection.find({
        "player_name": {
        "$regex": player_name,
        "$options":'i'
        }
    })
    return list(data)

def get_all_quality():
    """
    get all quality of cards
    :param:
    :return:
    """
    data = collection.find().distinct("quality")
    return list(data)

def get_best_5_players(quality):
    """
    get best 5 players ordered by overall
    :param:
    :return:
    """
    data = collection.find({
        "quality": {
            "$regex": quality,
            "$options": 'i'
        }
    }).sort("overall", -1).limit(5)
    return list(data)

def get_valutation_attack(player_name):
    """
    get document data by player_name
    :param player_name:
    :return:
    """
    data = collection.aggregate([
        {'$match': {"player_name": {
                        "$regex": player_name,
                        "$options":'i'
                      }
                    }
        },
        {'$project': {
                    'player_name': 1,
                    'player_extended_name': 1,
                    'quality': 1,
                    'revision': 1,
                    'club': 1,
                    'overall': 1,
                    'nationality': 1,
                    'position': 1,
                    'age': 1,
                    'pass_short':'$pass_short',
                    'shooting':'$shooting',
                    'dribbling':'$dribbling',
                    'pace_sprint_speed':'$pace_sprint_spid',
                    'valutation_attack': {'$avg': [ '$pass_short', '$shooting', '$dribbling', '$pace_sprint_spid'] }
                    }
        }
    ])
    return list(data)

def get_single_data(document_id):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data

def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    data = collection.find()
    return list(data)


def update_existing(document_id, data):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged


def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged


# CLOSE DATABASE
connection.close()
