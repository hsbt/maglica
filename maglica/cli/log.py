import maglica.request_log
import maglica.util
from termcolor import cprint
import json

def status(args):
    options = {
        "mandatory": ["id"],
        "optional":  [],
    }
    maglica.util.check_args(args, options)
    request_log = maglica.request_log.RequestLog()

    row = request_log.get_status(args["id"])

    status  = row["status"]
    args    = json.loads(row["args"])
    message = row["message"]

    if status == 0:
        cprint("In progress", "yellow")
        options = []
        for key in args["args"].keys():
            options.append("--%s=%s" % (key, args["args"][key]))
        options = " ".join(options)
        print "Running %s %s %s on %s" % ( args["type"], args["action"], options, args["host"])
    elif status == 1:
        cprint("Completed", "green")
    elif status == 2:
        cprint("Error", "red")

    if message:
        print message

