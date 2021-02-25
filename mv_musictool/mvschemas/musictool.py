# -*- coding: utf-8 -*-
# import tracemalloc
import os
import logging
import uuid
import datetime
import json
import sys
import getopt
import time
import traceback
import random
import re
import timeit
import pickle
import csv
import subprocess
import pafy
from pytube import YouTube
from pydub import AudioSegment
from mhyt import yt_download
import shutil
from functools import wraps
from flask import abort
import marshmallow as ma
from urllib.error import ContentTooShortError
from marshmallow import Schema, post_load, validate, ValidationError
from mv_musictool.mvmodels.Projects import Project,ProjectFile,TempFileStorage
from mv_musictool.mvexception.exception import MVException, ValidationException,Test
from mongoengine.queryset.visitor import Q
from flask import Flask,jsonify
from flask_pymongo import PyMongo
from flask_restplus import Api, Resource, fields
from bson import ObjectId
from mv_musictool import settings
from mv_musictool.api import utils
from pymongo import MongoClient
import threading
from werkzeug.utils import secure_filename
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.util import Inches
from pptx.opc.package import PartFactory
from pptx.parts.media import MediaPart

PartFactory.part_type_for.update(
    {
        'audio/mp3': MediaPart
    }
)
print (sys.getdefaultencoding())

log = logging.getLogger(__name__)
""" Db initialization """
local=MongoClient()
db=local['test_youtube_db']
coll=db["test_youtube_account"]


WATCH_URL = "https://www.youtube.com/watch?v="


DEFAULT_UPLOAD_PATH = settings.MEDIA_PATH+"/"
BASE_MEDIA_PATH = "mv_musictool/static/media/"
THUMBNAIL_JPG = "_thumbnail.jpg"

#TODO handle mv exception
class ProjectSchema(Schema):
    db_id = ma.fields.Str(allow_none=True)
    
    @post_load
    def make_project(self, data, **kwargs):
        return Project(**data)

'''
    ==============================================
    musictool - Class Factory
    ================================================
'''

class MusicSetFactory(object):

    # db connect in __init__?
    def __init__(self):
        # log.debug ('init')
        pass

    def get_marshalled_schema(self,obj):
        if obj:
            schema=ProjectSchema()
            retdata = schema.dump(obj)
            return retdata
    
    def create_project(self,data):
        i = 0
        proj_obj ={}
        res =[]
        with open('/home/desktop-obs-59/Projects/json_ppt/mv_musictool/input_data.json') as f:
            data = json.load(f)
            
        with open('/home/desktop-obs-59/Projects/json_ppt/mv_musictool/input_json_slide1.json') as f:
            data_first = json.load(f)

        prs = Presentation('/home/desktop-obs-59/Projects/json_ppt/TemplateForJson.pptx')

        k = 0
        slide = prs.slides[0] #first slide
        for val_1 in data_first:
            print(" ".join(data_first[val_1]))
            table = slide.shapes[0].table.cell(0,k).text = val_1
            table = slide.shapes[0].table.cell(1,k).text = " ".join(data_first[val_1])
            k += 1
        
        j =0
        slide = prs.slides[2] #third slide
        for val in data:
            table = slide.shapes[2].table.cell(0,j).text= val
            table = slide.shapes[2].table.cell(2,j).text= data[val]['score']
            j += 1
        
        prs.save("out.pptx")

        outfile_path = '/json_ppt/out.pptx'
        return outfile_path
                   
musicSetFactory = MusicSetFactory()



