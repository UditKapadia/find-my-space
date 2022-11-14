from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyB0OYzIwElxzKxTH9yWmGKHcVglGC81900",
    "authDomain": "find-your-space.firebaseapp.com",
    "databaseURL": "https://find-your-space-default-rtdb.firebaseio.com",
    "databaseURL": "https://find-your-space-default-rtdb.firebaseio.com",
    "projectId": "find-your-space",
    "storageBucket": "find-your-space.appspot.com",
    "messagingSenderId": "1085509776338",
    "appId": "1:1085509776338:web:fbdb27e77711addae04e0b"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

# Create your views here.


def index(request):
    parking_status = database.child(
        "parking-spaces").child("parking_status").get().val()
    available_slots = database.child(
        "parking-spaces").child("available_slots").get().val()
    sensor_1_status = database.child(
        "parking-spaces").child("slot_1").get().val()
    sensor_2_status = database.child(
        "parking-spaces").child("slot_2").get().val()
    sensor_3_status = database.child(
        "parking-spaces").child("slot_3").get().val()
    sensor_4_status = database.child(
        "parking-spaces").child("slot_4").get().val()
    sensor_5_status = database.child(
        "parking-spaces").child("slot_5").get().val()
    sensor_6_status = database.child(
        "parking-spaces").child("slot_6").get().val()

    return render(request, "smart_parking/index.html", {
        "parking_status": parking_status,
        "available_slots": available_slots,
        "sensor_1_status": sensor_1_status,
        "sensor_2_status": sensor_2_status,
        "sensor_3_status": sensor_3_status,
        "sensor_4_status": sensor_4_status,
        "sensor_5_status": sensor_5_status,
        "sensor_6_status": sensor_6_status,
    })
