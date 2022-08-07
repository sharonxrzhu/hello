let counter = 0; //define variable counter
    function count(){
        counter++;
        document.querySelector('h2').innerHTML = counter;

        if(counter % 10 === 0){
            alert(`Count is now ${counter}`);
        }
    }
    document.addEventListener('DOMContentLoaded', function(){ //wait until the DOM or entire page has loaded and run the function
        document.querySelector('button').onclick = count; //count is the function to be run when the button is clicked
    })