yum remove -y R-core
rm -rf /var/lib/ambari-server/resources/stacks/HDP/2.2/services/r-service

CLUSTER=Sandbox
USER=admin
PASS=admin
SERVICE=R
HOST=localhost:8080

# Stop service
echo Stopping $SERVICE..
curl -u $USER:$PASS -i -H 'X-Requested-By: ambari' -X PUT -d \
  '{"RequestInfo": {"context" :"Stop '"$SERVICE"' via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' \
  http://$HOST/api/v1/clusters/$CLUSTER/services/$SERVICE

finished=0
while [ $finished -ne 1 ]
do
  str=$(curl -s -u $USER:$PASS http://{$HOST}/api/v1/clusters/$CLUSTER/services/$SERVICE)
  if [[ $str == *"$2"* ]] || [[ $str == *"Not Found"* ]] 
  then
    finished=1
  fi
  echo Waiting for $SERVICE to stop..
  sleep 1
done

echo Removing $SERVICE from Ambari Service Registry..
curl -u $USER:$PASS -i -H 'X-Requested-By: ambari' -X DELETE http://$HOST/api/v1/clusters/$CLUSTER/services/$SERVICE
