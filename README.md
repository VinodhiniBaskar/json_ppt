# My project's README
### uses rest_plus
**Note:** you must do the following before run

~~~~
development mode
~~~~~~~~~~~~~~~~
To run
cd mv_neuroaligner_services
$ export PYTHONPATH=.:$PYTHONPATH
./flask_deploy.sh

or

$ export PYTHONPATH=.:$PYTHONPATH
$ python mv_musictool/app.py'


production mode
~~~~~~~~~~~~~~~~
To run
cd mv_neuroaligner_services
change settings.py file like in
replace :- 
gunicorn_debug = True
flask_debug =False

$ export PYTHONPATH=.:$PYTHONPATH
./gdeploy.sh

or

$ export PYTHONPATH=.:$PYTHONPATH
$ gunicorn -w 10 -b 0.0.0.0:7003 wsgi:app --daemon





  
