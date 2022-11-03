function lambda_function_builder { 
    mkdir -p ./results
    cd ./src/
    for f in *;  do 
        if [[ "$f" != "helper" && "$f" != "lambda-extension" && -d $f ]]; 
        then  
            echo "$f"
            cd "$f";
            sam build 
            cd .aws-sam/build/LambdaFunction/
            zip -r ../../../../../results/"$f" .  
            echo "Doing something in folder `pwd`/$f"; 
            cd ../../../../; 
        fi;  
    done;  
    cd ..
};
lambda_function_builder
