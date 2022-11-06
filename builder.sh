function lambda_function_builder { 
    mkdir -p ./results
    result_dir = $(realpath ./results)
    pushd ./src/
    for f in *;  do 
        if [[ "$f" != "helper" && "$f" != "lambda-extension" && -d $f ]]; 
        then  
            echo "$f"
            pushd "$f";
            sam build 
            cd .aws-sam/build/LambdaFunction/
            zip -r ../../../../../results/"$f" .  
            echo "Doing something in folder `pwd`/$f"; 
            popd; 
        fi;  
    done;  
    popd
};
lambda_function_builder
