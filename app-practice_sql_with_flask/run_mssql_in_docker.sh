# pull mssql docker image and run as a container
sudo docker run --name mssql -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=testMSsqlInDocker" -p 1433:1433 -d mcr.microsoft.com/mssql/server

# get a connect with mssql in container
sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "testMSsqlInDocker"
