import re
import web
import yaml


urls = (
    '/', 'index'
)


class index:
    def GET(self):
        match = None
        conf = yaml.load(open('speems.cfg', 'r'))
        hostname = web.ctx.env.get('HTTP_X_HOSTNAME')
        spec = open('spec.d/require.rb').read()
        for role in conf:
            for host in conf[role]:
                phost = re.compile(host)
                if phost.match(hostname):
                    spec += open('spec.d/' + role + '_spec.rb', 'r').read()
                    match = 1
        if match is None:
            spec = ""
        return spec

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
