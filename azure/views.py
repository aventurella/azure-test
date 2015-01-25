from django.shortcuts import render
import zmq


def action(request, **kwargs):
    return render(request, "view.html", {})


def foo(request, **kwargs):
    context = zmq.Context()

    push = context.socket(zmq.PUSH)
    push.bind("inproc://test")

    pull = context.socket(zmq.PULL)
    pull.connect("inproc://test")

    msg = {"data": "GOT IT!"}

    push.send_json(msg)

    msg_back = pull.recv_json()

    return render(request, "foo.html", msg_back)
