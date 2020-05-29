# SDE Online Assessment-My solution


## Usage Example
`$ docker build -t zhengsolution .`
`$ docker run -d -P <containID>`

ISSUE: Currently the docker image can be built built, but I cannot not start the container, maybe the code in dockerfile is problematic. 

The requirement for run the app is Python 3.7.6, and there is no more dependency.

The code can be run and tested successfully on my local desktop, the only issue is that I could not start running it in docker container.

To test without docker enviroment , just simply type `$ python sde-test-solution.py sample_input_2.json sample_output_2.json` in the command line, the last 2 arguments could be any names for the JSON file

## Testing 

This app uses Python built-in unittest pacakge. The function tests the sample JSON file as well as some special situation such as the tie for the same tenor difference.

For testing, just run the test.py file and give the input-file `sample_input_2.json` and expected output file `sample_output_2_expected.json`, the unit test code will automatically test if the app could successfully ouput the JSON file with the same expected content.

