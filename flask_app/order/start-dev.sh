python3 app.py &
pid=$!
echo "Process ID HNP!" $pid
sleep 10

sudo python sniffer.py &
pid2=$!
echo "Process ID HNP!" $pid2
sleep 10

function trap_ctrlc ()
{
  kill $pid
  kill $pid2
  exit 2
}

#This command will detect Control + C and kill the process in the BG.
trap "trap_ctrlc" 2

while true
do
  curl -d {} http://localhost:13003/rand_piece
  sleep $[ ( $RANDOM % 10 )  + 10 ] #Random 10-20 seconds
done
