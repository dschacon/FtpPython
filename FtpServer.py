import DummyAuthorizer
import FTPHandler
import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/username", perm="labdeRedes")
authorizer.add_anonymous("/home/username", perm="labdeRedes")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()