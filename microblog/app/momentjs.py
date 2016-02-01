from jinja2 import Markup


class Momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def render(self, format):
        return Markup("<script>\ndocument.write(moment('{0}').{1})\n</script>".format(
                self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format))

    def format(self, fmt):
        return self.render("format({0})".format(fmt))

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")
