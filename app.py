{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cbd98ba0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (1.1.2)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from flask) (2.0.3)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from flask) (2.11.3)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from flask) (2.0.1)\n",
      "Requirement already satisfied: click>=5.1 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from flask) (8.0.4)\n",
      "Requirement already satisfied: importlib-metadata in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from click>=5.1->flask) (4.11.3)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from Jinja2>=2.10.1->flask) (2.0.1)\n",
      "Requirement already satisfied: zipp>=0.5 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from importlib-metadata->click>=5.1->flask) (3.7.0)\n",
      "Requirement already satisfied: typing-extensions>=3.6.4 in /Users/noemimontelongo/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages (from importlib-metadata->click>=5.1->flask) (4.1.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5fe5c40e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "46ebaf8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "17d85fbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7d1c936a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a06bbfa5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ab64ed38",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "09021c48",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5ad25c65",
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "51d76c97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We can view all of the classes that automap found\n",
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cadd3cde",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    185\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 186\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/qc/61mrs1g52x71c76g782d2hmw0000gn/T/ipykernel_66829/1266249183.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mMeasurement\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmeasurement\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mStation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclasses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/sqlalchemy/util/_collections.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m    186\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_data\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    187\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 188\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    189\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    190\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__contains__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: measurement"
     ]
    }
   ],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ee435317",
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "98e10818",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3a77ad1e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/qc/61mrs1g52x71c76g782d2hmw0000gn/T/ipykernel_66829/2751818280.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mapp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"example __name__ = %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m__name__\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Desktop/app.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m    169\u001b[0m   {\n\u001b[1;32m    170\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 171\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    172\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"9872b2b4\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    173\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import app\n",
    "\n",
    "print(\"example __name__ = %s\", __name__)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"example is being run directly.\")\n",
    "else:\n",
    "    print(\"example is being imported\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "69066413",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec03f0b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "flask run"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
