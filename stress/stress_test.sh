curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=A[1-1000]" &
pidlist="$pidlist $!"
curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=B[1-1000]" &
pidlist="$pidlist $!"
curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=C[1-1000]" &
pidlist="$pidlist $!"
curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=D[1-1000]" &
pidlist="$pidlist $!"
curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=E[1-1000]" &
pidlist="$pidlist $!"
curl -L -s "https://ecommerce-autocomplete.appspot.com/?search=F[1-1000]" &
pidlist="$pidlist $!"

for job in $pidlist do 
  echo $job
  wait $job || let "FAIL+=1" 
done  

if [ "$FAIL" == "0" ]; then 
  echo "YAY!" 
else 
  echo "FAIL! ($FAIL)" 
fi
