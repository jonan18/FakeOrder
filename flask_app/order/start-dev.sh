function trap_ctrlc ()
{
  docker-compose down
}

#This command will detect Control + C and kill the process in the BG.
trap "trap_ctrlc" 2

docker-compose up -d

while true
do
  curl -d {} http://localhost:8000/rand_piece
  sleep $[ ( $RANDOM % 10 )  + 10 ] #Random 10-20 seconds
done