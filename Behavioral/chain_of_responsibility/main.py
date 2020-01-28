from Behavioral.chain_of_responsibility import Compressor, Logger, Authenticator, WebServer, HttpRequest

if __name__ == '__main__':
    compressor = Compressor(None)
    logger = Logger(compressor)
    authenticator = Authenticator(logger)
    server = WebServer(authenticator)
    server.handle(HttpRequest("admin", "1234"))
