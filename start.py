from data.server import server ##import server / enough to start the online-version (Azure WebApp)
server.run(debug=True,port=2222,host="localhost") ##run server / needed for offline version (local machine)